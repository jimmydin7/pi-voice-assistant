#twillio api texting
#no this isnt my moms real number btw

import json

contacts_path = '../data/contacts.json'

def read_contacts():
    with open(contacts_path, 'r') as f:
        return json.load(f) 
    

def check_if_contact_exists(contact):
    contacts = read_contacts()

    for name in contacts: 
        if name == contact:
            return True
    return False


def text(contact):

    if check_if_contact_exists(contact):
        print(f"contact exists! ({contact})")
    else:
        print(f"invalid contact ({contact})")

text('mum')
text('dljsakdhaskjdhsaj')
