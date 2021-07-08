class IdentifiedObject:

    def __init__(self, _oid):
        self._oid = _oid

    @property
    def oid(self):
        return self._oid

    def __eq__(self, other):
        return self._oid == other.oid

    def __hash__(self):
        return hash(self._oid)



