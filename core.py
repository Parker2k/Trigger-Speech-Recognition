import pyaudio,os
import speech_recognition as sr

def mainfunction(source):
    audio = r.listen(source)
    user = r.recognize_google(audio)
    print(user)
    if user == "hello":
        return True
    else:
        return False

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while mainfunction(source) != True:
            print ('working')




"""

This script is meant to consistently listen for a trigger word. In this case 'hello'.

Once the trigger word has been processed the script would in some way, authenticate and then 
pass to another function where more commands could be passed. If the trigger word is not
authenticated then the system should keep listening and do nothing other then print to the 
console. 

Another issue I am facing is that Google Speech throws an error when it picks up voice 
that it does not recognise. I need to find a way to catch this and restart the function.
 
"""

"""

Below is the error the program returns when it cannot recognise the word. I need to catch 
this and then return the function seamlessly if possible... 

Traceback (most recent call last):
  File "core.py", line 18, in <module>
    while mainfunction(source) != True:
  File "core.py", line 6, in mainfunction
    user = r.recognize_google(audio)
  File "/Library/Python/2.7/site-packages/speech_recognition/__init__.py", line 780, in recognize_google
    if not isinstance(actual_result, dict) or len(actual_result.get("alternative", [])) == 0: raise UnknownValueError()
speech_recognition.UnknownValueError

"""