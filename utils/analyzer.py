# utils/analyzer.py

from utils.reference_ranges import get_reference_range, get_critical_limits

def assess_risk(test_name: str, value: float, unit: str = None, 
                gender: str = "default", age_group: str = "adult"):
    """
    Assess risk level for a lab value.
    
    Args:
        test_name: Name of the test
        value: Numeric value
        unit: Unit of measurement (for validation)
        gender: Patient gender
        age_group: Patient age group
    
    Returns:
        dict: {
            "status": "green"/"yellow"/"red",
            "range": reference range string,
            "message": explanation,
            "bar_pct": percentage for visual bar
        }
    """
    
    # Get reference range
    ref_range = get_reference_range(test_name, gender, age_group)
    
    if not ref_range:
        return {
            "status": "yellow",
            "range": "Reference range not available",
            "message": f"Unable to find reference range for {test_name}",
            "bar_pct": 50
        }
    
    min_val = ref_range.get("min", 0)
    max_val = ref_range.get("max", 100)
    
    # Check critical limits first
    critical = get_critical_limits(test_name)
    if critical:
        if value < critical.get("low", -float('inf')):
            return {
                "status": "red",
                "range": f"{min_val} – {max_val}",
                "message": f"CRITICALLY LOW: {test_name} is dangerously below normal range. Seek immediate medical attention.",
                "bar_pct": 10
            }
        if value > critical.get("high", float('inf')):
            return {
                "status": "red",
                "range": f"{min_val} – {max_val}",
                "message": f"CRITICALLY HIGH: {test_name} is dangerously above normal range. Seek immediate medical attention.",
                "bar_pct": 90
            }
    
    # Calculate percentage for visual bar
    # Normalize to 0-100% range for display
    normal_center = (max_val + min_val) / 2
    if value < min_val:
        # Below range - calculate how far below
        pct = max(10, (value / min_val) * 30)  # Cap at 30% for below range
        bar_pct = min(30, pct)
    elif value > max_val:
        # Above range - calculate how far above
        ratio = value / max_val
        pct = min(90, 70 + (ratio * 20))
        bar_pct = min(90, pct)
    else:
        # Within range - map to 30-70% range
        bar_pct = 30 + ((value - min_val) / (max_val - min_val) * 40)
    
    # Risk assessment logic
    if min_val <= value <= max_val:
        # Normal range
        return {
            "status": "green",
            "range": f"{min_val} – {max_val}",
            "message": f"Your {test_name} is within the normal range ({min_val}–{max_val} {unit}).",
            "bar_pct": int(bar_pct)
        }
    
    elif value < min_val:
        # Below normal
        deviation_pct = ((min_val - value) / min_val) * 100
        
        if deviation_pct < 10:
            status = "yellow"
            message = f"Your {test_name} is slightly below normal ({min_val}–{max_val} {unit}). Consider monitoring."
        else:
            status = "red"
            message = f"Your {test_name} is significantly below normal ({min_val}–{max_val} {unit}). Please consult your doctor."
        
        return {
            "status": status,
            "range": f"{min_val} – {max_val}",
            "message": message,
            "bar_pct": int(bar_pct)
        }
    
    else:  # value > max_val
        # Above normal
        deviation_pct = ((value - max_val) / max_val) * 100
        
        if deviation_pct < 10:
            status = "yellow"
            message = f"Your {test_name} is slightly above normal ({min_val}–{max_val} {unit}). Lifestyle modifications may help."
        else:
            status = "red"
            message = f"Your {test_name} is significantly above normal ({min_val}–{max_val} {unit}). Please consult your doctor."
        
        return {
            "status": status,
            "range": f"{min_val} – {max_val}",
            "message": message,
            "bar_pct": int(bar_pct)
        }


def process_lab_results(extracted_data: dict, patient_context: dict = None):
    """
    Process multiple lab results from extraction.
    
    Args:
        extracted_data: Dictionary of {test_name: value} from Ameer's extractor
        patient_context: Optional dict with gender, age, etc.
    
    Returns:
        List of processed results matching the dashboard format
    """
    if patient_context is None:
        patient_context = {"gender": "default", "age_group": "adult"}
    
    results = []
    
    for test_name, value_info in extracted_data.items():
        # Handle different possible formats from extractor
        if isinstance(value_info, dict):
            value = value_info.get("value")
            unit = value_info.get("unit", "")
        else:
            value = value_info
            unit = ""
        
        # Skip non-numeric values
        try:
            value = float(str(value).replace(',', ''))
        except (ValueError, TypeError):
            continue
        
        # Assess risk
        risk_info = assess_risk(test_name, value, unit, 
                               patient_context.get("gender", "default"),
                               patient_context.get("age_group", "adult"))
        
        results.append({
            "name": test_name.title().replace("_", " "),
            "value": value,
            "unit": unit,
            "reference": risk_info["range"],
            "status": risk_info["status"],
            "bar_pct": risk_info["bar_pct"],
            "explanation": risk_info["message"]
        })
    
    return results