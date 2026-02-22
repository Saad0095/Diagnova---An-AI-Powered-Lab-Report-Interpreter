# Setup Instructions for Diagnova

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Get Groq API Key

1. Go to https://console.groq.com/keys
2. Sign up or log in (free account)
3. Create a new API key
4. Copy the key

## 3. Configure API Key

Open `.streamlit/secrets.toml` and replace the placeholder:

```toml
GROQ_API_KEY = "gsk_your_actual_api_key_here"
```

## 4. Run the Application

```bash
streamlit run app.py
```

## 5. Test the Application

1. Click on "✏️ Paste Text" input method
2. Paste sample lab report text like:

```
Hemoglobin: 11.2 g/dL
WBC Count: 7,800 /μL
Fasting Glucose: 108 mg/dL
Platelets: 145,000 /μL
Creatinine: 0.9 mg/dL
Total Cholesterol: 215 mg/dL
```

3. Select report type (e.g., "🩸 Complete Blood Count (CBC)")
4. Click "🔍 Analyze Report"
5. Wait for AI extraction and analysis
6. View results with risk assessment

## Troubleshooting

**If you see empty results:**
- Check that your Groq API key is correctly set in `.streamlit/secrets.toml`
- Ensure you have internet connection
- Check terminal for any error messages

**If analysis is slow:**
- Groq is usually very fast (< 2 seconds)
- Check your internet connection
- Verify API key is valid

## Architecture

```
User Input (Pasted Text)
    ↓
utils/extractor.py
    → process_lab_report() - extracts values using Groq LLM
    ↓
Dict[str, float] - e.g., {"Hemoglobin": 11.2, "WBC": 7800}
    ↓
utils/analyzer.py
    → process_lab_results() - assesses risk levels
    ↓
List[dict] - results with status (green/yellow/red)
    ↓
components/result_dashboard.py
    → Displays visual results with cards, charts, recommendations
```

## Features

✅ AI-powered text extraction using Groq LLM
✅ Automatic unit removal and value cleaning
✅ Risk assessment against medical reference ranges
✅ Visual dashboard with color-coded results
✅ Personalized recommendations
✅ Download report summary

## Notes

- Currently supports **pasted text only** (PDF/image upload UI exists but not wired)
- Uses Groq Mixtral-8x7b model (fast and free)
- Reference ranges from standard clinical guidelines
- This is a hackathon MVP - not for medical diagnosis
