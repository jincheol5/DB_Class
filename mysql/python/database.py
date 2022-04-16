
import pymysql
from config import db_name,db_user,db_pw,db_host,db_table 


class database:
    

    #기본형태 : cursor.execute("SQL 실행문")

    #connect -> create cursor 까지
    def __init__(self):
        self.db=db_name
        self.user=db_user
        self.pw=db_pw
        self.host=db_host
        

    #connect
    def connect(self):
        self.conn=pymysql.connect(host=self.host,user=self.user,password=self.pw,db=self.db,charset='utf8')
        self.cursor=self.conn.cursor()

    #connect out 
    def connect_out(self):
        self.conn.close()

        
    #create table
    def create_table(self,table_name):
        sql="create table if not exists "+table_name+" (id int)"
        self.cursor.execute(sql)
        self.conn.commit() #save
    ##overloading create table 
    
        
    #insert into table
    def insert_into_table(self,table_name,user_id,user_name):
        sql="insert into "+ table_name+" (user_id,user_name) values (" + "'"+user_id+"','"+user_name+"')"
        self.cursor.execute(sql)
        self.conn.commit() #save
    ##overloading insert to table 

    #delete table
    def delete_table(self,table_name):
        sql="delete "+table_name
        self.cursor.execute(sql)
        self.conn.commit() #save
    ##overloading delete table 
    
    #drop table
    def drop_table(self,table_name):
        sql="drop table "+table_name
        self.cursor.execute(sql)
        self.conn.commit() #save
    ##overloading drop table 
        
    
    #select all from table 
    def print_all_table(self,table_name):
        sql="select * from "+table_name
        self.cursor.execute(sql)
        
        rows=self.cursor.fetchall() #result list
        for row in rows:
            print(row)
    ##overloading select 

        

        
    