import streamlit as st

# Portfolio Tab
def show_portfolio():
    # Portfolio Header
    st.markdown("<h1 class='header-main'>My Portfolio 📂</h1>", unsafe_allow_html=True)

    # Upcoming Projects Section
    st.markdown("<h2 style='text-align: center; color: #101010;'>Upcoming Projects 🚀</h2>", unsafe_allow_html=True)

    # Define upcoming projects
    upcoming_projects = [
        {
            "title": "AI-Powered Mini-me Writing Bot",
            "description": "Building a custom NLP-AI model using personal writing data to replicate my writing style for smart content generation."
        },
    ]

    # Display upcoming projects
    for project in upcoming_projects:
        st.markdown(f"""
            <div style="margin-bottom: 20px; padding: 15px; background-color: #ffe078; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                <h3 style="color: #023047; margin-bottom: 5px; text-align: center">{project['title']}</h3>
                <p style="color: #101010; font-size: 16px; margin: 0; text-align: center;">{project['description']}</p>
            </div>
        """, unsafe_allow_html=True)

    # Completed Projects Section
    st.markdown("<h2 style='text-align: center; color: #101010;'>Completed Projects ✅</h2>", unsafe_allow_html=True)

    # Define completed projects
    projects = [
        {
            "title": "Mental Health Stress Predictor",
            "field": "Machine Learning | Exploratory Data Analysis",
            "intent": "To help users make better wellness decisions by predicting stress levels and seeking in-time help.",
            "link": "https://github.com/manasavuppu/Mental_Health_App"
        },
        {
            "title": "Data Synthesizer for Non-invasive Ultrasonic Testing",
            "field": "Data Science | Deep Learning",
            "intent": "To tackle industry scarcity of data by providing pre-trained Ultrasonic Testing Data Synthesizers.",
            "link": "https://github.com/manasavuppu/UT_synthesizer_V2"
        },
        {
            "title": "Cab-Industry-Investment-Analysis",
            "field": "Exploratory Data Analysis",
            "intent": "To suggest personalized investment planning for company X in the cab industry based on profit-revenue margins.",
            "link": "https://github.com/manasavuppu/Cab-Industry-Investment-Analysis"
        },
        {
            "title": "Rotten Tomatoes Movie Review Analysis",
            "field": "Exploratory Data Analysis | Machine Learning | Natural Language Processing",
            "intent": "To analyze customer reviews and gauge overall brand sentiment, suggesting prospect sales, brand expansion, and rating predictions.",
            "link": "https://github.com/manasavuppu/Rotten_Tomatoes_Movie_Review_Analysis"
        },
        {
            "title": "Netflix Dashboard using Tableau",
            "field": "Exploratory Data Analysis | Data Visualization",
            "intent": "To visualize audience viewing trends and make recommendations for targeted content investment.",
            "link": "https://github.com/manasavuppu/Midterm-Netflix_Dashboard"
        },
        {
            "title": "Zomato Restaurant Rating and Expansion Propensity Prediction",
            "field": "Exploratory Data Analysis | Machine Learning",
            "intent": "To predict restaurant ratings and suggest optimal locations for expansion based on demographics and cuisine trends.",
            "link": "https://github.com/manasavuppu/Zomato_Restaurant_Analysis"
        }
    ]

    # Add custom CSS for grid, spacing, and hover effects
    st.markdown("""
        <style>
            .portfolio-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 30px;
                margin-top: 20px;
            }
            .portfolio-item {
                position: relative;
                background-color: #ffe078;
                border-radius: 10px;
                text-align: center;
                padding: 20px;
                border: 2px solid #ffd54f;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .portfolio-item:hover {
                transform: translateY(-10px);
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            }
            .portfolio-item-title {
                font-size: 18px;
                font-weight: bold;
                color: #101010;
                margin-bottom: 10px;
            }
            .thinking-cloud {
                position: absolute;
                top: -50px;
                left: 50%;
                transform: translateX(-50%);
                background-color: #ffffff;
                color: #101010;
                padding: 10px;
                border-radius: 15px;
                font-size: 14px;
                line-height: 1.4;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                visibility: hidden;
                opacity: 0;
                transition: visibility 0.3s, opacity 0.3s;
            }
            .portfolio-item:hover .thinking-cloud {
                visibility: visible;
                opacity: 1;
            }
        </style>
    """, unsafe_allow_html=True)

    # Render portfolio grid
    st.markdown('<div class="portfolio-grid">', unsafe_allow_html=True)

    for project in projects:
        # HTML for each portfolio item with hover pop-up
        st.markdown(f"""
            <div class="portfolio-item">
                <a href="{project['link']}" target="_blank" style="text-decoration: none;">
                    <div class="portfolio-item-title">{project['title']}</div>
                    <div class="thinking-cloud">{project['intent']}</div>
                </a>
                <div class="portfolio-hover">{project['field']}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Run the function to display portfolio
show_portfolio()
