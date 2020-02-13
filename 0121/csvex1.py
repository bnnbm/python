'''
Created on 2020. 1. 21.

@author: gd7
csvex1.py : csv 파일 읽기
'''
import sys # command 라인에서 입력값 받기
input_file = sys.argv[1] # jeju1.csv
output_file = sys.argv[2] #jeju1_bak.csv
with open(input_file,'r',newline="") as filereader :
    with open(output_file, 'w',newline="") as filewriter :
        header = filereader.readline()
        print(type(header))
        header = header.strip()
        print(header)
        header_list = header.split(",")
        print(header_list)
        filewriter.write(",".join(map(str, header_list)) + "\r\n")
        for row_list in filereader :
            print(type(row_list))
            filewriter.write(row_list)
#            filewriter.write("".join(map(str,row_list)))