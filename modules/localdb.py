from modules.database import *
import config
class db: 
    def __init__(self):
        pass
    def get(self):
        database=conn()
        database.sethost(localdb["host"])
        database.setname(localdb["name"])
        database.setuser(localdb["user"])
        database.setpass(localdb["pass"])
        db.query("""SELECT * FROM pro
         WHERE price < 5""")
    def set(self):
        pass

class probeshell:
    def __init__(self):
        pass
    def run(self):
        pass
    