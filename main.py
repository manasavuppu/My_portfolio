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

# Apply custom CSS for collapsibility and responsive design
st.markdown("""
    <style>
        /* Background color for the app */
        .stApp {
            background-color: #fdfd96; /* Brighter yellow */
        }
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #ffe078; /* Light yellow background */
            padding: 20px; /* Add padding for spacing */
        }
        /* Sidebar collapsibility on mobile screens */
        @media (max-width: 768px) {
            section[data-testid="stSidebar"] {
                display: none; /* Hide sidebar on small screens */
            }
        }
        /* Header styling */
        .header-main {
            color: #101010; /* Black for Hello there! */
            font-size: 50px;
            font-weight: bold;
            text-align: center;
        }
        .header-name {
            color: #808000; /* Olive for name */
            font-size: 50px;
            font-weight: bold;
            text-align: center;
        }
        .dynamic-keyword {
            color: #fb8500; /* Orange for animated keywords */
            font-style: italic;
            font-size: 36px;
            text-align: center;
            font-weight: bold;
        }
        /* About Me Text Styling */
        .about-me-text {
            text-align: justify;
            font-size: 20px;
            color: #101010;
            line-height: 1.8;
        }
    </style>
""", unsafe_allow_html=True)

# Cache functions to optimize image loading
@st.cache_data
def load_image(image_path):
    """Load and return an image using Pillow."""
    return Image.open(image_path)

@st.cache_data
def get_keywords():
    """Return a list of animated keywords."""
    return [
        "Machine Learning", 
        "Artificial Intelligence",
        "Data Visualization", 
        "Business Intelligence", 
        "Deep Learning",
        "Generative AI"
    ]

# Load images
profile_image = load_image("me.jpeg")

# Collapsible Sidebar for Desktop
show_sidebar = st.checkbox("Show Sidebar", value=True)

if show_sidebar:
    with st.sidebar:
        st.markdown("""
            <style>
                .sidebar-title {
                    font-size: 26px; /* Increase font size */
                    font-weight: bold; /* Make it bold */
                    color: #023047; /* Set dark blue color */
                    text-align: left; /* Left align the text */
                    margin-bottom: 20px; /* Add spacing below */
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
    # If sidebar is hidden, use dropdown for navigation
    tabs = st.selectbox(
        "Navigate to:",
        ["About Me", "Portfolio", "Interests", "Why hire me", "Contact"]
    )

# Tabs Logic
if tabs == "About Me":
    st.markdown("<h1 class='header-main'>Hello there! 👋🏽</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='header-name'>Welcome to Manasa's Portfolio</h1>", unsafe_allow_html=True)

    # Dynamic Animation for Keywords
    keywords = get_keywords()
    placeholder = st.empty()
    colors = ["#666600", "#273e06", "#666600", "#273e06", "#666600", "#273e06"]

    for _ in range(3):
        for word, color in zip(keywords, colors):
            placeholder.markdown(
                f"<h2 class='dynamic-keyword' style='color: {color};'>{word}</h2>",
                unsafe_allow_html=True
            )
            time.sleep(1)

    # Add vertical space
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

    # About Me Text
    st.markdown("""
        <div style="text-align: justify; font-size: 16px; color: #101010; line-height: 1.8; padding: 0; margin: 0;">
        
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

    # Add images
    st.image(profile_image, caption="You know me now! 🤠 -minn", width=600)

elif tabs == "Portfolio":
    show_portfolio()

elif tabs == "Interests":
    show_interests()

elif tabs == "Why hire me":
    show_cv()

elif tabs == "Contact":
    contact_me()
