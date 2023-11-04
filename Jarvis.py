import speech_recognition as sr
import pyttsx3
import webbrowser 
import os
import pyautogui as gui


# Initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello")
speak("How  can i help you?")

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Waiting for command....")
        audio = r.listen(source,0,5)

    try:
        text = r.recognize_google(audio)
        print("You said : ", text)
        
    except Exception as e:
        print("say that again...")
        return "None"
    text = str(text)
    return text.lower()


def MainTask():
    while True:
        command = recognize_speech()
        # Add your own commands here
        if "hello" in command:
            speak("Hello")
        elif "what's is your name" in command:
            speak("My name is kelly.")
        elif "what is your name" in command:
            speak("I am kelly.")
        elif "how are you" in command:
            speak("I am Fine , How are you?")
        elif "I am fine " in command:
            speak("Good , i hope you always stay fine and healthy.")
        elif "who are you" in command:
            speak("I am kelly , Voice Assistant.")
        elif "who created you" in command:
            speak("Rut  Rupala   Created   me.")
            print("Rut Rupala.")
        elif "good" in command:
            speak("Thank you..")
        elif "Thanks" in command:
            speak("Welcome.")        
        elif "thank you" in command:
            speak("Welcome.")
        elif "stop" in command:
            speak( "you can call me when you need.")
            break
        elif "Take a rest " in command:
            speak("Ok")
            speak("as you wish , you can call me whenever you need.")
            break
        elif "break" in command:
            speak("Ok , call me when you need.")
            break
        elif "I am gettig bored" in command:
            speak("You should start watching Anime or Marvel movie.")
        elif "open youtube" in command:
            speak("opening YouTube..")
            webbrowser.open("https://www.youtube.com")
        elif "close YouTube" in command:
            speak("Ok , YouTube Closed.")
        elif "multi message" in command:
            speak("Ok sir, starting spammer bot") 
            os.startfile("Spammer.py")   
        elif "what are you doing" in command:
            speak("Talking with you Sir.")
        elif "pose" in command:
            speak("ok siry")
            gui.press("k")
        elif "start" in command:
            speak("ok sir")
            gui.press("k")
        elif "byy" in command:
            speak("Ok Byy Sir")
            break
        elif "what can you do" in command:
            speak("I can do only something that written in my code.")
        elif "tell me about yourself" in command:
            speak("I am Artifical , Inteligent ,  Created , by Rut Rupala. And My Name is Kelly .")
        
if __name__ == "__main__":
    MainTask()
