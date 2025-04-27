import speech_recognition as sr
import pyttsx3
import webbrowser  # <-- Added this to open websites

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice (optional, makes it sound cooler)
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

def run_jarvis():
    command = listen_command()
    if 'hello' in command:
        speak('Hello Sir, how can I help you?')
    elif 'your name' in command:
        speak('I am your personal assistant, Jarvis.')
    elif 'how are you' in command:
        speak('I am functioning within optimal parameters.')
    elif 'open instagram' in command:
        speak('Opening Instagram for you.')
        webbrowser.open('https://www.instagram.com')
    else:
        speak('Sorry, I did not understand that.')

if __name__ == "__main__":
    while True:
        run_jarvis()
