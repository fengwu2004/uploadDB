class CodeInfo(object):

    def __init__(self, code="", name=""):

        super().__init__()

        self.name = name

        self.code = code

    def isST(self):

        if "ST" in self.name:

            return True

        return False

    def isSTIB(self):

        if "688" not in self.code:

            return False

        if self.code.index("688") == 0:

            return True

        return False

    def __eq__(self, value):

        return self.code == value.code

    def toJson(self):

        return {"name":self.name, "code":self.code}