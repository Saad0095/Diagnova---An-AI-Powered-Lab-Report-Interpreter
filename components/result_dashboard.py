import streamlit as st
import time

# ── Mock data ─────────────────────────────────────────────────────────────────
# NOTE FOR TEAMMATES: Replace MOCK_RESULTS with real AI/rule engine output.
MOCK_RESULTS = [
    {
        "name": "Hemoglobin",
        "value": 11.2,
        "unit": "g/dL",
        "reference": "13.5 – 17.5",
        "status": "red",
        "bar_pct": 55,
        "explanation": "Your hemoglobin is below the normal range, which may indicate anemia. This can cause fatigue, weakness, or shortness of breath.",
    },
    {
        "name": "WBC Count",
        "value": 7800,
        "unit": "/μL",
        "reference": "4,500 – 11,000",
        "status": "green",
        "bar_pct": 65,
        "explanation": "White blood cell count is within a healthy range, indicating your immune system is functioning normally.",
    },
    {
        "name": "Fasting Glucose",
        "value": 108,
        "unit": "mg/dL",
        "reference": "70 – 100",
        "status": "yellow",
        "bar_pct": 78,
        "explanation": "Slightly above normal fasting glucose. This may suggest pre-diabetic tendencies and warrants monitoring.",
    },
    {
        "name": "Platelets",
        "value": 145000,
        "unit": "/μL",
        "reference": "150,000 – 400,000",
        "status": "yellow",
        "bar_pct": 30,
        "explanation": "Platelet count is marginally below the reference range. This could affect blood clotting. Retest recommended.",
    },
    {
        "name": "Creatinine",
        "value": 0.9,
        "unit": "mg/dL",
        "reference": "0.7 – 1.3",
        "status": "green",
        "bar_pct": 50,
        "explanation": "Creatinine is at a healthy level, indicating your kidneys are filtering waste efficiently.",
    },
    {
        "name": "Total Cholesterol",
        "value": 215,
        "unit": "mg/dL",
        "reference": "< 200",
        "status": "yellow",
        "bar_pct": 82,
        "explanation": "Slightly elevated cholesterol. Dietary adjustments and regular exercise may help bring this to a healthier range.",
    },
]

MOCK_SUMMARY = (
    "Your CBC panel shows mild anemia with hemoglobin at 11.2 g/dL, which may be linked "
    "to iron or vitamin B12 deficiency — further ferritin and B12 tests are advisable. "
    "Fasting glucose at 108 mg/dL places you in the pre-diabetic range; lifestyle modifications "
    "are strongly encouraged. Platelet count is slightly low and should be rechecked in 4–6 weeks. "
    "Your immune and kidney markers are within healthy limits."
)

MOCK_NEXT_STEPS = [
    {"tag": "urgent",  "icon": "🚨", "text": "Consult a physician regarding your hemoglobin level. Consider iron studies (ferritin, TIBC) and B12 assessment."},
    {"tag": "consult", "icon": "⚠️", "text": "Schedule a follow-up for fasting glucose. Consider an HbA1c test for a 3-month glucose average."},
    {"tag": "consult", "icon": "⚠️", "text": "Recheck platelet count in 4–6 weeks. Avoid NSAIDs and report any unusual bruising to your doctor."},
    {"tag": "monitor", "icon": "✅", "text": "Maintain a low-saturated-fat diet to manage cholesterol. A follow-up lipid panel in 3 months is recommended."},
]


def _status_label(status: str) -> str:
    return {"green": "Normal", "yellow": "Borderline", "red": "Abnormal"}.get(status, "")


def _render_single_card(r: dict):
    s   = r["status"]
    lbl = _status_label(s)
    val = f"{r['value']:,}" if isinstance(r["value"], int) else str(r["value"])
    st.markdown(f"""
    <div class="result-card {s}">
        <div class="rc-header">
            <span class="rc-name">{r['name']}</span>
            <span class="rc-badge badge-{s}">{lbl}</span>
        </div>
        <div class="rc-value {s}">{val}</div>
        <div class="rc-unit">{r['unit']}</div>
        <div class="rc-range">Reference: {r['reference']}</div>
        <div class="rc-bar-track">
            <div class="rc-bar-fill {s}" style="width:{r['bar_pct']}%;"></div>
        </div>
        <div class="rc-explanation">{r['explanation']}</div>
    </div>
    """, unsafe_allow_html=True)


