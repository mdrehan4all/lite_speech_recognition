import speech_recognition as sr

recording = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        recording.adjust_for_ambient_noise(source)
        print("Please Say something:")
        audio = recording.listen(source)
    try:
        print("You said: \n" + recording.recognize_google(audio))
    except Exception as e:
        print(e)