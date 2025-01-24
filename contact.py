import streamlit as st

# Function to load the resume dynamically from a URL
@st.cache_data
def get_resume_link():
    """Returns a direct download link for the resume."""
    return "https://your-resume-link-here.com/VSM_CV_2025.pdf"  # Replace with your actual hosted resume link

def contact_me():
    # Apply custom CSS for layout and styling
    st.markdown("""
    <style>
        .stApp {
            background-color: #fdfd96; /* Main theme background */
        }
        .contact-container {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            gap: 40px;
            padding: 20px;
            margin: auto;
            flex-wrap: wrap;
        }
        .left-panel {
            background: linear-gradient(135deg, #FFB74D, #FF8A65); /* Gradient background */
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            color: black;
            max-width: 400px;
            width: 100%;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
        }
        .left-panel h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
        }
        .left-panel p {
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .contact-btn {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px 5px;
            border-radius: 25px;
            text-decoration: none;
            color: #FF8A65; /* Button text color */
            background-color: white;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .contact-btn:hover {
            background-color: #FF7043; /* Darker orange on hover */
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # Layout
    st.markdown("""
    <div class="contact-container">
        <!-- Left Panel -->
        <div class="left-panel">
            <h1>Manasa Vuppu</h1>
            <p>University of North Carolina at Charlotte👩🏼‍🎓</p>
            <p>Charlotte, North Carolina 📍</p>
            <p>Email: <a href="mailto:minnuv97@gmail.com" style="color: white; text-decoration: underline;">minnuv97@gmail.com</a></p>
            <p>GitHub: <a href="https://github.com/manasavuppu" target="_blank" style="color: white; text-decoration: underline;">github.com/manasavuppu</a></p>
            <a href="{get_resume_link()}" download="Manasa_Vuppu_CV.pdf" class="contact-btn">Download CV</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Render the "Contact Me" section
contact_me()
