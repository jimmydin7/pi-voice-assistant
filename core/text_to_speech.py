import pyttsx3

engine = pyttsx3.init()



def speak(text, rate, volume):

    if not text:
        return

    engine.setProperty("rate", 170)  
    engine.setProperty("volume", 1.0) 
    
    engine.say(text)
    engine.runAndWait()
