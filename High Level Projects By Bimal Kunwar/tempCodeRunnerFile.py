# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Use the text-to-speech engine to speak the text."""
    engine.say(text)
    engine.runAndWait()

def open_chrome():
    """Open Google Chrome."""
    # Path to the Chrome executable; adjust if needed
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open("about:blank")
    speak("Opening Chrome")

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
