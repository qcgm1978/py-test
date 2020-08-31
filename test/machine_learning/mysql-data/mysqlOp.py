from functools import reduce
import mysql.connector
class MysqlOp(object):
    def __init__(self, table):
        self.table=table
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test@2018",
        database="mydatabase"
        )
        self.mycursor = self.mydb.cursor(buffered=True)
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
        alter = '''
    ALTER TABLE customers  
    ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY
'''
        self.mycursor.execute(alter)
    def insertInto(self,sql,val):
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    def executemany(self,val):
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        self.mycursor.executemany(sql, val)
        self.mydb.commit()
    def select(self):
        self.mycursor.execute("SELECT * FROM {0}".format(self.table))
        myresult = self.mycursor.fetchall()
        return myresult
    def selectColumns(self, cols):
        s=reduce(lambda acc,item:acc+', '+item,cols)
        self.mycursor.execute("SELECT {0} FROM customers".format(s))
        return self.mycursor.fetchall()
    def fetchOne(self):
        self.mycursor.execute("SELECT * FROM {0}".format(self.table))
        return self.mycursor.fetchone()