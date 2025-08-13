import random
from logs import logger


HELLO_MSG_PATH = "data/hello.txt"

def hello_msg(list_or_get: str):
    with open(HELLO_MSG_PATH, 'r') as f:
        hello_messages = f.read().splitlines()

    if list_or_get == 'list':
        return hello_messages
    elif list_or_get == 'get':
        return random.choice(hello_messages)
    else:
        return hello_messages


def parse_command(prompt: str, welcome_list_random: str) -> str:
    list_hello_messages = hello_msg('list')

    if prompt in list_hello_messages:
        logger.log('greeting detected', 'info')
        return welcome_list_random

    logger.log('command not recognized by parser', 'warning')
    return ""
