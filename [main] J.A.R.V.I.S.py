import pyttsx3
import speech_recognition
import requests
import webbrowser
import wikipedia










   
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source,0,4)

    
    try:
        print("understanding")
        query = r.recognize_google(audio, language="en-in")
        print(f"you  said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
     query = takecommand().lower()
     if "wake up" in query:
    

        from greetme import greetme
        greetme()

        if " wake up JARVIS" in query:
                from greetme import greetme
                greetme()
            

        while True:
            query = takecommand().lower()
            if "go to sleep" in query:
                speak("ok sir , you can call me anytime ")
                break
            
            elif " how r u " in query:
                speak("i am good sir what about you")
            elif " hello" in query:
                speak("hello sir how can i help you")
            elif"what is your name" in query:
                speak("my name is JARVIS sir ") 
            elif "tell me your name " in query:
                speak("my name is JARVIS sir ")
            elif "who created you" in query:
                speak("i was created by  YASH")
            elif " who are you " in query:
                speak("i am a artificial intelligence my name is JARVIS and i was created by YASH ")
            elif " who r u " in query:
                speak("i am a artificial intelligence my name is JARVIS and i was created by YASH ")
            elif " hu r u " in query:
                speak("i am a artificial intelligence my name is JARVIS and i was created by YASH ")
            
            elif "search" in query:
                query = query.replace(" jarvis", "")
                query = query.replace("search", "")
                query = query.replace("google", "")
                speak("searching sir.......")
                speak(query)
                speak("in google")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif "google" in query:
                query = query.replace(" jarvis", "")
                query = query.replace("search", "")
                query = query.replace("google", "")
                speak("searching sir.......")
                speak(query)
                speak("in google")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif "youtube" in query:
                query = query.replace(" jarvis", "")
                query = query.replace("youtube", "")
                speak("searching sir.......")
                speak(query)
                speak("here's what I found on YOUTUBE SIR")
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            elif "wikipedia" in query:
                query = query.replace(" jarvis", "")
                query = query.replace("wikipedia", "")
                query = query.replace(" on wikipedia", "")
                query = query.replace("search", "")
                speak(f"searching {query} this on wikipedia sir ......")
                results = wikipedia.summary(query,sentences = 2)
                speak("here are the results sir")
                print(results)
                speak(results)
            elif "incognito" in query:
                query = query.replace(" jarvis", "")
                query = query.replace("search", "")
                query = query.replace("incognito", "")
                speak("searching sir.......")
                speak(query)
                speak("in chrome on incognito sir")
                webbrowser.open(f"https://in.search.yahoo.com/search?fr=mcafee&type=E211IN714G0&p={query}")
           
            elif " finally sleep " in query:
                speak("going to sleep sir ")
                exit()
          
                
            
               

           


           

           

        

        
 
