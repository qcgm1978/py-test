from functools import reduce
import mysql.connector
class MysqlOp(object):
    def __init__(self, table,cols=None,val=None):
        self.table = table
        self.mydb = mysql.connector.connect(
            host="localhost", user="root", password="test@2018", database="mydatabase"
        )
        self.mycursor = self.mydb.cursor(buffered=True)
        if isinstance(cols,dict):
            self.createTable(cols)
            self.fields = cols
            self.fields.pop('id',None)
            if isinstance(val,list):
                self.executemany(val)
        elif isinstance(cols,list):
            fields=cols[0]
            if isinstance(fields,dict):
                d=self.getFields(fields)
                self.fields = d
                self.fields.pop('id',None)
                self.createTable(d)
                self.executemany(cols)
    def __del__(self):
        self.mycursor.close()
        self.mydb.close()
    def getFields(self,d):
        r={}
        for key,val in d.items():
            if isinstance(val,int):
                r[key]='INT'
            elif isinstance(val,str):
                r[key]='VARCHAR(255)'
        return r
    def showTables(self):
        self.mycursor.execute("SHOW TABLES")
    def createTable(self,d):
        def getKey(acc,key):
            if key=='id':
                return acc
            else:    
                return acc+"{0} {1},".format(key, d[key])
        s=reduce(getKey, d, "")
        self.mycursor.execute(
            "CREATE TABLE IF NOT EXISTS {0} ({1})".format(self.table,s[:-1])
        )
    def createPrimaryKey(self):
        self.mycursor.execute(
            "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
        )
    def addPrimaryKey(self):
        alter = """
    ALTER TABLE {0}  
    ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY
""".format(self.table)
        self.mycursor.execute(alter)
    def insertInto(self, sql, val):
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            return 1
        except mysql.connector.errors.IntegrityError:
            return 0
    def executemany(self, val):
        def removeId(item):
            isinstance(item,dict) and item.pop('id',None)
            return item
        val=list(map(removeId,val))
        s=','.join(self.fields.keys())
        placeholder=', '.join(['%s']*len(self.fields))
        sql = "INSERT INTO {2} ({0}) VALUES ({1})".format(s,placeholder,self.table)
        try:
            vals=list(map(lambda item:tuple(item.values()) if isinstance(item,dict) else item,val))
            self.mycursor.executemany(sql, vals)
            self.mydb.commit()
            return 1
        except mysql.connector.errors.IntegrityError:
            return 0
    def select(self ,limit=None,offset=None):
        o='OFFSET '+str(offset) if offset else ''
        s='LIMIT '+str(limit) if limit else ''
        self.mycursor.execute("SELECT * FROM {0} {1} {2}".format(self.table,s,o))
        myresult = self.mycursor.fetchall()
        return myresult
    def getRowsCount(self):
        self.select()
        return self.mycursor.rowcount
    def selectColumns(self, cols):
        s = reduce(lambda acc, item: acc + ", " + item, cols)
        self.mycursor.execute("SELECT {0} FROM customers".format(s))
        return self.mycursor.fetchall()
    def fetchOne(self):
        self.mycursor.execute("SELECT * FROM {0}".format(self.table))
        return self.mycursor.fetchone()
    def where(self, d,offset=0):
        s = reduce(lambda acc, key: "{0} = '{1}'".format(key, d[key]), d, "")
        sql = "SELECT * FROM customers WHERE {0}".format(s)
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    def ignore(self, colName):
        sql = """delete from {0} 
where ID in (
select * from (select ID from {0} where ID not in (
select max(ID) from {0} group by {1}
) ORDER BY ID
) AS p
)""".format(
            self.table, colName
        )
        self.mycursor.execute(sql)
    def unique(self, colName):
        self.ignore(colName)
        sql = "ALTER  TABLE {0} ADD UNIQUE unique_index  ({1})".format(
            self.table, colName
        )
        try:
            self.mycursor.execute(sql)
        except mysql.connector.errors.ProgrammingError:
            return None
    def wild(self, d):
        s = self.getStr(d,'LIKE',True)
        sql = "SELECT * FROM {0} WHERE {1}".format(self.table, s)
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    def getStr(self, d,relation=' ',isWild=False):
        s='%' if isWild else ''
        return reduce(lambda acc, key: "{0} {2} '{3}{1}{3}'".format(key, d[key],relation,s), d, "")
    def escape(self, adr, field="address"):
        sql = "SELECT * FROM {0} WHERE {1} = %s".format(self.table, field)
        self.mycursor.execute(sql, adr)
        return self.mycursor.fetchall()
    def sort(self, field, isDESC=False):
        sql = "SELECT * FROM {0} ORDER BY {1} {2}".format(
            self.table, field, "DESC" if isDESC else ""
        )
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    def delete(self,d):
        s=reduce(lambda acc, key: "{0} = %s".format(key),d, "")
        sql = "DELETE FROM {0} WHERE {1}".format(self.table,s)
        self.mycursor.execute(sql,tuple(d.values()))
        self.mydb.commit()
        return self.mycursor.rowcount
    def dropTable(self,l=None):
        if l is None:
            l=[self.table]
        for val in l:
            sql = "DROP TABLE  IF EXISTS  {0}".format(val)
            self.mycursor.execute(sql)
        return True
    def updateField(self,d):
        sql = "UPDATE {0} SET {1} = %s WHERE {1} = %s".format(self.table,d['field'])
        self.mycursor.execute(sql,(d['to'],d['from']))
        self.mydb.commit()
        return self.mycursor.rowcount