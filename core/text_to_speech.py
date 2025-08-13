import pyttsx3
from logs import logger


engine = pyttsx3.init()



def speak(text, rate, volume):

    if not text:
        return

    engine.setProperty("rate", rate)  
    engine.setProperty("volume", volume) 
    
    engine.say(text)
    logger.log(f'response generated: "{text}"', 'info')
    engine.runAndWait()
