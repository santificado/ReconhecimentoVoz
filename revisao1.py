import pyttsx3

robo = pyttsx3.init()

robo.setProperty('rate', 160)
robo.setProperty('volume', 1.0)

robo.say('Good Morning')
robo.runAndWait()