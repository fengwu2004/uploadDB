from typing import Dict, List
from data.codeInfo import CodeInfo

class BlockInfo(object):

    def __init__(self):

        super().__init__()

        self.name = ""

        self.codeList:List[CodeInfo] = []

    def createCodeList(self, items:List):

        for item in items:

            codeInfo = CodeInfo(code=item["code"], name=item["name"])

            self.codeList.append(codeInfo)
              
    def createFromJson(self, name:str, items:List):

        self.name = name

        self.createCodeList(items)

    def toJson(self):

        codeList = []

        for code in self.codeList:

            codeList.append({"name":code.name, "code":code.code})

        return {"name":self.name, "codeList":codeList}