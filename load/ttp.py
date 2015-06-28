# holder class to hold Term and TypeId
class TermTypePair:

    def __init__(self, term = "", typeId = ""):
        self.term = term
        self.typeId = typeId

    def getTerm(self):
        return self.term

    def getTypeId(self):
        return self.typeId
