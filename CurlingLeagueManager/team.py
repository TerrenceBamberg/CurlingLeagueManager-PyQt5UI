from CurlingLeagueManager.identifiedObject import IdentifiedObject
#from emailer import Emailer
from CurlingLeagueManager.duplicate_oid import DuplicateOid
from CurlingLeagueManager.duplicate_email import DuplicateEmail
#from team_member import TeamMember


class Team(IdentifiedObject):

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._members = []

    @property
    def members(self):
        return self._members

    def add_member(self, member):
        if member in self._members:
            raise DuplicateOid(member.oid)
        for x in range(len(self._members)):
            if member.email == self._members[x].email:
                raise DuplicateEmail(member.email)
        self._members.append(member)

    def remove_member(self, member):
        if member in self._members:
            self._members.remove(member)

    def send_email(self, emailer, subject, message):
        emailer._recipients = []
        for x in self.members:
            emailer._recipients.append(x.email)
        emailer.send_plain_email(emailer._recipients, subject, message)

    def get__members(self):
        return self._members

    def __str__(self):
        return f"Team {self.name}: {len(self._members)} members"

