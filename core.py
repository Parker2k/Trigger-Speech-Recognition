import pyaudio,os
import speech_recognition as sr

def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize_google(audio)
    print(user)
    if user == "Hello":
        return True
    else:
        print("I did not understand")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
            if mainfunction == True:
                print ("This is true")