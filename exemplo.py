import pyttsx3
import speech_recognition as sr
import os

try:
    microfone = sr.Microphone()
    reconhecedor = sr.Recognizer()
    with microfone as mic:
        reconhecedor.adjust_for_ambient_noise(mic)
        print("Do you want to listen a music")
        robo = pyttsx3.init()
        robo.setProperty('volume',1.0)
        robo.setProperty('rate', 160)
        robo.say("Do you want to listen a music?")
        robo.runAndWait()
        audio = reconhecedor.listen(mic)
        print("Entendido...")
        texto = reconhecedor.recognize_google(audio, language='pt')
        print("Você falou...", texto)

        respostas = ["OK", "YES", "SIM", "BELEZA"]
        if texto.upper() in respostas:
            print("Ok, wait a moment...")
            robo.say("Ok, wait a moment")
            robo.runAndWait()
            os.system('Ankara.mp3')
        else:
            print("Ok, bye!")
            robo.say("Ok, bye")
            robo.runAndWait()
except:
    print("Buguei")
