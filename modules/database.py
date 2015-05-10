import _mysql
class conn:
    dbhost="" 
    dbname=""
    dbuser=""
    dbpass=""
    def __init__(self):
        pass
    def connect(self):
        database=_mysql.connect(host=self.dbhost, user=self.dbuser,
                  passwd=self.dbpass,db=self.dbname)
        return database
    def sethost(self,db):
        pass
    def setname(self,db):
        pass
    def setuser(self,db):
        pass
    def setpass(self,db):
        pass
database=conn()