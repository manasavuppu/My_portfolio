import streamlit as st
from PIL import Image
import time
from portfolio import show_portfolio
from interests import show_interests
from whyhireme import show_cv
from contact import contact_me

# Configure the page
st.set_page_config(
    page_title="Manasa Vuppu - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS for styling and responsive fixes
st.markdown("""
    <style>
        .stApp {
            background-color: #fdfd96; /* Brighter yellow */
        }
        section[data-testid="stSidebar"] {
            background-color: #ffe078; /* Sidebar background color */
        }
        .sidebar-toggle {
            position: fixed;
            top: 20px;
            left: 10px;
            background-color: #fb8500;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            z-index: 1000;
        }
        .sidebar-toggle:hover {
            background-color: #023047;
        }
        .nav-bar {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }
        .nav-bar-item {
            padding: 10px 20px;
            background-color: #ffe078;
            color: #101010 !important;
            border: 2px solid #023047;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
        }
        .nav-bar-item:hover {
            background-color: #fb8500;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar toggle logic
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = True

def toggle_sidebar():
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

# Toggle button
toggle_button = st.markdown(
    f"""
    <button class="sidebar-toggle" onclick="window.location.reload();">{'→' if st.session_state.sidebar_visible else '←'}</button>
    """,
    unsafe_allow_html=True,
)

# Show sidebar conditionally
if st.session_state.sidebar_visible:
    with st.sidebar:
        st.markdown("""
            <style>
                .sidebar-title {
                    font-size: 26px; /* Increase font size */
                    font-weight: bold;
                    color: #023047;
                    text-align: left;
                    margin-bottom: 20px;
                }
            </style>
        """, unsafe_allow_html=True)
        st.markdown("<div class='sidebar-title'>Know me Better Today! 🙌🏽</div>", unsafe_allow_html=True)
        tabs = st.radio(
            "Navigate to:",
            ["About Me", "Portfolio", "Interests", "Why hire me", "Contact"],
            index=0
        )
else:
    # Horizontal navigation bar
    st.markdown("<div class='nav-bar'>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    if col1.button("About Me"):
        tabs = "About Me"
    elif col2.button("Portfolio"):
        tabs = "Portfolio"
    elif col3.button("Interests"):
        tabs = "Interests"
    elif col4.button("Why hire me"):
        tabs = "Why hire me"
    elif col5.button("Contact"):
        tabs = "Contact"
    else:
        tabs = "About Me"  # Default

# Tabs logic
if tabs == "About Me":
    st.markdown("<h1 style='text-align: center;'>Hello there! 👋🏽</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>Welcome to Manasa's Portfolio</h1>", unsafe_allow_html=True)

    # Dynamic Animation for Keywords
    keywords = ["Machine Learning", "Artificial Intelligence", "Data Visualization", "Business Intelligence", "Deep Learning", "Generative AI"]
    placeholder = st.empty()
    colors = ["#666600", "#273e06", "#666600", "#273e06", "#666600", "#273e06"]

    for _ in range(3):
        for word, color in zip(keywords, colors):
            placeholder.markdown(
                f"<h2 style='color: {color}; text-align: center;'>{word}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(1)

    st.markdown("""
        <div style="text-align: justify; font-size: 16px; color: #101010; line-height: 1.8; margin-top: 20px;">
        I am Manasa, but you can call me Minn—or perhaps, a Data Scientist!  
        My mission is to transform raw data into actionable insights that drive success and innovation for businesses.

        With a strong foundation in Computer Science Engineering, Marketing, and Entrepreneurship, I thrive on embracing calculated risks and finding innovative solutions.

        The elegance of mathematics captivates me, empowering my strengths in statistical analysis and data-driven decision-making. 
        I am a creative thinker with a deep curiosity for understanding consumer behavior, coupled with a passion for growing in the technical domain.

        Leveraging the power of open-source AI tools and Python, I create impactful solutions that address real-world challenges and contribute to the community. 
        My aspirations lie in gaining hands-on experience through industrial projects that challenge me, inspire me, and encourage me to grow continuously.

        Every day, I immerse myself in the exciting worlds of machine learning, deep learning, and business intelligence. 
        Staying updated on industry breakthroughs while honing my skills is my way of preparing for a better tomorrow.

        This is just a glimpse of who I am—there’s so much more to share! I’d love to connect and learn about you too. 
        Perhaps we can catch up over a virtual coffee on Zoom sometime? ☕️

        Take your time exploring my portfolio, and thank you for visiting!  
        </div>
    """, unsafe_allow_html=True)
    st.image("me.jpeg", caption="You know me now! 🤠 -minn", width=600)

elif tabs == "Portfolio":
    show_portfolio()

elif tabs == "Interests":
    show_interests()

elif tabs == "Why hire me":
    show_cv()

elif tabs == "Contact":
    contact_me()
