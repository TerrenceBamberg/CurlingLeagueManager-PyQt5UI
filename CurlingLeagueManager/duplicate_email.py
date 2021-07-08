class DuplicateEmail(Exception):
    def __init__(self, email):
        self._email = email
