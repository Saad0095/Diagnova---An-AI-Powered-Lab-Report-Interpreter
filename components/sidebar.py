import streamlit as st


def render_sidebar():
    """Renders the sidebar with branding, how-it-works, risk legend, and supported reports."""

    with st.sidebar:

        # Branding
        st.markdown("""
        <div style="text-align:center;padding:1.5rem 0 1rem 0;">
            <div style="font-size:2.5rem;margin-bottom:0.5rem;">🧬</div>
            <div style="font-size:1.3rem;font-weight:800;color:#ffffff;letter-spacing:-0.02em;">
                LabLens AI
            </div>
            <div style="font-size:0.68rem;color:rgba(255,255,255,0.5);letter-spacing:0.14em;
                        text-transform:uppercase;margin-top:5px;">
                Medical Report Interpreter
            </div>
        </div>
        <hr style="border-color:rgba(255,255,255,0.12);margin:0 0 1.5rem 0;"/>
        """, unsafe_allow_html=True)

        # How It Works
        st.markdown("""
        <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.14em;
                  text-transform:uppercase;color:rgba(255,255,255,0.5);margin-bottom:1rem;">
            ⚙️ How It Works
        </p>
        """, unsafe_allow_html=True)

        steps = [
            ("01", "Upload",  "Upload your PDF or image lab report"),
            ("02", "Extract", "AI reads and extracts key clinical values"),
            ("03", "Analyze", "Values checked against reference ranges"),
            ("04", "Explain", "Results explained in plain language"),
            ("05", "Act",     "Color-coded risk levels and next steps"),
        ]

        for num, title, desc in steps:
            st.markdown(f"""
            <div style="display:flex;gap:0.8rem;margin-bottom:0.9rem;align-items:flex-start;">
                <div style="min-width:26px;height:26px;border-radius:50%;
                            background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.2);
                            display:flex;align-items:center;justify-content:center;
                            font-size:0.58rem;font-weight:700;color:#7efff5;
                            font-family:'JetBrains Mono',monospace;flex-shrink:0;">
                    {num}
                </div>
                <div>
                    <div style="font-size:0.8rem;font-weight:700;color:#ffffff;margin-bottom:2px;">
                        {title}
                    </div>
                    <div style="font-size:0.72rem;color:rgba(255,255,255,0.55);line-height:1.5;">
                        {desc}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr style="border-color:rgba(255,255,255,0.12);margin:0.5rem 0 1.2rem 0;"/>', unsafe_allow_html=True)

        # Risk Legend
        st.markdown("""
        <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.14em;
                  text-transform:uppercase;color:rgba(255,255,255,0.5);margin-bottom:1rem;">
            🎨 Risk Legend
        </p>
        """, unsafe_allow_html=True)

        legend = [
            ("#00a67e", "rgba(0,166,126,0.15)",  "rgba(0,166,126,0.4)",  "✅ Normal",     "Value within reference range."),
            ("#c97800", "rgba(201,120,0,0.15)",   "rgba(201,120,0,0.4)",  "⚠️ Borderline", "Slightly outside range. Monitor."),
            ("#d93025", "rgba(217,48,37,0.15)",   "rgba(217,48,37,0.4)",  "🚨 Abnormal",   "Significantly out of range."),
        ]

        for color, bg, border, label, desc in legend:
            st.markdown(f"""
            <div style="display:flex;align-items:flex-start;gap:0.75rem;margin-bottom:0.7rem;
                        background:{bg};border:1px solid {border};border-radius:10px;padding:0.65rem 0.8rem;">
                <div style="width:9px;height:9px;border-radius:50%;background:{color};
                            margin-top:3px;flex-shrink:0;"></div>
                <div>
                    <div style="font-size:0.78rem;font-weight:700;color:{color};">{label}</div>
                    <div style="font-size:0.7rem;color:rgba(255,255,255,0.55);line-height:1.4;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr style="border-color:rgba(255,255,255,0.12);margin:0.5rem 0 1.2rem 0;"/>', unsafe_allow_html=True)

        # Supported Reports
        st.markdown("""
        <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.14em;
                  text-transform:uppercase;color:rgba(255,255,255,0.5);margin-bottom:0.8rem;">
            📋 Supported Reports
        </p>
        """, unsafe_allow_html=True)

        reports = [
            "🩸 CBC (Complete Blood Count)",
            "🧪 Metabolic Panel",
            "💛 Liver Function (LFT)",
            "🫘 Kidney Function (KFT)",
            "🍬 Diabetes Panel",
            "🦋 Thyroid (TFT)",
            "💊 Lipid Profile",
            "🔎 Urinalysis",
        ]

        for r in reports:
            st.markdown(f"""
            <div style="font-size:0.78rem;color:rgba(255,255,255,0.65);padding:0.35rem 0;
                        border-bottom:1px solid rgba(255,255,255,0.07);">
                {r}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr style="border-color:rgba(255,255,255,0.12);margin:1rem 0 0.8rem 0;"/>', unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div style="text-align:center;padding:0.5rem 0 0.5rem 0;">
            <div style="font-size:0.68rem;color:rgba(255,255,255,0.35);line-height:1.9;">
                Built for <span style="color:#7efff5;font-weight:600;">Hackathon 2025</span><br/>
                Not a substitute for medical advice<br/>
                <span style="font-size:0.62rem;opacity:0.6;">v1.0.0 · LabLens AI</span>
            </div>
        </div>
        """, unsafe_allow_html=True)