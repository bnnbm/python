'''
Created on 2020. 1. 10.

@author: gd7
distionaryex3.py : 딕셔너리 예제3
'''
import operator
dic,list = {},[]
dic={"Thomas":"토마스","Edwrd":"에드워드","Henry":"헨리","Gothen":"고든","James":"제임스"}
list = sorted(dic.items(),key=operator.itemgetter(0),reverse=True) #거꾸로 정렬
print(list)
list = sorted(dic.items(),key=operator.itemgetter(1)) #한글순서로 정렬
print(list)