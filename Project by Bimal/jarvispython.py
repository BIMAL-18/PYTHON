import pyttsx3
import webbrowser
from datetime import datetime
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Use the text-to-speech engine to speak the text."""
    engine.say(text)
    engine.runAndWait()

def open_website(url):
    """Open a website in the default web browser."""
    webbrowser.open(url)
    speak(f"Opening {url}")

def tell_time():
    """Tell the current time."""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")
    print(f"The current time is {current_time}")

def handle_command(command):
    """Handle different commands."""
    command = command.lower()

    if 'open website' in command:
        # Extract the URL from the command
        url = command.split('open website ')[1]
        open_website(url)
    elif 'time' in command:
        tell_time()
    else:
        speak("Sorry, I didn't understand that command.")

def listen_command():
    """Listen for a command from the user."""
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
    """Main function to run the assistant."""
    speak("Hello, I am your assistant. How can I help you?")
    print("You can say 'open website <url>' to open a website or 'time' to get the current time.")

    while True:
        command = listen_command()
        if command:
            if 'exit' in command or 'quit' in command:
                speak("Goodbye!")
                break
            handle_command(command)

if __name__ == "__main__":
    main()
