import keyring
import yagmail


class Emailer:
    _sole_instance = None
    sender_address = ''

    def __init__(self):
        self._recipients = []
        self.subject = None
        self.message = None

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def configure(cls, sender_address):
        cls.sender_address = sender_address

    def send_plain_email(self, recipients, subject, message):
        yag = yagmail.SMTP(self.sender_address, keyring.get_password('gmail.com', self.sender_address))
        self._recipients = recipients
        self.subject = subject
        self.message = message
        for r in recipients:
            yag.send(r, subject, message)
        return f"Sending email to: {self._recipients}"




