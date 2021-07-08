from identifiedObject import IdentifiedObject
from emailer import Emailer



class TeamMember(IdentifiedObject):
    def __init__(self, oid, name, email):
        super().__init__(oid)
        self.name = name
        self.email = email

    def send_email(self, emailer, subject, message):
        emailer._recipients = []
        emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        return f"{self.name}<{self.email}>"