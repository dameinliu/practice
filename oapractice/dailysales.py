'''
# V1.0
# author: @dameinliu, github:dameinliu
# 统计销售额脚本
# 将text文件转化为xlsx
'''
import sys, os
import pandas as pd

# 需要统计的产品asin
my_asins = ['B01N76O2E9','B079P1X8H8','B07J4ZQDY4','B07ZTDFKLK','B078B7WT3R','B071H2YTQ9','B071H2YTQ9','B07QCSGQPV','B079M3W46N','B079MHVMKJ','B079LZXDWV','B07D32FNDZ','B07BN8JZJP','B07MVZMM7Z','B07DZS6J5P','B07DZR15FG','B07JB9NF24','B07VC8NN92','B07VJNQV4T','B07W3M4VGS','B07YV8LYZN','B07W3LF4HR','B07YV8LYZN',]

# 功能函数，分组并计算销售额
# 需要传入一个参数：filename, 文件路径
def calculate_sales(filename): 
    wb = pd.read_csv(filename, '\t')

    all_sales = wb.iloc[:,[12,15,17]].groupby('asin').sum()
    all_sales = all_sales.reset_index()
    my_sales = all_sales[all_sales['asin'].isin(my_asins)]

    print(my_sales)
    print('==========')
    print(my_sales['quantity'].sum())
    print(my_sales['item-price'].sum())
    
    os.remove(filename)

if __name__=='__main__':
    try:
        filename = sys.argv[1]
        calculate_sales(filename)
    except Exception as e:
        print(sys.argv)
        print(e)