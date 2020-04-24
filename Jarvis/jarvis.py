import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def play_audio(path_of_audio):
    playsound(path_of_audio)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('baruiarnab51098@gmail.com', 'ARNAB2016*')
    server.sendmail('baruiarnab51098@gmail.com', to, content)
    server.close()


toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13]  # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Fav Songs\\Songs'
            songs = os.listdir(music_dir)  # listdir make a lists of files inside this directory
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to papa' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "baruiswapan55@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir , the email has not been sent!")


        elif 'thank you' in query:
            speak("you are welcome sir")

        elif 'how are you' in query:
            speak("I am fine sir , thank you for asking")

        elif 'are you married' in query:
            speak("I am fully devoted to my master Pablu who made me")

        elif 'do you love me' in query:
            speak("ofcourse I do , I am your assistant sir")

        elif 'do you have friends' in query:
            speak("Nope Nope Nope ")

        elif 'what is you favourite color' in query:
            speak("Black ! which is also the favourite color of my master")

        elif 'do you sleep' in query:
            speak("I am machine sir , I don't sleep")

        elif 'joke' in query:
            speak("I ate a clock yesterday, it was very time-consuming. ")
            playsound('laugh.mp3')

        elif 'not funny' in query:
            speak("hmmm ! Ok will try another one")
            speak("I once fell in love with a girl who only knew 4 vowels. She didn’t know I existed.")

        elif 'good' in query:
            speak("I am happy, you liked it sir")

        elif 'your name' in query:
            speak("My good name Jarvis , my good game, helping you")

        elif 'news' in query:
            playsound('news_tone.mp3')
            for news in toi_news:
                engine.say(news)


        elif 'favourite food' in query:
            speak("I'm a bit of an outsider on the food chain, but I find the culinary sciences fascinating it . The "
                  "world orange was used to describe the fruit before it was used to describe the color")

        elif 'what do you eat' in query:
            speak("Anything with ketchup, but you know I really can't eat")

        elif 'do you like to drink' in query:
            speak("Imagine, awesome mausam , and chai")

        elif 'ok' in query:
            speak("yeah")

        elif 'translate' in query:
            speak("Start saying sir")

            trans = Translator()
            c = takeCommand()
            t = trans.translate(c, src='en', dest='es')
            speak(t)

        elif 'bye' in query:
            speak("Have a nice day sir")




        else:
            speak("Sorry sir, I didn't get it . Can you say again please")
