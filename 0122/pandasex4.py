'''
Created on 2020. 1. 22.

@author: gd7
pandasex4.py : pandas 모듈을 사용하여 column 조회하기
'''
import pandas as pd
input_file = "supplier_data.csv"
output_file = "pandas_out3.csv"

df = pd.read_csv(input_file)
df_col = df.iloc[:,[0,3]] #0번열과 3번열 조회
print("=====df.iloc[:,[0,3]]===")
print(df_col)
df_col = df.iloc[0:4,0:3]
print("=====ff.iloc[0:4,0:3]===")
print(df_col)
#모든 행의 Invoice Number, Cost 컬럼 조회
df_col = df.loc[:,["Invoice Number","Cost"]]
#Invoice Number의 값이 920- 시작하는 행의
#Invoice Number, Cost 컬럼 조회
df_col = df.loc[df["Invoice Number"].
        str.startswith("920-"),["Invoice Number","Cost"]]
df_col.to_csv(output_file, index=False)