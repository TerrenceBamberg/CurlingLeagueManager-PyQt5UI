from CurlingLeagueManager.identifiedObject import IdentifiedObject
#from team import Team
#from competition import Competition
#from team_member import TeamMember
from CurlingLeagueManager.duplicate_oid import DuplicateOid


class League(IdentifiedObject):
    _teams = []
    _competitions = []

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name


    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self._competitions

    def add_team(self, team):
        if team in self._teams:
            raise DuplicateOid(team.oid)
        self._teams.append(team)


    def add_competition(self, competition):
        if competition in self._competitions:
            raise DuplicateOid(competition.oid)
        self._competitions.append(competition)

    def teams_for_member(self, member):
        teams_for_player = []
        for team in self._teams:
            for player in team.members:
                if player == member:
                    teams_for_player.append(team)
        return teams_for_player

    def competitions_for_team(self, team):
        # return a list of all competitions in which team is participating
        competitions_for_team = []
        for comp in self._competitions:
            for t in comp.teams_competing:
                if t == team:
                    competitions_for_team.append(comp)
        return competitions_for_team

    def competitions_for_member(self, member):
        # return a list of all competitions for which member played on one of the competing teams
        competitions_for_member = []
        for comp in self._competitions:
            for t in comp.teams_competing:
                if member in t.members:
                    competitions_for_member.append(comp)
        return competitions_for_member

    def __str__(self):
        return f"League {self.name}: {len(self._teams)} teams,  {len(self._competitions)} competitions"
