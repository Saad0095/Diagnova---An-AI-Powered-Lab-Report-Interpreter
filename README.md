# 🧬 LabLens AI — Medical Report Interpreter

> An AI-powered lab report interpreter that transforms complex diagnostic data into clear, color-coded, patient-friendly insights.

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py
```

---

## 📁 Folder Structure

```
/ (repo root)
│
├── app.py                        ← Main Streamlit app + global CSS
├── requirements.txt              ← Python dependencies
├── README.md                     ← This file
│
├── components/                   ← Frontend UI components (your role)
│   ├── __init__.py
│   ├── upload_section.py         ← File upload + text input UI
│   ├── result_dashboard.py       ← Colored result cards + summary + next steps
│   └── sidebar.py                ← Sidebar with instructions & legend
│
└── utils/                        ← AI & rule engine (teammates' role)
    ├── extractor.py              ← PDF/image text extraction
    ├── analyzer.py               ← Reference range checking + risk stratification
    └── reference_ranges.py       ← Medically accepted reference values
```

---

## 🎨 Design System

| Token          | Value        |
|----------------|--------------|
| Primary BG     | `#050d1a`    |
| Card BG        | `#0a1f35`    |
| Accent Cyan    | `#00c8ff`    |
| Normal (Green) | `#00e676`    |
| Borderline     | `#ffd740`    |
| Abnormal (Red) | `#ff5252`    |
| Heading Font   | Sora         |
| Mono Font      | JetBrains Mono |
| Body Font      | Crimson Pro  |

---

## 🔌 Integration for Teammates

`result_dashboard.py` uses `MOCK_RESULTS` as placeholder data.
Replace it with real output from your AI/rule engine in this format:

```python
[
    {
        "name":        "Hemoglobin",      # Parameter name
        "value":       11.2,              # Extracted numeric value
        "unit":        "g/dL",            # Unit of measurement
        "reference":   "13.5 – 17.5",    # Normal reference range string
        "status":      "red",             # "green" | "yellow" | "red"
        "bar_pct":     55,                # Visual bar fill 0–100
        "explanation": "..."              # Plain language explanation
    },
    ...
]
```

---

## ⚕️ Disclaimer

LabLens AI is an educational tool. It does not replace professional medical advice. Always consult a qualified healthcare provider.