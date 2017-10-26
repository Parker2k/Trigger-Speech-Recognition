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


"""

This script is meant to consistently listen for a trigger word. In this case 'hello'.

Once the trigger word has been processed the script would in some way, authenticate and then 
pass to another function where more commands could be passed. If the trigger word is not
authenticated then the system should keep listening and do nothing other then print to the 
console. 

Another issue I am facing is that Google Speech throws an error when it picks up voice 
that it does not recognise. I need to find a way to catch this and restart the function.
 
"""