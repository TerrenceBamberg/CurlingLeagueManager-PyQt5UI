import os
import csv
import pickle
from os import path


class LeagueDatabase:
    """writing instance for only one database"""
    sole_instance = None

    def __init__(self):
        self._last_oid = 0
        self._leagues = []

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def load_file(cls, file_name):
        try:
            file_in = open(file_name, 'rb')
            cls._sole_instance = pickle.load(file_in)
            file_in.close()
        except FileNotFoundError or Exception:
            print("Error. Please try again.")


    @property
    def leagues(self):
        return self._leagues

    def add_league(self, league):
        self._leagues.append(league)

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid

    def save(self, file_name):
        if not str(path.exists(file_name)):
            os.rename(file_name, file_name + ".backup")
            with open(file_name + ".backup") as f:
                pickle.dump(self, f)
                f.close()
        else:
            with open(file_name) as f:
                pickle.dump(self, f)
                f.close()

    def import_league(self, league_name, file_name):
        try:
            with open(file_name, mode='r', encoding='utf-8') as csvfile:
                self.add_league(league_name)
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    print(row)
        except Exception:
            print("Error importing leagues.")

    def export_league(self, league, file_name):
        try:
            with open(file_name, mode='w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Team name' , ' Member name' , ' Member email'])
                [writer.writerow([team.name, mem.name, mem.email]) for team in league.teams for mem in team.members]
                f.close()
        except Exception:
            print("Error exporting leagues.")
