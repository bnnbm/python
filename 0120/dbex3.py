'''
Created on 2020. 1. 20.

@author: gd7
'''
import pymysql # pip install pymysql 실행하기
conn = pymysql.connect(host="localhost", port=3306,
                       user="scott",passwd="1234",
                       db="classdb", charset="utf8")
try :
    cur = conn.cursor()
    cur.execute("select * from item")
    while True :
        row = cur.fetchone() #1건의 레코드만 조회
        if row == None :
            break
        print(row)
finally : 
    cur.close()
    conn.close()