'''
workbook    工作簿
worksheet   工作表
cell        单元格
'''

import openpyxl

# 打开工作簿
woekbook = openpyxl.load_workbook(r'selenium\ranzhi\data.xlsx')
# 获取指定的工作表
login_success = woekbook['login_success']
# l=[]
# for row in login_success:
#     # print(row)
#     t=[]
#     for cell in row:
#         # print(cell.value)
#         t.append(cell.value)
#     l.append(tuple(t))

l =[tuple(cell.value for cell in row) for row in login_success]
print(l)
