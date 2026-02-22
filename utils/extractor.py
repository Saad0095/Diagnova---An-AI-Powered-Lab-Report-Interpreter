# utils/extractor.py

"""
Lab report text extraction and cleaning module.
Extracts lab test values from pasted text using LLM and cleans them for analysis.
"""

import json
import re
from typing import Dict
import streamlit as st
from groq import Groq


def call_llm(prompt: str) -> str:
    """
    Call Groq LLM API to extract structured data from text.
    
    Uses Groq's fast inference with Mixtral model for JSON extraction.
    Falls back to empty JSON if API call fails.
    
    Args:
        prompt: The prompt to send to the LLM
        
    Returns:
        str: LLM response (should be valid JSON)
    """
    try:
        # Get API key from Streamlit secrets
        api_key = st.secrets.get("GROQ_API_KEY", "")
        
        if not api_key:
            # No API key - return empty JSON
            print("⚠️ No GROQ_API_KEY found in secrets")
            return "{}"
        
        print(f"✅ API key found, calling Groq...")
        
        # Initialize Groq client
        client = Groq(api_key=api_key)
        
        # Call Groq API
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Fast, accurate model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,  # Low temperature for consistent JSON output
            max_tokens=2000
        )
        
        result = response.choices[0].message.content
        print(f"✅ LLM response received ({len(result)} chars)")
        return result
        
    except Exception as e:
        # API call failed - return empty JSON safely
        print(f"❌ LLM call failed: {str(e)}")
        return "{}"


def extract_json_from_llm(text: str) -> dict:
    """
    Extract lab values from raw report text using LLM.
    
    Args:
        text: Raw lab report text from user input
        
    Returns:
        dict: Extracted lab values (may need cleaning), empty dict on failure
    """
    # Build prompt for LLM
    prompt = f"""Extract all lab test names and their numeric values from the following lab report.

Return ONLY valid JSON in this exact format:
{{
  "Test Name": numeric_value,
  "Another Test": numeric_value
}}

Rules:
- Use standard medical test names (e.g., "Hemoglobin", "WBC Count", "Glucose")
- Extract ONLY the numeric value, ignore units
- Do NOT include any explanations, markdown, or extra text
- Return ONLY the JSON object

Lab Report Text:
{text}

JSON Output:"""

    try:
        # Call LLM
        llm_response = call_llm(prompt)
        cleaned = llm_response.strip()
        
        # Remove markdown code blocks if present
        if "```" in cleaned:
            # Extract content between first { and last }
            start = cleaned.find("{")
            end = cleaned.rfind("}")
            if start != -1 and end != -1 and end > start:
                cleaned = cleaned[start:end+1]
        
        # Parse JSON
        data = json.loads(cleaned)
        
        # Ensure it's a dict
        return data if isinstance(data, dict) else {}
        
    except:
        # Any error - return empty dict safely
        return {}


def clean_lab_values(data: dict) -> dict:
    """
    Clean extracted lab values to ensure Dict[str, float] format.
    
    Converts all values to float, removes units, handles nested dicts.
    Skips any value that cannot be converted to float.
    
    Args:
        data: Dictionary from LLM (may contain units, strings, nested objects)
        
    Returns:
        dict: Clean dictionary with format {test_name: float_value}
              GUARANTEED to only contain float values
    """
    cleaned = {}
    
    for key, val in data.items():
        try:
            # Skip None or empty
            if val is None or val == "":
                continue
            
            # Handle nested dict - extract 'value' key if present
            if isinstance(val, dict):
                val = val.get("value")
                if val is None:
                    continue
            
            # If already numeric, convert directly
            if isinstance(val, (int, float)):
                cleaned[key] = float(val)
                continue
            
            # String processing - extract first number found
            # Remove symbols and commas first
            val_str = str(val).replace("<", "").replace(">", "").replace(",", "")
            
            # Extract number (handles negative, decimal)
            match = re.search(r'-?\d+\.?\d*', val_str)
            
            if match:
                # Convert to float - this is the ONLY place we add to cleaned dict
                # Guarantees all values are float
                cleaned[key] = float(match.group(0))
        
        except:
            # Skip any value that fails conversion
            continue
    
    return cleaned


def regex_fallback_extraction(text: str) -> dict:
    """
    Simple regex-based fallback extraction when LLM fails.
    
    Extracts patterns like:
    - Hemoglobin: 9.8
    - WBC 12000
    - MCV - 70
    
    Args:
        text: Raw lab report text
        
    Returns:
        dict: Extracted values {test_name: value_string}
    """
    results = {}
    
    try:
        # Split into lines
        lines = text.strip().split('\n')
        
        for line in lines:
            # Pattern: Word(s) followed by separator (:, -, or space) then number
            # Matches: "Hemoglobin: 9.8" or "WBC 12000" or "MCV - 70"
            match = re.match(r'([A-Za-z\s]+?)[\s:=-]+([0-9,.<>]+(?:\s*[A-Za-z/μ°%]+)?)', line.strip())
            
            if match:
                test_name = match.group(1).strip()
                value = match.group(2).strip()
                
                # Only keep if test name looks reasonable (2-30 chars)
                if 2 <= len(test_name) <= 30:
                    results[test_name] = value
    
    except:
        pass
    
    return results


def process_lab_report(text: str) -> dict:
    """
    Main function to process raw lab report text into clean lab values.
    
    Pipeline:
    1. Extract values using LLM
    2. Clean and normalize to Dict[str, float]
    3. Fallback to regex extraction if LLM fails
    4. Return result ready for risk analysis
    
    Args:
        text: Raw lab report text pasted by user
        
    Returns:
        dict: Clean dictionary {test_name: float_value}
              Empty dict if processing fails
              GUARANTEED: Dict[str, float] format - no strings, no nested objects
              
    Example Output:
        {
            "Hemoglobin": 9.8,
            "WBC Count": 12000.0,
            "MCV": 70.0
        }
    """
    # Validate input
    if not text or not isinstance(text, str) or not text.strip():
        print("❌ No valid text provided")
        return {}
    
    try:
        text = text.strip()
        print(f"📝 Processing {len(text)} characters of text...")
        
        # Step 1: Try LLM extraction first
        extracted_data = extract_json_from_llm(text)
        cleaned_data = clean_lab_values(extracted_data)
        
        if cleaned_data:
            print(f"✅ LLM extraction successful: {len(cleaned_data)} values")
        else:
            print("⚠️ LLM extraction returned empty, trying regex fallback...")
            # Step 2: If LLM failed, try regex fallback
            fallback_data = regex_fallback_extraction(text)
            cleaned_data = clean_lab_values(fallback_data)
            if cleaned_data:
                print(f"✅ Regex fallback successful: {len(cleaned_data)} values")
            else:
                print("❌ Both LLM and regex extraction failed")
        
        # Step 3: Final safeguard - ensure all values are float
        result = {k: v for k, v in cleaned_data.items() if isinstance(v, float)}
        print(f"📊 Final result: {len(result)} valid lab values")
        return result
        
    except Exception as e:
        # Never crash the app
        print(f"❌ Exception in process_lab_report: {str(e)}")
        return {}
