import pyttsx3

engine = pyttsx3.init()



def speak(text, rate, volume):

    if not text:
        return

    engine.setProperty("rate", rate)  
    engine.setProperty("volume", volume) 
    
    engine.say(text)
    engine.runAndWait()
