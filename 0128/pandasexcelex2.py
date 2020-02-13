'''
Created on 2020. 1. 28.

@author: gd7
pandasexcelex2.py : Customer Name 컬럼의 값이 J로 시작하는 행만 선택하여 pandas_output2.xls 파일로 생성하기
'''
import pandas as pd

input_file = "sales_2015.xlsx"
output_file = "pandas_output.xls"
data_frame = pd.read_excel\
            (input_file,"janary_2015",index_col=None)
#data_frame_value : 조건에 맞는 데이터 저장
data_frame_value = \
      data_frame[data_frame['Customer Name'].str.startswith("J")]
writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel(writer,sheet_name="jan_15_output",index=False)
writer.save()