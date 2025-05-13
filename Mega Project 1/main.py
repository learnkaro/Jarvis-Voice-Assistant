import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
musicLibrary = musicLibrary.music

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open" in command:
        if "notepad" in command:
            os.startfile("notepad.exe")
            speak("Opening Notepad")
        elif "calculator" in command:
            os.startfile("calc.exe")
            speak("Opening Calculator")
        elif "chrome" in command:
            os.startfile("chrome.exe")
            speak("Opening Chrome")
        else:
            speak("I don't know how to open that application.")
    
    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        link = musicLibrary.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, {song} not found in your music library.")
    
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google.")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I didn't understand that command.")

    return True

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Speech recognition service is down.")
        return ""

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        print("Waiting for wake word 'Jarvis'...")
        command = listen_command()
        if "jarvis" in command:
            speak("Yes, how can I help you?")

            while True:
                user_command = listen_command()
                if user_command:
                    continue_loop = processCommand(user_command)
                    if not continue_loop:
                        break
