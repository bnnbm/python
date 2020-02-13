'''
Created on 2020. 2. 13.

@author: gd7
learnirisex2.py : pandas를 이용하여 학습데이터와 테스트 데이터 분류하기
'''
import pandas as pd
from sklearn import svm,metrics
#학습데이터, 테스트 데이터 분류하기 위한 모듈
from sklearn.model_selection import train_test_split
csv = pd.read_csv("iris.csv")
csv_data = csv[["SepalLength","SepalWidth",
                "PetalLength","PetalWidth"]] #기본데이터부분
#붓꽃의 이름 저장
csv_label = csv["Name"] #정답부분, 결과부분
#train_data : 학습데이터
#test_data : 평가데이터
#train_label :학습데이터의 정답
#test_label : 학습데이터의 정답
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data,csv_label,test_size=0.3)
print(len(train_data),len(test_data),)
clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label,pre)
print("정답률=",ac_score)