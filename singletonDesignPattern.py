import MySQLdb

class DBConnection(object):
    connection = None
    def getConnection (self):
        if self.connection == None:
            self.connection = MySQLdb.connect(host="localhost", user="root", password="password", database="blogPostdb")
        return self.connection 
            