from modules.database import *
import config
from config import localdb
class probe: 
    def __init__(self):
        pass
    def get(self):
        global localdb
        database=conn()
        database.sethost(localdb["host"])
        database.setname(localdb["name"])
        database.setuser(localdb["user"])
        database.setpass(localdb["pass"])
    def set(self):
        pass

class probeshell:
    def __init__(self):
        pass
    def run(self):
        pass
    