import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
#vol=engine.getProperty('volume')
#print(engine.getProperty('volume'))
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
        speak("Good evening Sir,long day ha")
    speak("I am Alen, how may i help")

def volume_down():
    vol=engine.getProperty('volume')
    if vol == 0 :
        speak("the volume is minimum")
        print(vol)
    else:
     vol=vol-1
     engine.setProperty('volume',vol)
     print("is the volume is okay")
     speak("is the volume is okay")

def volume_up():
    if vol == 10:
        speak("the volume is maximum")
        print(vol)
    else:
     vol=vol+1
     engine.setProperty('volume',vol)
     print("is the volume is okay")
     speak("is the volume is okay")

    vol
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"Boss said: {query}\n")  
    except Exception as e:
       # print(e)
        print("Couldn't Hear You..")
        return "None"        
    return query

def wiki(query):
    speak('Searching in wikipedia')
    query = query.replace("wikipedia", " ")
    try: 
        results = wikipedia.summary(query,sentences=2)
    except Exception as e: 
        print("Server is slow, Please try again")
        speak("Server is slow, Please try again")
        #print(engine.getProperty('rate'))
    speak("According to wikipedia")
    print(results)
    speak(results)


if __name__ == "__main__":
    engine.setProperty('rate', 170)
   # volume_down()
    #speak("Harry is a good boy")
    wishme()
    while True:
       query=take().lower()
       #logics
       if 'wikipedia' in query:
           wiki(query)
          











          
