<div align="center">

# 🧬 Diagnova
### AI-Powered Lab Report Interpreter

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![HuggingFace](https://img.shields.io/badge/Deployed%20on-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-00a67e?style=for-the-badge)](LICENSE)

**Transforming complex diagnostic reports into clear, actionable health insights — instantly.**

[🚀 Live Demo](https://huggingface.co/spaces/Ameer-Hamza-Afridi/Diagnova) · [📋 Report Issue](https://github.com/Saad0095/Diagnova---An-AI-Powered-Lab-Report-Interpreter/issues) · [💡 Request Feature](https://github.com/Saad0095/Diagnova---An-AI-Powered-Lab-Report-Interpreter/issues)

</div>

---

## 🩺 The Problem

Every day, millions of patients receive lab reports filled with medical jargon, cryptic abbreviations, and numerical values they don't understand. Without context, a number like **"Hemoglobin: 11.2 g/dL"** means nothing to a patient — but it could indicate anemia that needs urgent attention.

**The gap between medical data and patient understanding is a real healthcare crisis.**

---

## 💡 Our Solution

**Diagnova** is an AI-powered medical report interpreter that bridges this gap. Upload your lab report and within seconds receive:

- ✅ **Structured extraction** of all clinical values
- 🎯 **Risk stratification** using Green / Yellow / Red color coding
- 📖 **Plain language explanations** for every parameter
- 🔗 **Pattern recognition** linking related parameters (e.g., Hemoglobin + MCV + Ferritin)
- 📋 **Actionable next steps** — Monitor / Consult / Urgent

> **Diagnova doesn't replace doctors. It empowers patients.**

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📄 **Multi-format Upload** | Supports PDF, PNG, JPG lab reports |
| ✏️ **Text Input** | Paste raw lab values directly |
| 🧪 **8+ Report Types** | CBC, LFT, KFT, Thyroid, Lipid Profile & more |
| 🟢🟡🔴 **Risk Stratification** | Clear Normal / Borderline / Abnormal classification |
| 🤖 **AI Summary** | Concise plain-language overview of your results |
| 📋 **Next Steps** | Prioritized recommendations: Monitor, Consult, Urgent |
| 📥 **Download Report** | Export your interpreted summary as a text file |
| 📱 **Fully Responsive** | Works seamlessly on desktop and mobile |

---

## 🏗️ Project Architecture

```
Diagnova/
│
├── app.py                        # Main Streamlit app + global CSS theming
├── requirements.txt              # Python dependencies
├── README.md                     # You are here
│
├── components/                   # Frontend UI components
│   ├── __init__.py
│   ├── upload_section.py         # File upload + text input interface
│   ├── result_dashboard.py       # Color-coded result cards + summary
│   └── sidebar.py                # Info expander (how it works, legend)
│
└── utils/                        # AI & rule engine (backend logic)
    ├── extractor.py              # PDF/image text extraction (OCR)
    ├── analyzer.py               # Reference range checking + risk logic
    └── reference_ranges.py       # Medically accepted reference values
```

---

## 🔬 How It Works

```
📄 User uploads lab report
         ↓
🔍 AI extracts clinical values (OCR + NLP)
         ↓
📊 Rule engine checks against reference ranges
         ↓
🎨 Risk stratification: Green / Yellow / Red
         ↓
💬 AI explains each value in plain language
         ↓
📋 Actionable next steps generated
```

---

## 🎨 Design System

Diagnova uses a professional medical color palette inspired by leading healthcare platforms:

| Token | Color | Usage |
|---|---|---|
| Primary Blue | `#0a2472` | Headers, hero, buttons |
| Action Blue | `#2d8ef5` | Accents, links |
| ✅ Normal | `#00a67e` | Values within range |
| ⚠️ Borderline | `#c97800` | Slightly out of range |
| 🚨 Abnormal | `#d93025` | Significantly out of range |
| Background | `#f0f6ff` | Page background |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Saad0095/Diagnova---An-AI-Powered-Lab-Report-Interpreter.git
cd Diagnova---An-AI-Powered-Lab-Report-Interpreter

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎉

---

## 🧩 Team Roles & Contributions

| Member | Role | Responsibilities |
|---|---|---|
| **Hamza** | Frontend / UI | Streamlit interface, result dashboard, upload section, responsive design |
| **Saad** | AI & Backend | LLM integration, report extraction, prompt engineering |
| **[Member 3]** | Rule Engine | Reference ranges, risk stratification, medical reasoning |
| **[Member 4]** | Data & Testing | Test cases, validation, medical data accuracy |

---

## 🔌 Integration Guide for Teammates

The frontend expects results in this exact format from the backend:

```python
# Expected output from utils/analyzer.py
results = [
    {
        "name":        "Hemoglobin",        # Parameter name
        "value":       11.2,                # Extracted numeric value
        "unit":        "g/dL",              # Unit of measurement
        "reference":   "13.5 – 17.5",      # Normal reference range
        "status":      "red",               # "green" | "yellow" | "red"
        "bar_pct":     55,                  # Visual bar fill 0–100
        "explanation": "Your hemoglobin..." # Plain language explanation
    },
]

summary    = "Overall plain language summary..."
next_steps = [
    {"tag": "urgent",  "icon": "🚨", "text": "See a physician immediately..."},
    {"tag": "consult", "icon": "⚠️", "text": "Schedule a follow-up..."},
    {"tag": "monitor", "icon": "✅", "text": "Monitor with diet changes..."},
]
```

Replace `MOCK_RESULTS`, `MOCK_SUMMARY`, and `MOCK_NEXT_STEPS` in `components/result_dashboard.py` with real output from the AI pipeline.

---

## 📦 Dependencies

```
streamlit      — Web application framework
Pillow         — Image processing
PyMuPDF        — PDF text extraction
```

---

## 🌐 Deployment

Diagnova is live on **Hugging Face Spaces**:

🔗 **[huggingface.co/spaces/Ameer-Hamza-Afridi/Diagnova](https://huggingface.co/spaces/Ameer-Hamza-Afridi/Diagnova)**

---

## ⚕️ Medical Disclaimer

> Diagnova is an **educational tool** designed to help patients understand their lab results. It does **not** replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider with questions about your health.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ for **Hackathon 2025**

**🧬 Diagnova — Understanding Your Health, Simplified**

</div>
