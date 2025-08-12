import json
from core.speech_to_text import listen
from core.text_to_speech import speak#
from core.commands_parser import parse_command
import sys
import random
from logs import logger

CONFIG_PATH = "data/config.json"
WELCOME_MSG_PATH = "data/welcome.txt"


try:
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)

    logger.log('info', 'loaded config file')
except Exception:
    logger.log('error', 'could not load config file. check data/config.json')


ASSISTANT_NAME = config.get('name')
USER_NAME = config.get('your_name')
EXIT_WORDS = config.get('exit_words')
ENGINE_RATE = config.get('voice_engine_rate')
ENGINE_VOLUME = config.get('voice_engine_volume')


def load_welcome_message():
    try:
        with open(WELCOME_MSG_PATH, 'r') as f:
            welcome_messages = f.read().splitlines()
            welcome_messages = [msg.replace('_USER_', USER_NAME) for msg in welcome_messages]
            return random.choice(welcome_messages)

        logger.log('info', 'loaded welcome messages')
    except Exception:
        logger.log('error', 'could not load welecome messages. check data/welcome.txt')

def main():
    
    speak(load_welcome_message(), rate=ENGINE_RATE, volume=ENGINE_VOLUME)

    while True:
        try:
            command = listen().lower()

            if not command:
                continue

            for keyword in EXIT_WORDS:
                if keyword in command:
                    speak(f"Goodbye {USER_NAME}!", rate=ENGINE_RATE, volume=ENGINE_VOLUME)

            response = parse_command(command, load_welcome_message())
            speak(response)

        except KeyboardInterrupt:
            speak(f"Stopping {ASSISTANT_NAME}!")
            sys.exit()


if __name__ == "__main__":
    main()
