from pymongo import MongoClient

_instance = None

_debug = False

class DatabaseMgr(object):

    @classmethod
    def instance(cls):

        global _instance

        if _instance is None:

            _instance = DatabaseMgr()

        return _instance
    
    def __init__(self):

        uri = "mongodb://172.28.221.110:27017/recommond?"
        
        self.client = MongoClient(uri)

        self.db = self.client["recommond"]

    @property
    def stocks(self):
        
        return self.db['stocks']

    @property
    def block(self):
        
        return self.db['block']

    @property
    def capitals(self):
        
        return self.db['capitals']

    @property
    def industry(self):

        return self.db['industry']

    @property
    def stockInfos(self):
        
        return self.db['stockinfo']

    def stockvolumof(self, dt:str):

        return self.db[dt]

    @property
    def users(self):
        
        return self.db['users']