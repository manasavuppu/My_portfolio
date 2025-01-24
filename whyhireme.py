import streamlit as st

def show_cv():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .stApp {
            background-color: #fdfd96; /* Matches the main theme */
        }
        .hero-header {
            font-size: 3em;
            text-align: center;
            margin-bottom: 20px;
            color: #023047; /* Dark blue */
            font-weight: bold;
        }
        .section-description {
            text-align: center;
            font-size: 1.2em;
            color: #000000;
            margin-bottom: 40px;
        }
        .download-btn {
            display: inline-block;
            padding: 12px 24px;
            background-color: white; /* Button color updated to white */
            color: #023047; /* Text color is dark blue */
            border: 2px solid #023047; /* Add a border */
            border-radius: 8px;
            text-decoration: none;
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth zoom effect */
        }
        .download-btn:hover {
            transform: scale(1.1); /* Zoom in slightly */
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.3); /* Add shadow for emphasis */
        }
        .card-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* 3 columns per row */
            gap: 20px; /* Add spacing between cards */
            padding: 20px;
        }
        .card {
            background-color: #ffe078; /* Light yellow */
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
        }
        .card:hover {
            transform: translateY(-10px); /* Lift the card */
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2); /* Enhanced shadow on hover */
        }
        .card-icon {
            font-size: 50px;
            margin-bottom: 15px;
            color: #fb8500; /* Orange */
        }
        .card-title {
            font-size: 1.5em;
            color: #023047; /* Dark blue */
            font-weight: bold;
            margin-bottom: 10px;
        }
        .card-description {
            font-size: 1em;
            color: #333333;
            line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section with Updated Button Style
    st.markdown("<div class='hero-header'>Why Hire Me? 🚀</div>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <a href="path/to/your-cv.pdf" download="Manasa_Vuppu_CV.pdf" class="download-btn">Download CV</a>
        </div>
    """, unsafe_allow_html=True)


    # Description Section
    st.markdown("<div class='section-description'> As George Box once said, 'All models are wrong, but some are useful.' I aim to build those useful ones, combining mindfulness, wisdom, and knowledge to transform data into meaningful insights and impactful decisions. </div>", unsafe_allow_html=True)

    # Cards Section
    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    # Define card data
    cards = [
        {"icon": "✏️", "title": "Collect", "description": "Adept in data collection qualitatively and quantitatively using tools like Qualtrics for impact assessment."},
        {"icon": "⚙️", "title": "Process", "description": "Skilled in data transformation, explorartory data analysis and predictive analytics to generate actionable insights."},
        {"icon": "📊", "title": "Visualize", "description": "Creating impactful dashboards with tools like Tableau, Excel and Matplotlib."},
        {"icon": "🤖", "title": "Machine Learning", "description": "Proficient in building supervised, un-supervised, deep learning models to uncover patterns and make accurate predictions."},
        {"icon": "📈", "title": "Data Analytics", "description": "Expertise in analyzing and interpreting large datasets to extract actionable insights."},
        {"icon": "🧠", "title": "Generative AI", "description": "Passionate on exploring advancements with hands-on experience with generative AI models for creative problem-solving."},
        {"icon": "🧩", "title": "Problem Solver", "description": "Adept at identifying areas that need attention; breaking down complex challenges to deliver scalable solutions."},
        {"icon": "🎯", "title": "Ambitious & Target-Oriented", "description": "Driven by results, ensuring projects are completed with precision with a You vs You mindset."},
        {"icon": "🤝", "title": "Honest & Hardworking", "description": "Known for integrity, diligence, and commitment to professional excellence with personal evolution."}
    ]

    # Generate cards dynamically
    for card in cards:
        st.markdown(f"""
            <div class="card">
                <div class="card-icon">{card['icon']}</div>
                <div class="card-title">{card['title']}</div>
                <div class="card-description">{card['description']}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Call the function to render the section
show_cv()
