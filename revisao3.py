import speech_recognition as sr

microfone = sr.Microphone()
reconhecedor = sr.Recognizer()

with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    print("Fale algo...")
    audio = reconhecedor.listen(mic)
    print("Reconhecendo...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print("Você falou...", texto)