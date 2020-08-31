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
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            return 1
        except mysql.connector.errors.IntegrityError:
            return 0
    def executemany(self,val):
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        try:
            self.mycursor.executemany(sql, val)
            self.mydb.commit()
            return 1
        except mysql.connector.errors.IntegrityError:
            return 0
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
    def where(self,d):
        s=reduce(lambda acc,key:"{0} = '{1}'".format(key,d[key]),d,'')
        sql = "SELECT * FROM customers WHERE {0}".format(s) 
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    def ignore(self,colName):
        sql='''delete from {0} 
where ID in (
select * from (select ID from {0} where ID not in (
select max(ID) from {0} group by {1}
) ORDER BY ID
) AS p
)'''.format(self.table,colName)
        self.mycursor.execute(sql)
    def unique(self,colName):
        self.ignore(colName)
        sql = "ALTER  TABLE {0} ADD UNIQUE unique_index  ({1})".format(self.table,colName)
        try:
            self.mycursor.execute(sql)
        except mysql.connector.errors.ProgrammingError:
            return None