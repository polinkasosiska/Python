

'''
Надо скачать следующие модули, чтобы запустить

откройте терминал и введите: 
pip install pipwin
pipwin install pyaudio
pip install speechRecognition


так же потребуется определить правильный индекс устройства с плмлщью команды - 
pip install speechRecognition

'''


import pyaudio
import speech_recognition as sr
import os
import pyttsx3
import random
import webbrowser

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Здравствуйте, я ваш голосовой помощник")
voice.runAndWait()
greetings = ["Привет", "Здравствуйте", "Доброго времени суток", "Хай", "Ку"]

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь ...")
        audio = r.listen(source)

    try:
        speech = r.recognize_google(audio, language="ru_RU").lower()
        print("Вы сказали: " + speech)
        if speech.find("привет") >= 0 or speech.find("хай") >=0:
            voice.say(random.choice(greetings))
            voice.runAndWait()
        elif speech.find("открой файл") >= 0 or speech.find("игра") >=0:
            os.startfile("C:/Users/Vitaliy/Desktop/arkanoid.py")
            voice.say("Игра запущена")
            voice.runAndWait()
        elif "youtube" in speech:
            webbrowser.open_new("https://www.youtube.com/?gl=RU&hl=ru")
            voice.say("Ютуб запущен")
            voice.runAndWait()
        elif speech.find("пока") >= 0 or speech.find("до свидания") >=0:
            voice.say("До свидания")
            voice.runAndWait() 
            break
        else:
            voice.say("Я вас не понимаю, повторите пожалуйста")
            voice.runAndWait() 
    except:
        print("Ошибка, я вас не услышала")

    



