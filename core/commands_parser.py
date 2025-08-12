import random


HELLO_MSG_PATH = "../data/hello.txt"

def hello_msg(list_or_get):

    with open(HELLO_MSG_PATH, 'r') as f:
        hello_messages = f.read().splitlines()

    if list_or_get == 'list':
        return hello_messages
    
    elif list_or_get == 'get':
        return random.choice(list_or_get)
    

def parse_command(prompt, welcome_list_random):
    list_hello_messages = hello_msg('list')

    if prompt in list_hello_messages:
        greeting = welcome_list_random
