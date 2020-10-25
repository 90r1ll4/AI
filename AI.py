import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
#print(voices)
#engine.say("hello")
#engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir, How u r Feeling")
    elif hour>12 and hour<17:
        speak("Good Afternoon Sir,Lets get to work")
    elif hour>17:
        speak("Good evening Sir,long day uhh")
    speak("I am Alen, I am ready to roll")




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"Boss said: {query}\n")  
    except Exception as e:
        print(e)
        print("Couldn't Hear You..")
        return "None"        
    return query

if __name__ == "__main__":
    #speak("Harry is a good boy")
    wishme()
    take()