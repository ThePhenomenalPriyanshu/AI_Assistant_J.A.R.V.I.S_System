import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishes():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hii Dear, I am Cortana and Mr.Priyanshu send me to help you. Please tell me how may i help you!!")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    speak("Cortana wishes happy Birthday Dad")
    wishes()
    while True:
        query=takecommand().lower()
        
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open github" in query:
            webbrowser.open("github.com")

        elif "play music" in query:
            music_dir="D:\MUSIC"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))