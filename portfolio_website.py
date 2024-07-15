#streamlit run portfolio_website.py
# import time
import streamlit as st
import google.generativeai as genai


api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


if 'sidebar_opened' not in st.session_state:
    st.session_state.sidebar_opened = False
    
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Select a page:", ["Home", "About", "Designs"])

# Display the option selected
st.write(f"Current Page: {option}")




if option == "Designs":
    
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



elif option == "Home":

    # st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Hi :wave: ")
        st.title("I am Swaroop Sigdel :fire::candle: :hole:")
        st.write("Singer by passion, Coder by heart, Designer by mind, and oh! aim : Data Scientist part.")

    with col2:
        st.image("images/swaroop.png")

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

    with col2:
        st.subheader("Gaming Channel")
        st.video("https://youtu.be/40qHVsjownA?si=hAlsw5KrCAvO4SrU")
        st.write("- best gameplay channel")
        st.write("- 35+ subscribers")
        st.write("- 400000+ bros")


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



st.subheader("")
st.write("CONTACT")
st.title("For any inquiries, contact me at :")
st.subheader("swaroopsigdel@gmail.com")