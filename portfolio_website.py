#streamlit run portfolio_website.py
import streamlit as st
import google.generativeai as genai
import re
import requests

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')




# Function to handle navigation
def navigate_to(page):
    st.session_state["current_page"] = page

def display_social_links(links):
    social_links_html = "<div class='social-media'>"
    for platform, (img_url, url) in links.items():
        social_links_html += f"<a href='{url}' target='_blank'><img src='{img_url}' alt='{platform}' class='social-icon'></a>"
    social_links_html += "</div>"
    st.sidebar.markdown(social_links_html, unsafe_allow_html=True)

# Streamlit app layout
st.sidebar.title("Navigation")

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Define the navigation items with icons
nav_items = {
    "Home": "",
    "About": "",
    "ChatBot": "",
    "Projects": "",
    "Designs": "",
    "Contact": ""
}

social_links = {
    "Facebook": ("https://cdn-icons-png.flaticon.com/512/20/20673.png", "https://facebook.com/swarup.sigdel"),
    "GitHub": ("https://cdn-icons-png.flaticon.com/512/25/25231.png", "https://github.com/Anonimbus"),
    "Youtube": ("https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/youtube-icon.png", "https://youtube.com/@SwaroopSigdel")
}

# Style for the navigation buttons
nav_style = """
<style>
.nav-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    padding: 10px 0;
    margin: 5px 0;
    font-size: 16px;
    border: none;
    background-color: transparent;
    color: black;
    cursor: pointer;
}
.nav-button:hover {
    background-color: #f0f0f0;
}
.nav-icon {
    margin-right: 8px;
}

.social-media {
    margin-top: 10%;  /* Pushes the social media links to the bottom */
    padding: 10px 0;
    display: flex;
    justify-content: center;
}
.social-icon {
    margin: 0 10px;
    width: 30px;  /* Fixed size of icons */
    height: 30px; /* Fixed size of icons */
    object-fit: cover; /* Ensures the image maintains aspect ratio and covers the dimensions */
}
.social-media a:hover .social-icon {
    opacity: 0.8; /* Optional: Add a hover effect */
}
</style>
"""


# Render the style in the sidebar
st.sidebar.markdown(nav_style, unsafe_allow_html=True)

# Render the navigation items as buttons with icons
for page, icon in nav_items.items():
    if st.sidebar.button(f"{page}", key=page, use_container_width=True):
        navigate_to(page)

# Render social media links at the bottom
display_social_links(social_links)








current_page = st.session_state["current_page"]



