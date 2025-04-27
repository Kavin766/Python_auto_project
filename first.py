import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pyautogui
import time
import subprocess

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female voice

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
    speak("Which account do you want to use? Account one or account two?")
    account_choice = listen_command()

    if 'first account' in account_choice or '1' in account_choice:
        speak("Opening Instagram with Account 1.")
        subprocess.Popen(
            r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 1" https://www.instagram.com'
        )
    elif 'second account' in account_choice or '2' in account_choice:
        speak("Opening Instagram with Account 2.")
        subprocess.Popen(
            r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2" https://www.instagram.com'
        )
    else:
        speak("I did not understand which account. Opening Instagram in default browser.")
        webbrowser.open('https://www.instagram.com')

def open_instagram_explore():
    speak("Opening Instagram Explore page.")
    subprocess.Popen(
        r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2" https://www.instagram.com/explore/'
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