def _render_cards(results: list):
    if not results:
        st.markdown(
            "<p style='color:var(--text-light);font-size:0.83rem;padding:0.8rem 0;'>"
            "No parameters in this category.</p>",
            unsafe_allow_html=True,
        )
        return
    pairs = [results[i:i+2] for i in range(0, len(results), 2)]
    for pair in pairs:
        cols = st.columns(len(pair))
        for col, r in zip(cols, pair):
            with col:
                _render_single_card(r)


def render_result_dashboard():
    show      = st.session_state.get("show_results",    False)
    analyzing = st.session_state.get("analyze_clicked", False)

    # Placeholder
    if not show:
        st.markdown("""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;
                    min-height:380px;border:2px dashed var(--border-mid);border-radius:var(--radius-xl);
                    background:var(--bg-white);text-align:center;padding:2.5rem 1.5rem;
                    box-shadow:var(--shadow-sm);">
            <div style="font-size:3rem;margin-bottom:1.2rem;opacity:0.3;">🧪</div>
            <p style="color:var(--text-muted);font-size:0.92rem;max-width:280px;line-height:1.7;margin:0;">
                Your interpreted results will appear here after analysis.<br/><br/>
                Upload a report and click
                <strong style="color:var(--blue-700);">Analyze Report</strong>.
            </p>
            <div style="display:flex;gap:0.7rem;margin-top:1.5rem;">
                <div style="width:9px;height:9px;border-radius:50%;background:var(--green);opacity:0.5;"></div>
                <div style="width:9px;height:9px;border-radius:50%;background:var(--yellow);opacity:0.5;"></div>
                <div style="width:9px;height:9px;border-radius:50%;background:var(--red);opacity:0.5;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Loading
    if analyzing:
        with st.spinner("Extracting values · Checking ranges · Generating insights..."):
            time.sleep(2)
        st.session_state["analyze_clicked"] = False

    counts = {"green": 0, "yellow": 0, "red": 0}
    for r in MOCK_RESULTS:
        counts[r["status"]] += 1

    st.markdown('<div class="section-label">📊 Analysis Results</div>', unsafe_allow_html=True)

    # Stats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="stat-chip green">
            <span class="stat-chip-num">{counts['green']}</span>
            <span class="stat-chip-lbl">✅ Normal</span>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-chip yellow">
            <span class="stat-chip-num">{counts['yellow']}</span>
            <span class="stat-chip-lbl">⚠️ Borderline</span>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-chip red">
            <span class="stat-chip-num">{counts['red']}</span>
            <span class="stat-chip-lbl">🚨 Abnormal</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    # Tabs
    tabs = st.tabs(["🔬 All", "🚨 Abnormal", "⚠️ Borderline", "✅ Normal"])
    with tabs[0]: _render_cards(MOCK_RESULTS)
    with tabs[1]: _render_cards([r for r in MOCK_RESULTS if r["status"] == "red"])
    with tabs[2]: _render_cards([r for r in MOCK_RESULTS if r["status"] == "yellow"])
    with tabs[3]: _render_cards([r for r in MOCK_RESULTS if r["status"] == "green"])

    # Summary
    st.markdown(f"""
    <div class="summary-panel">
        <div class="summary-title">🤖 AI Summary</div>
        <div class="summary-text">{MOCK_SUMMARY}</div>
    </div>
    """, unsafe_allow_html=True)

    # Next Steps
    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">📋 Recommended Next Steps</div>', unsafe_allow_html=True)

    for step in MOCK_NEXT_STEPS:
        st.markdown(f"""
        <div class="next-step-item">
            <span style="font-size:1rem;flex-shrink:0;margin-top:2px;">{step['icon']}</span>
            <div>
                <span class="step-tag tag-{step['tag']}">{step['tag'].upper()}</span>
                <div class="step-text">{step['text']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Download
    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
    st.download_button(
        label="⬇️ Download Report Summary",
        data=(
            "Diagnova — Report Summary\n\n"
            + MOCK_SUMMARY + "\n\nNext Steps:\n"
            + "\n".join(f"[{s['tag'].upper()}] {s['text']}" for s in MOCK_NEXT_STEPS)
        ),
        file_name="diagnova_summary.txt",
        mime="text/plain",
        use_container_width=True,
    )
