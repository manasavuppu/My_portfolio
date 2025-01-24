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
        .nav-bar {
            display: flex;
            justify-content: center;
            gap: 15px; /* Spacing between items */
            margin-top: 20px;
        }
        .nav-bar-item {
            padding: 10px 20px;
            background-color: #ffe078;
            color: #101010 !important; /* Ensure button text stays black */
            border: 2px solid #023047;
            border-radius: 5px;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
        }
        .nav-bar-item:hover {
            background-color: #fb8500; /* Hover color */
            color: white; /* Hover text color */
        }
        .nav-bar-item:active {
            background-color: #023047; /* Active state */
            color: white; /* Active text color */
        }
        /* Mobile-specific fixes */
        @media (max-width: 768px) {
            .nav-bar-item {
                background-color: #ffe078 !important;
                color: #101010 !important;
            }
            .nav-bar-item:hover {
                background-color: #fb8500 !important;
                color: white !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Initialize tab state
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "About Me"

# Sidebar toggle
show_sidebar = st.checkbox("Show Sidebar", value=True)

if show_sidebar:
    with st.sidebar:
        tabs = st.radio(
            "Navigate to:",
            ["About Me", "Portfolio", "Interests", "Why hire me", "Contact"],
            index=["About Me", "Portfolio", "Interests", "Why hire me", "Contact"].index(st.session_state.active_tab)
        )
        st.session_state.active_tab = tabs  # Update session state
else:
    # Horizontal navigation bar with buttons
    st.markdown("<div class='nav-bar'>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("About Me"):
            st.session_state.active_tab = "About Me"
    with col2:
        if st.button("Portfolio"):
            st.session_state.active_tab = "Portfolio"
    with col3:
        if st.button("Interests"):
            st.session_state.active_tab = "Interests"
    with col4:
        if st.button("Why hire me"):
            st.session_state.active_tab = "Why hire me"
    with col5:
        if st.button("Contact"):
            st.session_state.active_tab = "Contact"

    st.markdown("</div>", unsafe_allow_html=True)

# Tabs logic
tabs = st.session_state.active_tab

if tabs == "About Me":
    st.markdown("<h1>About Me</h1>", unsafe_allow_html=True)
    st.write("Welcome to the About Me section!")

elif tabs == "Portfolio":
    st.markdown("<h1>Portfolio</h1>", unsafe_allow_html=True)
    show_portfolio()

elif tabs == "Interests":
    st.markdown("<h1>Interests</h1>", unsafe_allow_html=True)
    show_interests()

elif tabs == "Why hire me":
    st.markdown("<h1>Why Hire Me?</h1>", unsafe_allow_html=True)
    show_cv()

elif tabs == "Contact":
    st.markdown("<h1>Contact Me</h1>", unsafe_allow_html=True)
    contact_me()
