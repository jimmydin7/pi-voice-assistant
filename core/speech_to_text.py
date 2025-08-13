import speech_recognition as sr
from logs import logger

def listen(timeout_seconds: float = 5.0, phrase_time_limit_seconds: float = 10.0) -> str:
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logger.log('calibrating mic for ambient noise', 'info')
            recognizer.adjust_for_ambient_noise(source, duration=0.6)
            logger.log('listening...', 'info')
            audio = recognizer.listen(
                source,
                timeout=timeout_seconds,
                phrase_time_limit=phrase_time_limit_seconds
            )
    except sr.WaitTimeoutError:
        logger.log('listen timeout: no speech detected', 'warning')
        return ""
    except Exception as exc:
        logger.log(f'error accessing microphone: {exc}', 'error')
        return ""

    try:
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        logger.log('speech not recognized', 'warning')
        return ""
    except sr.RequestError as exc:
        logger.log(f'speech recognition service error: {exc}', 'error')
        return ""
