'''
Created on 2020. 2. 10.

@author: gd7
jsonex2.py : json 내용에서 날짜와 과일의 가격을 화면에 출력하고, 파일에 저장하기
'''
import json
price = {
    "data" : "2020-02-10",
    "price" : {
        "Apple" : 800,
        "Orange" : 1000,
        "Banana" : 500
        }
}
print("날짜: ",price["data"])
for p in price["price"].keys() :
    print("%s => %s " % (p, price["price"][p]))
s = json.dump(price,open("json_output2.json","w"))
