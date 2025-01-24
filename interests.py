import streamlit as st

def show_interests():
    # Apply custom CSS for layout and styling
    st.markdown("""
        <style>
            /* General Header Styling */
            .header-main {
                font-size: 50px;
                font-weight: bold;
                color: #101010; /* Black text */
                text-align: center;
                margin-bottom: 30px;
            }
            /* Sub-header Styling */
            .sub-header {
                color: #023047; /* Dark blue text */
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 15px;
            }
            /* Paragraph Styling */
            .paragraph {
                font-size: 18px;
                color: #023047;
                line-height: 1.8;
                text-align: justify;
            }
            /* Blog Card */
            .blog-item {
                background-color: #fdfd96; /* Light yellow */
                border-radius: 10px;
                text-align: center;
                padding: 20px;
                border: 2px solid #ffd54f;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                cursor: pointer;
                margin: 10px 0;
            }
            .blog-item:hover {
                transform: translateY(-5px);
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            }
            .blog-title {
                font-size: 24px;
                font-weight: bold;
                color: #273e06; /* olive text */
                margin: 0;
            }
            /* Topics Styling */
            .topics-container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 15px; /* Spacing between topics */
                margin: 20px 0;
            }
            .topic {
                background-color: #ffe078; /* Light yellow */
                color: #023047; /* Dark blue */
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .topic:hover {
                transform: translateY(-5px);
                box-shadow: 0px 6px 15px rgba(255, 136, 0, 0.3); /* Orange shadow on hover */
            }
            /* Expander Styling */
            .expander-header {
                font-size: 2px;
                font-weight: bold;
                color: #273e06; /* Dark blue */
                background-color: #fdfd96; /* Light yellow */
                border-radius: 10px;
                padding: 15px;
                border: 2px solid #ffd54f;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                cursor: pointer;
            }
            .expander-content {
                font-size: 20px;
                line-height: 1.6;
                color: #333333; /* Dark grey */
                margin-top: 10px;
                text-align: justify;
                padding: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Topics Section
    st.markdown("<h2 class='header-main'>Topics Interested In 🌟</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="topics-container">
            <div class="topic">Data Modelling</div>
            <div class="topic">Machine Learning</div>
            <div class="topic">Generative AI</div>
            <div class="topic">Data Visualisation</div>
            <div class="topic">Business Intelligence</div>
            <div class="topic">Deep Learning</div>
            <div class="topic">Large Language Models</div>
            <div class="topic">Cloud for AI/ML</div>
            <div class="topic">RAG | LangChains</div>
        </div>
    """, unsafe_allow_html=True)

    # Blog Cards Section
    st.markdown("<h2 class='header-main'>Read my Mind ✍🏼</h2>", unsafe_allow_html=True)

    # Collapsible Expander Section
    blog_posts = {
        "Why Data Science?": """
        I’ve always wanted to bring my ideas to life in a way that was both creative and technical. Being tech-savvy, I knew I had the potential to do so, but I needed the right direction and training to refine my abilities. So, I made the bold choice to continue sharpening my technical skills. My background in technology and computers provided me with a strong foundation to dive into artificial intelligence—a field I have long been eager to explore.
        As a former marketer, I learned to observe consumers, understand patterns, and interpret behavior. I developed a knack for identifying how external and internal factors influence thinking, how interests shape thoughts, and how subtle shifts can bring about significant changes. Now, as a data scientist, I get to test hypotheses, apply these observations, and ground them in facts. I bring actionable analytics to the table, equipping organizations with the tools to stay on the path of optimization.
        I want to deepen my skills in research, integration, and presentation. The world no longer cares solely about one’s ability to code—it’s about what the code brings to life. This shift in priorities inspires me to think about how AI can be integrated to build efficiency, innovation, and progress, whether in work or play.
        Ultimately, I want to dive into historic data records to understand where we’re heading, how today’s actions influence tomorrow, and what the future will look like. All of this, to me, is what it means to truly understand data.
        """,
        "Why Corporate After Entrepreneurship?": """
        Straight out of college, I founded my marketing firm, which ran from 2019 to 2024. It was a beautiful journey that shaped and defined my core values. I discovered that once my mind is set on something, there’s no stopping me. With an unbreakable spirit and unwavering commitment, I achieved my goals and added my unique touch to everything I worked on.
        While many seek independence by building their own businesses, I realized I wanted something more—I want access to brilliant minds. I want to surround myself with people who inspire and challenge me, and I see myself as a protégé and a perpetual learner. Working in the corporate world would allow me to prove my mettle, execute bold ideas, and make pitches that create waves of energy, perspective, and progress.
        The hunger to break boundaries, push limitations, and embrace challenges is what drives me. I thrive on impactful work, and I find satisfaction and fulfillment in contributing to something larger than myself. That’s why I’m choosing the corporate route—it’s not just about growth, but about building a legacy alongside like-minded individuals.
        """,
        "Reflections at Data School": """
        Going back to school after five years, I realized how much I love it all. I expected to dive into Python, but I didn’t expect to be swept away by the wonders of generative AI and the groundbreaking advancements happening around me.
        I dedicate my time not just to learning how to use the tools but to understanding their building blocks. Often, I find that great ideas are born out of learning something completely unexpected, and I want to live in that space of discovery forever.
        I may not know everything right now, and I may still be an amateur, but I know more than I did yesterday—and less than I will tomorrow. That’s the mindset I embrace each day. This journey of learning and growth is not only humbling but deeply exciting, and it’s a perspective I hold close to my heart.
        """
    }

    for title, content in blog_posts.items():
        with st.expander(f"**{title}**", expanded=False):
            st.markdown(f"<div class='expander-content'>{content}</div>", unsafe_allow_html=True)

    # Future Goals Section
    st.markdown("<h2 class='header-main'>What Do I Want to Do in the Future? 💭</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='paragraph'>
            I want to never stop learning and be recognised for my willingness and my ability to learn. 
            I want to work with companies that strive to bring out real value and where I will be challenged 
            to contribute and make a striking impact. I might not know everything all at once today, but my goal 
            has always been to know more than I do today, and I am striving to get there.
        </p>
    """, unsafe_allow_html=True)

    # Ongoing Learning Tracks Section
    st.markdown("<h2 class='header-main'>On-going Learning Tracks 📚</h2>", unsafe_allow_html=True)
    st.markdown("""
        <ul class='paragraph'>
            <li>AWS Cloud Certification</li>
            <li>Data Analysis using Python on DataCamp</li>
        </ul>
    """, unsafe_allow_html=True)

# Run the function to display interests
show_interests()
