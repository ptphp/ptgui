#coding:utf-8
'''
Created on Sep 25, 2012

@author: joseph
'''
from app.utils.sqlitedb import SqliteDB
from app.utils.common import trace_back
import os

db = SqliteDB()
dbname = "test.db"
createtable_sql = """
        CREATE TABLE IF NOT EXISTS [test](
              [id] INTEGER PRIMARY KEY,              
              [name] TEXT,
              [age] INTEGER,
              UNIQUE([name]));
    """
droptable_sql = """
        DROP TABLE IF  EXISTS [test];
    """
    
div = "*" * 60

def test_open():
    print div,"test open db"
    db.open(dbname)
    if os.path.exists(os.path.abspath(dbname)):
        print os.path.abspath(dbname)+u'已生成'
    #db.query(droptable_sql)
    #db.query(createtable_sql)

def test_deleteDB():
    print div,"test del db"
    db.deleteDb(dbname)
    if os.path.exists(os.path.abspath(dbname)) == False:
        print os.path.abspath(dbname)+u'已删除'


def test_query():
    print div,"test query method"
    print u"删除 Table test"
    db.query(droptable_sql)
    print u"生成 Tabel test"
    db.query(createtable_sql)    


def test_insert(name):
    print div,u"测试插入数据库方法"
    param = {}
    param['name'] = name
    param['age'] = 69
    sql,_param = db.parseInsert("test", param)
    print "sql : "+sql
    print "param : "+ str(_param)
    
    id = db.insert("test", param)
    print "insert id is :%d "  % id


def test_getAll():
    print div,"test getALL()"
    db.query("select * from test")
    print db.getAll()


def test_getOne(id):
    print div,"test getOne()"
    sql = "select * from test where id = %d" % id
    print sql
    db.query(sql)
    print db.getOne()


def test_update(id):
    print div,"test update()"
    param = {}
    param['name'] = "george"
    param['age'] = 99
    condition = {}
    condition['id'] = id
    
    print db.where(condition) 
    sql,pp = db.parseUpdate("test", param, condition)
    print sql
    print pp
        
    db.update("test", param, condition)
    
def main():
    try:
        test_open()
        test_query()
        test_insert("joseph")
        test_insert("lisa")
        
        test_getAll()
        test_getOne(2)
        test_update(2)
        test_getOne(2)
        
        test_deleteDB() 
               
    except:
        print trace_back()    

if __name__ == "__main__":
    main()
