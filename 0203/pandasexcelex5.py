'''
Created on 2020. 2. 3.

@author: gd7
pandasexcelex5.py : 모든 sheet 조회하기
'''
import pandas as pd
input_file = "sales_2013.xlsx"
output_file = "pandas_output5.xls"
data_frame = pd.read_excel\
         (input_file,sheetName=None,index_col=None)
row_output = []
#data_frame.items() : 모든 sheet를 선택
for worksheet_name, data in data_frame.items() :
    print("=====",worksheet_name,"=====")
    row_output.append(data[data['Sale Amount'].
 replace('$','').replace(',','').astype(float) > 2000.0])
    
filtered_row = pd.concat\
                (row_output,axis=0,ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_row.to_excel\
   (writer,sheet_name="sale_amount_gt2000",index=False)
writer.save()