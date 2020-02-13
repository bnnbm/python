'''
Created on 2020. 2. 10.

@author: gd7
jsonex3.py : 문자열 데이터를 json 파일로 파싱하여 결과 조회하기
'''
import json
str = '''{
    "data" : "2020-02-10",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
        }
}'''
#json.loads : 문자열 정보를 json 파일로 파싱.
price = json.loads(str)
print("날짜: ",price["data"])
for p in price["price"].keys() :
    print("%s => %s " % (p, price["price"][p]))
s = json.dump(price,open("json_output2.json","w"))
