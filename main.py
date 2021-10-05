import speech_recognition as sr
import webbrowser
import time
from playsound import playsound
import os
import random
from gtts import gTTS 
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            zoey_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)    
        except sr.UnknownValueError:
            zoey_speak("Sorry, I dont understand what you said")
        except sr.RequestError:
            zoey_speak("Sorry, I can't help you now.")
        return voice_data

def zoey_speak(audio_string):
    tts = gTTS(text = audio_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        zoey_speak('My name is Zoey, is that Williams?')
    if 'Did you say' in voice_data:
        zoey_speak('Yes')
    if "Yes, it's Williams" in voice_data:
        zoey_speak('Good to hear from you again, what do you want this time?')
    if 'what time is it' in voice_data:
        zoey_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        zoey_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What location ?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        zoey_speak('Here is the location' + location)
    if 'interesting' in voice_data:
        zoey_speak('What is interesting?')
    if 'You are doing well' in voice_data:
        zoey_speak('Thank you')
    if 'Thank You' in voice_data:
        zoey_speak('You are welcome')
    if 'exit' in voice_data:
        exit()


time.sleep(1)
zoey_speak('How may I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)