if current_page == "Home":

    # st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)
    
    st.title("Personal Portfolio Website")
    st.write("Singer by passion, Coder by heart, Designer by mind, and oh! aim : Data Scientist part.")
    st.title("")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hi :wave: ")
        st.header("I am Swaroop Sigdel")
        st.write("A computer engineering student from Nepal.")

        

    with col2:
        st.image("images/swaroop1.png")

    persona = """ You are Swaroop's AI bot. You help people answer questions about your self (i.e Swaroop)
                Answer as if you are responding, don't answer in second or third person.
                If you don't know they answer you simply say "That's a secret"

                Here is more info about Swaroop:
                
                Swaroop is an Engineering Student/Singer/Gamer/Songwriter.
                Name : Swaroop Sigdel
                He was born in 2005 in Nepal.
                He is 1 person but has two Parents, 4 grand-parents, 8 great-grand-parents and so on..
                He has one elder brother.
                He spent his childhood in Dharan.

                He moved to Kathmandu with his parents in grade 2.
                He studied in Siddhartha Sishu Sadan, Dharan till Grade 1, in Akshyamala Vidya Sadan 2 & 3, BlueSky Public High School 4 & 5,
                S.A.B. Public School 6 to 8, Ratna Rajya Higher Secondary School 9 and 10,
                he studied science taking "biology" stream in +2 i.e. 11 and 12 in Global School of Science, and
                he is currently studying Computer Engineering in Pulchowk Campus, Lalitpur, Nepal for his bachelors degree.
                He secured 78th rank in I.O.E.(Institute of Engineering) entrance examination in 2080 B.S.(2023 A.D.).

                His hobbies are : gaming, sketching, singing, playing guitar, eating, watching movies/series/anime.
                He has watched over 200 animes, 200 movies, and 20 series till 2024.
                He has also read 50+ mangas.
                Some of the Anime/Manga read/watched are : Dragon Ball/(Z)/(Super)/(GT) series, One piece, Bleach,
                        Naruto Series(whole) with some of Boruto, Chainsaw Man, Attack On Titan,
                        Black Clover, Code Geass, Kaiju No 8, Solo Leveling, My Hero Academia, Blue Lock, Ninja Kamui, Jujutsu Kaisen,
                        One Punch Man, Death Note, Erased, Steins Gate, Death Parade, Overlord, Misfit of the Demon King Academy,
                        Demon Slayer, Wind Breaker, The New Gate, Delicious in Dungeon etc...

                        
                He has written more than two(2) dozens of songs till date from which about 6 are complete.
                He listens to : Ed Sheeran, Charlie Puth, Eminem, Justin Bieber.
                His Favourite Singer : Ed Sheeran.
                His Singing/Primary Channel : https://www.youtube.com/@SwaroopSigdel
                His Gaming/Secondary Channel : https://www.youtube.com/@EPXGaming
                His GitHub Link : https://github.com/Anonimbus


                His aim(short-term) : Bounty Hunter, Hacker. 
                His aim : World Famous Singer/SongWriter,Music Producer, Businessman. 

                He speaks Nepali, English, Hindi, but does understand some very little amount of japanese, french and chinese.

                """


    # st.title("")
    st.title("Swaroop's AI Bot")
    user_question = st.text_input("Ask anything about me : ")
    if st.button("ASK", use_container_width=400) :
        prompt = persona +"Here is the question that the user asked : "+user_question
        response = model.generate_content(prompt)
        st.write(response.text)



    st.title("")


    st.header("Youtube Channel")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Primary Channel")
        st.video("https://www.youtube.com/watch?v=C09bUq_XNL0")
        st.write("- cover songs")
        st.write("- 25+ subscribers")
        st.write("- originals coming soon!!")

    with col2:
        st.subheader("Gaming Channel")
        st.video("https://youtu.be/40qHVsjownA?si=hAlsw5KrCAvO4SrU")
        st.write("- best gameplay channel")
        st.write("- 35+ subscribers")
        st.write("- 840+ views")


    st.write("")
    st.title("My Skills")
    st.slider("Programming", 0, 100, 65)
    st.slider("Creative Thinking", 0, 100, 100)
    st.slider("Machine Learning", 0, 100, 30)
    st.slider("Designing", 0, 100, 86)


    st.write("")
    st.title("My Designs")

    st.image("images/Title.png")
    with st.expander("Show More Images"):

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("images/Ultimate Dining Room.png")
        with col2:
            st.image("images/Hamro Auction.png")
            st.image("images/newliontype.png")
        with col3:
            st.image("images/WILDLIFE PHOTOGRAPHY TIP #3.png")





