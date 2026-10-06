import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Guidance",
    page_icon="🎯",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #eef2ff, #f8fafc);
    }

    /* Main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    /* Header */
    .header {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 35px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.25);
    }

    .header h1 {
        font-size: 42px;
        margin-bottom: 8px;
        font-weight: 700;
    }

    .header p {
        font-size: 18px;
        margin: 0;
        opacity: 0.9;
    }

    /* Search card */
    .search-card {
        background: white;
        padding: 28px;
        border-radius: 18px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .section-title {
        color: #3730a3;
        font-size: 24px;
        font-weight: 650;
        margin-bottom: 10px;
    }

    /* Input box */
    .stTextInput > div > div > input {
        border: 2px solid #c7d2fe;
        border-radius: 12px;
        padding: 12px;
        font-size: 16px;
    }

    .stTextInput > div > div > input:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 2px rgba(99,102,241,0.15);
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 20px;
        font-size: 17px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 18px rgba(79,70,229,0.3);
    }

    /* Result card */
    .result-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin-top: 25px;
    }

    /* Info cards */
    .info-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        margin-top: 20px;
    }

    .info-card h3 {
        color: #4f46e5;
        margin-bottom: 8px;
    }

    .info-card p {
        color: #64748b;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 40px;
        padding: 15px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("""
<div class="header">
    <h1>🎯 AI Career Guidance</h1>
    <p>Discover career opportunities based on your interests and skills</p>
</div>
""", unsafe_allow_html=True)


# ---------------- LOAD DATA ----------------

try:
    df = pd.read_csv("data/careers.csv")
except FileNotFoundError:
    st.error("❌ careers.csv file not found. Please check the data folder.")
    st.stop()


# ---------------- SEARCH SECTION ----------------

st.markdown("""
<div class="search-card">
    <div class="section-title">🔍 Find Your Career</div>
    <p>Enter a skill, interest, or career area to discover suitable options.</p>
</div>
""", unsafe_allow_html=True)


interest = st.text_input(
    "💡 Enter your interest or skill",
    placeholder="Example: Python, AI, Electronics, Data Science..."
)


# ---------------- SEARCH BUTTON ----------------

if st.button("🚀 Find Careers"):

    if interest.strip():

        results = df[
            df.astype(str).apply(
                lambda row: row.str.contains(
                    interest,
                    case=False,
                    na=False,
                    regex=False
                ).any(),
                axis=1
            )
        ]

        if not results.empty:

            st.success("🎉 Great! We found some career options for you.")

            st.markdown("""
            <div class="result-card">
                <div class="section-title">🌟 Recommended Career Options</div>
            </div>
            """, unsafe_allow_html=True)

            st.dataframe(
                results,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "😕 No matching careers found. Try another skill or interest."
            )

    else:

        st.warning(
            "⚠️ Please enter an interest or skill first."
        )


# ---------------- INFORMATION CARDS ----------------

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>💡 Explore</h3>
        <p>Explore different career paths based on your interests.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Discover</h3>
        <p>Find career options that match your skills.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🚀 Grow</h3>
        <p>Choose a career path and build your future.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    🤖 AI Career Guidance Assistant | Helping you discover your career path
</div>
""", unsafe_allow_html=True)