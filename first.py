import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pyautogui
import subprocess

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female voice

# Global variable to store which profile is currently selected
current_profile = None

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
    except:
        command = ""
    return command

def open_instagram():
    global current_profile
    speak("Which account do you want to use? Account one or account two?")
    account_choice = listen_command()

    if 'first account' in account_choice or '1' in account_choice:
        current_profile = "Profile 1"
        speak("Opening Instagram with Account 1.")
    elif 'second account' in account_choice or '2' in account_choice:
        current_profile = "Profile 2"
        speak("Opening Instagram with Account 2.")
    else:
        speak("I did not understand which account. Opening Instagram in default browser.")
        webbrowser.open('https://www.instagram.com')
        return  # Exit function if default browser is used

    # Open Instagram with selected profile
    subprocess.Popen(
        fr'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="{current_profile}" https://www.instagram.com'
    )

def open_instagram_explore():
    global current_profile
    if current_profile is None:
        speak("You haven't selected an account yet. Please open Instagram first.")
        open_instagram()
    else:
        speak("Opening Instagram Explore page.")
        subprocess.Popen(
            fr'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="{current_profile}" https://www.instagram.com/explore/'
        )

def run_jarvis():
    command = listen_command()
    if 'hello' in command:
        speak('Hello Sir, how can I help you?')
    elif 'your name' in command:
        speak('I am your personal assistant, Jarvis.')
    elif 'how are you' in command:
        speak('I am functioning within optimal parameters.')
    elif 'open instagram' in command:
        open_instagram()
    elif 'open stories' in command:
        speak('Opening Instagram stories.')
        webbrowser.open('https://www.instagram.com/stories/')
    elif 'open explore' in command or 'instagram explore' in command:
        open_instagram_explore()
    elif 'close all' in command:
        speak('Closing all Chrome windows.')
        os.system("taskkill /im chrome.exe /f")
    elif 'close' in command or 'close insta' in command or 'close instagram' in command:
        speak('Closing the current tab.')
        pyautogui.hotkey('ctrl', 'w')
    else:
        speak('Sorry, I did not understand that.')

if __name__ == "__main__":
    while True:
        run_jarvis()
