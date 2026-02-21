import streamlit as st


def render_upload_section():
    """Renders the file upload and text input section."""

    st.markdown('<div class="section-label">📂 Input Report</div>', unsafe_allow_html=True)

    # ── Input mode toggle ──────────────────────────────────────────────────────
    input_mode = st.radio(
        "Input method",
        ["📄 Upload File", "✏️ Paste Text"],
        horizontal=True,
        label_visibility="collapsed",
    )

    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

    # ── Upload mode ────────────────────────────────────────────────────────────
    if input_mode == "📄 Upload File":
        st.markdown("""
        <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.5rem;">
            Supported formats:&nbsp;
            <code style="background:var(--blue-50);color:var(--blue-700);
                padding:2px 8px;border-radius:5px;border:1px solid var(--border);
                font-size:0.75rem;">PDF</code>&nbsp;
            <code style="background:var(--blue-50);color:var(--blue-700);
                padding:2px 8px;border-radius:5px;border:1px solid var(--border);
                font-size:0.75rem;">PNG</code>&nbsp;
            <code style="background:var(--blue-50);color:var(--blue-700);
                padding:2px 8px;border-radius:5px;border:1px solid var(--border);
                font-size:0.75rem;">JPG</code>
        </p>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "lab_report",
            type=["pdf", "png", "jpg", "jpeg"],
            label_visibility="collapsed",
        )

        if uploaded_file:
            st.session_state["uploaded_file"] = uploaded_file
            st.session_state["input_ready"]   = True
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;margin-top:0.8rem;
                        background:var(--green-light);border:1.5px solid var(--green-border);
                        border-radius:var(--radius-md);padding:0.75rem 1rem;">
                <span>✅</span>
                <span style="font-size:0.84rem;color:var(--green);font-weight:600;">
                    {uploaded_file.name} — ready to analyze
                </span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.session_state["input_ready"] = False

    # ── Paste mode ─────────────────────────────────────────────────────────────
    else:
        pasted_text = st.text_area(
            "Paste lab report text",
            height=200,
            placeholder=(
                "Paste your lab values here, e.g.\n\n"
                "Hemoglobin: 11.2 g/dL\n"
                "WBC Count: 9,800 /μL\n"
                "Platelets: 145,000 /μL\n"
                "Fasting Glucose: 108 mg/dL"
            ),
            label_visibility="collapsed",
        )
        if pasted_text.strip():
            st.session_state["pasted_text"] = pasted_text
            st.session_state["input_ready"] = True
        else:
            st.session_state["input_ready"] = False

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

    # ── Report Type ────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">🔬 Report Type</div>', unsafe_allow_html=True)

    report_type = st.selectbox(
        "Report type",
        [
            "🩸 Complete Blood Count (CBC)",
            "🧪 Comprehensive Metabolic Panel",
            "💛 Liver Function Test (LFT)",
            "🫘 Kidney Function Test (KFT)",
            "🍬 Diabetes Panel (HbA1c / Glucose)",
            "🦋 Thyroid Function Test (TFT)",
            "💊 Lipid Profile",
            "🔎 Urinalysis",
            "📋 General / Mixed Report",
        ],
        label_visibility="collapsed",
    )
    st.session_state["report_type"] = report_type

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ── Analyze Button ─────────────────────────────────────────────────────────
    if st.button("🔍 Analyze Report", use_container_width=True):
        if st.session_state.get("input_ready"):
            st.session_state["analyze_clicked"] = True
            st.session_state["show_results"]    = True
        else:
            st.warning("⚠️ Please upload a file or paste report text first.")

    # ── Tips ───────────────────────────────────────────────────────────────────
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:1.1rem 1.2rem;background:var(--blue-50);
                border:1px solid var(--border);border-radius:var(--radius-md);">
        <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;
                  text-transform:uppercase;color:var(--blue-700);margin:0 0 0.7rem 0;">
            💡 Tips for best results
        </p>
        <ul style="margin:0;padding-left:1.1rem;">
            <li style="font-size:0.8rem;color:var(--text-body);margin-bottom:0.35rem;line-height:1.5;">
                Ensure the report is clear and legible
            </li>
            <li style="font-size:0.8rem;color:var(--text-body);margin-bottom:0.35rem;line-height:1.5;">
                Select the correct report type above
            </li>
            <li style="font-size:0.8rem;color:var(--text-body);line-height:1.5;">
                PDF format gives the most accurate text extraction
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)