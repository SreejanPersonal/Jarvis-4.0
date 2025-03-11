# jarvis/communication/contact_manager.py
# Contact profiles
class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email):
        self.contacts[name] = email

    def get_contact(self, name):
        return self.contacts.get(name)
