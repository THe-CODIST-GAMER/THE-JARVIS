# MODULES
import pyttsx3
import datetime
import requests 
from requests import get
import GUI
import time
import pyautogui
import pyttsx3
import datetime 
from datetime import sleep
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import random
import pyjokes
import PyPDF2
import pygame
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
import pathlib
import pyttsx3
import speech_recognition as sr
import warnings
import keyboard
import pyautogui as py
warnings.simplefilter('ignore')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)
#print(voices[2].id)
#print(voices[3].id)
#print(voices[4].id)
#print(voices[5].id)
#print(voices[6].id)
#print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    GUI.speak(audio)
    engine.say(audio)
    engine.runAndWait()
# WISH ME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
      speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Jarvis Here , an AI Langusge Model!!How may i help you?")


    


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() 
    with sr.Microphone() and keyboard as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='detect language') 
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def run_alpha():
        input = takeCommand()
        print(input)
        url = "http://api.brainshop.ai/get?bid=157984&key=3S0hhLXZ5GS2KYs4&uid=[uid]&msg=[{}]".format(input)
        response = requests.get(url).json()['cnt']
        print(response)
        speak(response)

wishMe()
def run_alpha():
        query = takeCommand()
        print(query)
# WIKIPEDIA
        if 'Wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# OPEN YOUTUBE
        elif 'open YouTube' in query:
            speak('Okay!')
            webbrowser.open("https://www.youtube.com")
# OPEN GOOGLE
        elif 'open Google' in query:
            speak('Okay!')
            webbrowser.open("https://www.google.com")
# OPEN GITHUB
        elif 'open Github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

# It writes the content to output 
        
# OPEN INSTAGRAM
        elif 'open Discord' in query:
            webbrowser.open("https://discord.com")
            speak("opening!!!!!!!")
# SEARCH SOMETHING ON GOOGLE
        elif 'Search on Google' in query or 'Search something' in query:
            speak("What would you like to search on google?")
            webbrowser.open("https://www.google.com")
            time.sleep(3)
            py.write(query , interval=0.1)
            py.keyDown('return')
            py.moveTo(0, 500)
            py.keyDown('tab')

#BARD AUTO
        elif 'Search on Bard' in query or 'Write + "  "' in query:
            speak("OK...")
            webbrowser.open("https://bard.google.com/chat")
            


# SOME YOUTUBE VIDEOS
        elif 'Open Gmail' in query:
            speak ("OFCOURSE!!!")
            webbrowser.open( "https://mail.google.com/mail/u/0/#inbox" )

        elif 'Play Tech Burner' in query:
            speak("YEAH!!, TECHNOLOGY BURNi'N")
            webbrowser.open("https://www.youtube.com/@TechBurner")

        elif 'Play Kaushik Shresth' in query:
            speak("YEAH!!,......")
            webbrowser.open("https://www.youtube.com/@Kaushikshresth")

        elif 'Play my favourite videos' in query:
            speak("Choosing....")
            webbrowser.open("https://www.youtube.com/@RAAAZofficial")

        


        


# WHATS THE TIME
        elif 'The Time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")

# OPEN NOTEPAD
        elif 'open notepad' in query:
            speak('Okay!')
            nPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(nPath)
# OPEN COMMAND PROMPT
        elif 'open command prompt' in query or 'open CMD' in query:
            speak('Okay!')
            os.system('start cmd')

# SEND WHATSAPP MESSAGE
        elif 'send message' in query:
            speak('Okay! Sending Message...')
          
            pywhatkit.sendwhatmsg('number here', 'message here', "time here")
# PLAY MUSIC FROM YOUTUBE
        elif 'Play a song' in query:
            song = query.replace('Play a song', '')
            speak('playing ' + song)
            webbrowser.open("https://www.youtube.com/results?search_query=" + song)
# SIMPLE TALKS
        elif "What\'s up" in query or 'How are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif ' made you' in query or ' created you' in query or ' developed you' in query:
            ans_m = " For your information Mr.Arinjoy Acharya Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        
        elif "Hello" in query or "Hello Jarvis" in query:
            hel = "Hello Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "Your name" in query  or "your name" in query :
            na_me = "Thanks for Asking my name my self ! JARVIS"  
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very energetic after meeting with you")
            speak("feeling Very energetic after meeting with you")
        elif "Shut up" in query:
            print("sorry???")
            speak("sorry???")
            exit (takeCommand)
        elif "not felling well" in query:
            speak("WAIT.....Take a deep breath,don'worry....")
            webbrowser.open('https://www.google.com/search?q=doctors+near+me&oq=doctors&gs_lcrp=EgZjaHJvbWUqBwgBEAAYjwIyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIHCAMQABiPAtIBCDUyMDlqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8&dlnr=1&sei=gs1tZe-eFo3x-QaE2b3gBg')
        elif "I have fever" in query:
            speak("Take in Calpol 650 or 500 according to your health and drink lots of water you will feel good")

#IP ADDRESS
        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
# JOKE
        elif "Tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        
# FIND LOCATION
        elif "Location" in query or "location" in query:
            speak("wait sir let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir im not sure, but we are in {city} city {state} state of {country} country")
            except Exception as e:
                speak("Sorry Sir, Due to network issue i am not able to find where we are.")
                pass
# TAKE SCREENSHOT
        elif "Take a screenshot" in query:
            speak("Sir, Please tell me the name for the screenshot file")
            name = takeCommand().lower()
            speak("Taking Screenshot...!")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("ScreenShot Saved...!")

        else:
            speak('OK!!Acessing Database...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("If I am not wrong,...")
            print(results)
            speak(results)

       

GUI.set_speak_command(run_alpha)
GUI.mainloop()











engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    GUI.speak(audio)
    engine.say(audio)
    engine.runAndWait()
# WISH ME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
      speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Jarvis Here,How may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


    
