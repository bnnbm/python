'''
Created on 2020. 1. 15.

@author: gd7
lottoex.py : 로또번호 생성기
'''
import random
def getNumber() :
    return random.randrange(1,46)
lotto = set()
while len(lotto) < 6 :
#    lotto.add(random.randrange(1,46))
     lotto.add(getNumber())
print("추첨된 로또 번호=>",sorted(lotto))