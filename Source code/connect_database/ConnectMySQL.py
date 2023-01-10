from mysql.connector import connect

class ConnectDatabase:
    def __init__(self,user='root',password='',database=''):
        self.mydb=connect(
            host="localhost",
            user=user,
            password=password,
            database=database
        )
    
    def select(self,sql_query):
        cursor=self.mydb.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

    def idu(self,sql_query):
        '''insert,delete,update'''
        cursor=self.mydb.cursor()
        cursor.execute(sql_query)
        self.mydb.commit()
        