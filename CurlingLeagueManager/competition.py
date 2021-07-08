from identifiedObject import IdentifiedObject
from team import Team
from datetime import datetime
from emailer import Emailer
from team_member import TeamMember


class Competition(IdentifiedObject):
    teams = []

    def __init__(self, oid, teams, location, date_time):
        super().__init__(oid)
        self._teams_competing = teams
        self.location = location
        self.date_time = date_time

    @property
    def teams_competing(self):
        return self._teams_competing

    def send_email(self, emailer, subject, message):
        emailer._recipients = []
        for x in self._teams_competing:
            for y in x.members:
                emailer._recipients.append(y.email)
        emailer.send_plain_email(emailer._recipients, subject, message)

    def __str__(self):
        if self.date_time is None:
            return f"Competition at {self.location} with {len(self._teams_competing)} teams"
        return f"Competition at {self.location} on {self.date_time} with {len(self._teams_competing)} teams"


