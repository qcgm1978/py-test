import mysql.connector
class MysqlOp(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test@2018",
        database="mydatabase"
        )
        self.mycursor = self.mydb.cursor()
    def __del__(self):
        self.mycursor.close()
        self.mydb.close()
    def showTables(self):
        self.mycursor.execute("SHOW TABLES")
    def createTable(self):
        self.mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    def createPrimaryKey(self):
        self.mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    def alterTable(self):
        self.mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
