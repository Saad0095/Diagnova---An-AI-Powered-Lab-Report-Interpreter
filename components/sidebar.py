import streamlit as st


def render_sidebar():
    """Renders app info as a top expander — works on all platforms including HuggingFace."""

    with st.expander("ℹ️ About Diagnova · How It Works · Risk Legend", expanded=False):

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div style="padding:0.5rem 0;">
                <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;
                          text-transform:uppercase;color:var(--blue-700);margin-bottom:0.8rem;">
                    ⚙️ How It Works
                </p>
            """, unsafe_allow_html=True)

            steps = [
                ("01", "Upload",  "Upload your PDF or image lab report"),
                ("02", "Extract", "AI reads and extracts clinical values"),
                ("03", "Analyze", "Values checked against reference ranges"),
                ("04", "Explain", "Results explained in plain language"),
                ("05", "Act",     "Color-coded risk levels and next steps"),
            ]
            for num, title, desc in steps:
                st.markdown(f"""
                <div style="display:flex;gap:0.6rem;margin-bottom:0.7rem;align-items:flex-start;">
                    <div style="min-width:22px;height:22px;border-radius:50%;
                                background:var(--blue-700);
                                display:flex;align-items:center;justify-content:center;
                                font-size:0.55rem;font-weight:700;color:#fff;
                                font-family:'JetBrains Mono',monospace;flex-shrink:0;">
                        {num}
                    </div>
                    <div>
                        <div style="font-size:0.78rem;font-weight:700;color:var(--text-dark);margin-bottom:1px;">{title}</div>
                        <div style="font-size:0.7rem;color:var(--text-muted);line-height:1.4;">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="padding:0.5rem 0;">
                <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;
                          text-transform:uppercase;color:var(--blue-700);margin-bottom:0.8rem;">
                    🎨 Risk Legend
                </p>
            """, unsafe_allow_html=True)

            legend = [
                ("var(--green)",  "var(--green-light)",  "var(--green-border)",  "✅ Normal",     "Value within reference range. No action needed."),
                ("var(--yellow)", "var(--yellow-light)", "var(--yellow-border)", "⚠️ Borderline", "Slightly outside range. Monitor and consult."),
                ("var(--red)",    "var(--red-light)",    "var(--red-border)",    "🚨 Abnormal",   "Significantly out of range. See a physician."),
            ]
            for color, bg, border, label, desc in legend:
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:0.6rem;margin-bottom:0.6rem;
                            background:{bg};border:1px solid {border};border-radius:8px;padding:0.6rem 0.8rem;">
                    <div style="width:8px;height:8px;border-radius:50%;background:{color};
                                margin-top:3px;flex-shrink:0;"></div>
                    <div>
                        <div style="font-size:0.76rem;font-weight:700;color:{color};">{label}</div>
                        <div style="font-size:0.7rem;color:var(--text-muted);line-height:1.4;">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div style="padding:0.5rem 0;">
                <p style="font-size:0.68rem;font-weight:700;letter-spacing:0.12em;
                          text-transform:uppercase;color:var(--blue-700);margin-bottom:0.8rem;">
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
                <div style="font-size:0.76rem;color:var(--text-body);padding:0.3rem 0;
                            border-bottom:1px solid var(--border);">
                    {r}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <div style="margin-top:1rem;padding:0.7rem;background:var(--blue-50);
                        border-radius:var(--radius-sm);border:1px solid var(--border);">
                <p style="font-size:0.7rem;color:var(--text-muted);margin:0;line-height:1.5;">
                    Built for <strong style="color:var(--blue-700);">Hackathon 2025</strong><br/>
                    Not a substitute for medical advice.
                </p>
            </div>
            </div>
            """, unsafe_allow_html=True)
