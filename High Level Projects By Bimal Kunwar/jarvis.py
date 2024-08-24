import pyttsx3
import webbrowser
import subprocess
from datetime import datetime
import speech_recognition as sr
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_chrome():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open("chrome.com")
    speak("Opening Chrome")

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening sir ")

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")
    print(f"The current time is {current_time}")

def handle_command(command):
    command = command.lower()

    if 'hi jarvis' in command:
        speak("Hi Bimal sir, what can I help you ")
    elif 'good morning' in command:
        speak("Hi Bimal sir, Good Morning")
    elif 'good bye' in command:
        speak("See You Buddy")
    elif 'take rest' in command:
        speak("ok Bimal sir have a good day.")
    elif 'open chrome' in command:
        open_chrome()
    elif 'open YouTube ' in command:
        open_website("https://www.youtube.com/watch?v=4R2WjSSPkBU&list=RD4R2WjSSPkBU&start_radio=1")
    elif 'time' in command:
        tell_time()
    else:
        speak("Sorry, I didn't understand that command.")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
            return None

def main():
    speak("Hello Bimal , I am Jarvis and I am your personal assistant. Sir give me some command")
    print("You can say 'Hi Jarvis', 'open Chrome', or 'open YouTube'.")

    while True:
        command = listen_command()
        if command:
            if 'exit' in command or 'quit' in command:
                speak("Goodbye Bimal. I come when you call me!")
                break
            handle_command(command)

if __name__ == "__main__":
    main()
