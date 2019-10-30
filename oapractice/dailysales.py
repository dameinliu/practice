import openpyxl
import codecs
import pandas as pd
from openpyxl.utils import get_column_letter

'''
# 将text文件转化为xlsx
'''
my_asins = ['B07J9WL1VY','B079KFHHRC','B01N76O2E9','B079P1X8H8','B07J4ZQDY4','B078B7WT3R','B07QCSGQPV','B079M3W46N','B079MHVMKJ','B079LZXDWV','B07D32FNDZ','B07DZS6J5P','B07DZR15FG','B07FKD3J2Q','B07DC2R4XW','B07DC2R4XW','B01N68WJBF','B01N68WJBF','B079KTJT3C','B079KTJT3C','B079KVDJ77','B07JZNNW2J','B07M8LC6W7','B07SD4DWFH','B07DC2Z6LQ','B07D9D5DWW','B079P3YKG2','B07MQ53DJS','B07MQ53DJS','B079P2BM9L','B07MLW9KQX','B07MLW9KQX','B07MFTVMYD','B07MM1K2PW','B07T46SPCB','B01N012YWY','B06XDH2WH7','B0753GB557','B0753GT953','B01N9K49BG','B01NBE990M','B07JB9NF24','B07VC8NN92','B07VJNQV4T','B07W3LF4HR','B07W3M4VGS','B07WS8TDX6','B07XGB4HTF','B07X93JKQH','B07YKVJCMZ','B07WJ3WZ95','B07WK58MBH','B07YKSYCGW']

def txt_to_xlsx(filename,outfile): 
    fr = codecs.open(filename,'r')
    wb = openpyxl.Workbook()
    ws = wb.active
    # ws = wb.create_sheet()
    ws.title = 'orders'
    
    row = 0
    for line in fr:
        row +=1
        line = line.strip()
        line = line.split('\t')
        
        col = 0
        for j in range(len(line)):
            col +=1
            # print (line[j])
            ws.cell(column = col, row = row, value = line[j].format(get_column_letter(col)))
    
    wb.save(outfile)


def cal_sales(filename):
    wb = pd.read_excel(filename)
    all_sales = wb.iloc[:,[12,15,17]].groupby('asin').sum()
    all_sales = all_sales.reset_index()
    my_sales = all_sales[all_sales['asin'].isin(my_asins)]

    print(my_sales)
    print('==========')
    print(my_sales['quantity'].sum())
    print(my_sales['item-price'].sum())


'''
# #读取xlsx内容    
# def read_xlsx(filename):
#     #载入文件
#     wb = openpyxl.load_workbook(filename)
#     #获取Sheet1工作表
#     ws = wb.get_sheet_by_name('Sheet1')
#     #按行读取
#     for row in ws.rows:
#         for cell in row:
#             print (cell.value)
#     #按列读
#     for col in ws.columns:
#         for cell in col:
#             print (cell.value)
'''

if __name__=='__main__':
    inputfileTxt = 'orders.txt'
    outfileExcel = 'daily_sales.xlsx'
    txt_to_xlsx(inputfileTxt,outfileExcel)

    cal_sales(outfileExcel)
    # read_xlsx(outfileExcel)