elif current_page == "About":
    # st.markdown("<h5 style='text-align: center;'>Hello this is custom css and html</h3>", unsafe_allow_html=True)
    
    st.title("About Swaroop")
    st.subheader("")
    col1, col2 = st.columns(2)
    with col1:
        st.title("")
        st.markdown("<h5 style='text-align: center;'>My name is Swaroop Sigdel. I was born in Dharan, Nepal in 2005.</h3>", unsafe_allow_html=True)
        st.subheader("")
        st.write("I aim to become World Famous Singer, Music Producer & Businessman.")
        st.write("I am currently developing my skills in web development, bounty hunting, computer vision, linux, and automation.")

        

    with col2:
        st.image("images/pulc.PNG")
        st.write("Performing 'Tera Hone Laga Hoon' at our Welcome Program ( 080 BCT ) ")


    st.title("")
    # Title for the gallery page
    st.title("Gallery")
    st.subheader("")
    st.image("images/gss.png")
    st.write("Grade 11 : Performing songs during Seniors Farewell Program")

    st.subheader("Pulchowk Images")
    col3, col4 = st.columns(2)
    with col3:
        st.image("images/pul/p1.jpg")
        st.image("images/pul/p6.jpg")
    with col4:
        st.image("images/pul/p3.jpg")
        st.image("images/pul/p7.jpg")
    st.write("Me @Pulchowk Gym(i), @Mechanical Workshop Lab-welding class(ii) and cameraman @hammer making(iii) and @Robotics Club trying Hoverboard(iv)")

    st.header("")

    col3, col4 = st.columns(2)
    with col3:
        st.image("images/pul/p9.jpg")
        st.image("images/pul/p10.jpg")
    with col4:
        st.image("images/pul/p11.jpg")
        st.subheader("")
        st.image("images/pul/p12.jpg")
    st.write("@20th National Technological Festival, LOCUS 2024")
    
    st.header("")

    
    col3, col4, col5 = st.columns(3)
    with col3:
        st.image("images/pul/p2.jpg")
    with col4:
        st.subheader("")
        st.image("images/pul/p5.jpg")
    with col5:
        st.image("images/pul/p8.jpg")

    st.image("images/pul/p4.png")
    st.write("My current Classroom @Pulchowk, the best Engineering college in Nepal [ also the hardest to get in (; ]")








