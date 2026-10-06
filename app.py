import streamlit as st
from evaluator import evaluate_idea
st.set_page_config(
    page_title="AI Project Evaluator",
    page_icon="🤖",
    layout="wide"
)
# CSS Styling
st.markdown("""
<style>
/* Background */
.stApp {
background: linear-gradient(135deg, #E3F2FD, #F3E5F5);
}
/* Main Title */
.main-title {
text-align: center;
font-size: 50px;
font-weight: bold;
color: #1565C0;
margin-bottom: 10px;
}
/* Subtitle */
.sub-title {
text-align: center;
font-size: 22px;
color: #6A1B9A;
margin-bottom: 30px;
}
/* Text Area */
textarea {
background-color: white !important;
color: black !important;
border-radius: 15px !important;
border: 2px solid #90CAF9 !important;
}
/* Button */
.stButton button {
background: #7E57C2 !important;
color: white !important;
border-radius: 12px !important;
height: 50px !important;
width: 100% !important;
font-size: 18px !important;
font-weight: bold !important;
}
/* Result Box */
.result-box {
background: white;
padding: 20px;
border-radius: 15px;
color: black;
box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}
* Label text */
label {
color: black !important;
font-weight: bold !important;
}
/* Placeholder text */
textarea::placeholder {
color: black !important;
opacity: 1 !important;
}
[data-testid="stTextArea"] textarea {
color: black !important;
background-color: white !important;
}
[data-testid="stTextArea"] textarea::placeholder {
color: black !important;
opacity: 1 !important;
}
</style>
""", unsafe_allow_html=True)
# Title
st.markdown(
    '<div class="main-title">🤖 AI Project Evaluator</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">Intelligent Feasibility and Innovation Assessment System</div>',
    unsafe_allow_html=True
)
# Input Heading
st.markdown(
    "<h3 style='color:black;'>Enter Your Project Idea</h3>",
    unsafe_allow_html=True
)
idea = st.text_area(
    "",
    height=200,
    placeholder="Example: AI Based Smart Attendance System using Face Recognition"
)
# Button
if st.button("Evaluate Project"):
    if idea.strip() == "":
        st.warning("Please enter a project idea.")
    else:
        with st.spinner("Analyzing Project Idea..."):
            result = evaluate_idea(idea)
            st.success("Analysis Completed ✅")
            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )
# Footer
st.markdown(
    """
    <hr>
    <center>
    Developed by Prakash | AI Project Evaluator
    </center>
    """,
    unsafe_allow_html=True
)