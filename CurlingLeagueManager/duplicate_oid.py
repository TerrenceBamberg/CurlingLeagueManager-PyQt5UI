class DuplicateOid(Exception):
    def __init__(self, oid):
        self._oid = oid