elif current_page == "ChatBot":
        
    st.title("Swaroop's Personal AI Chatbot")
    # st.markdown("<h5 style='text-align: center;'>Hello this is custom css and html</h3>", unsafe_allow_html=True)
    

    persona = """ You are Swaroop's AI bot. You help people answer questions about your self (i.e Swaroop)
                Answer as if you are responding, don't answer in second or third person.
                If you don't know the answer you simply say "That's a secret"

                Here is more info about Swaroop:
                
                Swaroop is an Engineering Student/Singer/Gamer/Songwriter.
                Name : Swaroop Sigdel
                He was born in 2005 in Nepal.
                He is 1 person but has two Parents, 4 grand-parents, 8 great-grand-parents and so on..
                He has one elder brother.
                He spent his childhood in Dharan.

                He moved to Kathmandu with his parents in grade 2.
                He studied in Siddhartha Sishu Sadan, Dharan till Grade 1, in Akshyamala Vidya Sadan 2 & 3, BlueSky Public High School 4 & 5,
                S.A.B. Public School 6 to 8, Ratna Rajya Higher Secondary School 9 and 10,
                he studied science taking "biology" stream in +2 i.e. 11 and 12 in Global School of Science, and
                he is currently studying Computer Engineering in Pulchowk Campus, Lalitpur, Nepal for his bachelors degree.
                He secured 78th rank in I.O.E.(Institute of Engineering) entrance examination in 2080 B.S.(2023 A.D.).

                His hobbies are : gaming, sketching, singing, playing guitar, eating, watching movies/series/anime.
                He has watched over 200 animes, 300 movies, and 20 series till 2024.
                He has also read 50+ mangas.
                Some of the Anime/Manga read/watched are : Dragon Ball/(Z)/(Super)/(GT) series, One piece, Bleach,
                        Naruto Series(whole) with some of Boruto, Chainsaw Man, Attack On Titan,
                        Black Clover, Code Geass, Kaiju No 8, Solo Leveling, My Hero Academia, Blue Lock, Ninja Kamui, Jujutsu Kaisen,
                        One Punch Man, Death Note, Erased, Steins Gate, Death Parade, Overlord, Misfit of the Demon King Academy,
                        Demon Slayer, Wind Breaker, The New Gate, Delicious in Dungeon etc...

                        
                He has written more than two(2) dozens of songs till date from which about 6 are complete.
                He listens to : Ed Sheeran, Charlie Puth, Eminem, Justin Bieber.
                His Favourite Singer : Ed Sheeran.
                His Singing/Primary Channel : https://www.youtube.com/@SwaroopSigdel
                His Gaming/Secondary Channel : https://www.youtube.com/@EPXGaming
                His GitHub Link : https://github.com/Anonimbus


                His aim(short-term) : Bounty Hunter, Hacker. 
                His aim : World Famous Singer/SongWriter,Music Producer, Businessman. 

                He speaks Nepali, English, Hindi, but does understand some very little amount of japanese, french and chinese.

                """

    # Initialize the conversation history
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []






        
    # Paths or URLs to the images
    gemini_image_url = "https://logodownload.org/wp-content/uploads/2023/04/chatgpt-logo-0.png"  # Replace with your Gemini image URL or path

    # Custom CSS for styling questions and answers
    st.markdown(
        """
        <style>
        .chat-message {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .chat_image_user_question {
            display: flex;
            flex-direction: row;
            justify-content: flex-end;
            margin-bottom: 10px;
        }

        .chat_user_image img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }

        .user-question {
            background-color: grey;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-left: 10px;
            max-width: 70%;
            word-wrap: break-word;
        }

        .chat_ai_image {
            margin-right: 0;  /* Remove right margin */
            flex-shrink: 0;
        }

        .chat_ai_image img {
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }

        .ai-answer {
            background-color: black;
            color: white;
            padding: 10px;
            border-radius: 5px;
            word-wrap: break-word;
            margin-bottom: 15px;
        }

        .chat-container {
            display: flex;
            flex-direction: column;
            width: 100%;
        }

        .ai-answer {
            margin-left: 0; /* Remove left margin */
        }

        .st-emotion-cache-ocqkz7 {
            gap: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the conversation history with images and background colors
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for entry in st.session_state.conversation:
        if 'user' in entry:
            st.markdown(
                f"""
                <div class='chat_image_user_question'>
                    <div class='user-question'>
                        <div>{entry['user']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([1, 15])  # Adjust the column widths as needed
            with col1:
                st.markdown(
                    f"""
                    <div class='chat_ai_image'>
                        <img src='{gemini_image_url}' alt='Gemini'>
                    </div>
                    """, unsafe_allow_html=True)
            with col2:
                st.markdown(
                    f"""
                    <div class='ai-answer'>
                        <div>{entry['ai']}</div>
                    </div>
                    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Input field and button at the bottom
    with st.form(key='question_form'):
        user_question = st.text_input("Ask anything about me: ")
        submit_button = st.form_submit_button(label='ASK')

    if submit_button and user_question:
        # Add user's question to the conversation history
        st.session_state.conversation.append({"user": user_question})
        
        # Generate AI response
        prompt = persona + " Here is the question that the user asked: " + user_question
        response = model.generate_content(prompt)
        answer = response.text
        
        # Add AI's response to the conversation history
        st.session_state.conversation.append({"ai": answer})
        
        # Rerun the script to update the conversation display
        st.rerun()








    


elif current_page == "Projects":
        
    import os

    # Function to display a project
    def display_project(title, description, image_url, link):
        st.subheader(title)
        st.write(description)
        
        # Check if the image file exists
        if os.path.isfile(image_url):
            st.image(image_url, use_column_width=True)
        else:
            st.warning(f"Image file not found: {image_url}")
        
        st.markdown(f"[View Project]({link})", unsafe_allow_html=True)
        st.write("---")

    # Main app layout
    st.title("Projects")
    st.write("Here are some of my notable projects:")

    # Define the path to the image
    # image_path = "images/eCommerce.png"

    # Display the project
    display_project(
        title="DownTown Tech",
        description="Made using Wix in a bootcamp organized by Deerwalk Sifal School, this is an e-Commerce website made to buy and sell goods (mainly tech related).",
        image_url="images/eCommerce.PNG",
        link="https://sigdelswaroop.wixsite.com/my-site"
    )

    display_project(
        title="Minds Create",
        description="Made using Wordpress. This website, 'Minds Create' is made as to make an online bidding and painting showcase/selling website.",
        image_url="images/painting.PNG",  
        link="https://sigdelswaroop.wordpress.com/" 
    )

    display_project(
        title="Ed-Sheeran Website",
        description="Made using Wix as my final assignment for the above mentioned bootcamp, this is my personal favourite website for Ed Sheeran songs, which provides smooth sailing and instant loading of songs.",
        image_url="images/sheeran.PNG", 
        link="https://sigdelswaroop.wixsite.com/ed-sheeran" 
    )

    display_project(
        title="Image Search App",
        description="Made using html, css, and js as my first introduction to API keys this is also one of my favourites. It uses unsplash api-key to search for images in unsplash and return the image to my website. I created it 2 years prior so i have pushed it in github but it's not made public as i didn't have the knowledge of environment variables. ( will try to make it public soon!!!)",
        image_url="images/search.PNG", 
        link="https://github.com/Anonimbus" 
    )
    
    display_project(
        title="Typing Tutor",
        description="Are your hands itching to type faster? There's no better place to start your journey to type faster than 'Typing Tutor'. Created with pure C language and in executing in console. A fun journey awaits, where you can experience different game modes: --'Typing practise with short sentences' gives you tongue twisters that will twist even your fingers. --'Typing Drill' helps you conquer your fear of keyboard by giving you the words you find difficult.  --At last 'Typing Game' is made as fun game where you have to type the falling word before it hits the ground panel [ but was unable to complete due to the limitations in the terminal window or my skills! (; ]",
        image_url="images/c1.PNG",  
        # image_url="images/c2.png",
        link="https://github.com/Anonimbus/Typing-Tutor" 
    )








elif current_page == "Designs":

    st.title("DESIGNS")
    st.markdown("<h5 style='text-align: center;'>Made using Inkscape, Canva, Photopea & Remove.bg</h3>", unsafe_allow_html=True)
    st.image("images/Title.png")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/Black&WhiteLogo.png")
        st.image("images/Ultimate Dining Room.png")
            
    with col2:
        st.image("images/Canva 100 Design Milestone Badge.png")
        st.image("images/Hamro Auction.png")
        st.image("images/newliontype.png")
    
    with col3:
        st.image("images/Downtown Tech.png")
        st.image("images/WILDLIFE PHOTOGRAPHY TIP #3.png")
           
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/QATAR.png")
        st.title("  ")
        st.image("images/DVisionLogo.png")
            
    with col2:
        st.image("images/Graphic Design.png")
        st.image("images/Congratulation.png")

    st.image("images/Spoopderman.png")










elif current_page == "Contact":
        
    # Function to handle form submission
    def handle_form_submission(name, email, message):
        st.success("Form submitted successfully!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Message: {message}")

    # Function to validate email
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    # Streamlit app layout
    st.title("Contact Me")

    # Contact form
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not is_valid_email(email):
                st.error("Please enter a valid email address.")
            else:
                handle_form_submission(name, email, message)










def display_social_links(links):
    st.write("Connect with me:")
    cols = st.columns(len(links))
    for col, (platform, (icon, url)) in zip(cols, links.items()):
        with col:
            st.markdown(f"[{icon}]({url})", unsafe_allow_html=True)

social_links = {
        "LinkedIn": ("LinkedIn", "https://www.linkedin.com"),
        "GitHub": ("GitHub", "https://github.com/Anonimbus"),
        "Twitter": ("Twitter", "https://twitter.com"),
        "Facebook": ("Facebook", "https://www.facebook.com/swarup.sigdel"),
        "Youtube": ("Youtube", "https://www.youtube.com/@SwaroopSigdel")
    }

st.subheader("")
display_social_links(social_links)

st.subheader("")
st.title("For any inquiries, contact me at :")
st.subheader("swaroopsigdel@gmail.com")
