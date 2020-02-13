'''
Created on 2020. 1. 17.

@author: gd7
dbex1.py : sqlite db 사용하기
'''
import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)
cur = conn.cursor() #sql 구문 전달하는 객체
cur.executescript('''
   drop table if exists items;
   create table items (item_id integer primay key,
      name text unique,
      price integer);
   insert into items (name, price) values ('Apple',800);
   insert into items (name, price) values ('Orange',500);
   insert into items (name, price) values ('Banana',300);
''')
conn.commit() #transaction 종료
cur = conn.cursor()
cur.execute("select item_id,name,price from items")
item_list = cur.fetchall() #모든 레코드 리턴
print(item_list)
for it in item_list :
    print(it)