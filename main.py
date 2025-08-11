import json
from core.speech_to_text import listen#have to make this lol
from core.text_to_speech import speak#have to make this lol
from core.commands_parser import parse_command#have to make this lol
import sys

CONFIG_PATH = "data/config.json"

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

ASSISTANT_NAME = config.get('name')
USER_NAME = config.get('your_name')
EXIT_WORDS = config.get('exit_words')


def main():
    
    speak(f"Hey {USER_NAME}, how can I help you today?")

    while True:
        try:
            command = listen().lower()

            if not command:
                continue

            for keyword in EXIT_WORDS:
                if keyword in command:
                    speak(f"Goodbye {USER_NAME}!")

            response = parse_command(command)
            speak(response)

        except KeyboardInterrupt:
            speak(f"Stopping {ASSISTANT_NAME}!")
            sys.exit()


if __name__ == "__main__":
    main()
