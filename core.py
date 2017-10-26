import pyaudio,os
import speech_recognition as sr


class recognition:
    # you can set variables here by doing self.variable = "blah"
    def init(self, user): # including self in the function enables you to call the variables within the class
        if user == "hello":
            print "verified"
            #Start writing your code here, this is where it will be initiated
            return True
        else:
            print "sorry i didn't understand"
            return False
    
    def mainFunction(self, user):
        if user == "tell me the weather":
            print("boobs")


if __name__ == "__main__":
    r = sr.Recognizer()
    recog = recognition() # setting up your new class
    # listen until I hear the pick up word
    with sr.Microphone() as source:
        user = ""
        while recog.init(user) == False:
            try:
                audio = r.listen(source)
                user = r.recognize_google(audio)
                recog.init(user) #now the class has been set you can call functions such as recog.init etc 
                # when you want a certain function under a class you can do recog.NewFunction()
            except Exception:
                pass
            
        #start main script
        try:
            audio = r.listen(source)
            user = r.recognize_google(audio)
            recog.mainFunction(user)
        except Exception:
            pass

    
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
