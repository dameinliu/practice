import csv
#引用csv模块。

'''
# 在.csv文件中写入数据
'''
# csv_file = open('demo.csv','w',newline='',encoding='utf-8')
# #调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
# writer = csv.writer(csv_file)
# # 用csv.writer()函数创建一个writer对象。

# writer.writerow(['电影','豆瓣评分'])
# writer.writerow(['银河护卫队','8.0'])
# writer.writerow(['复仇者联盟','8.1'])

# csv_file.close()


'''
# 读取.csv数据
'''
csv_file = open('demo.csv','r',newline='',encoding='utf-8')
reader = csv.reader(csv_file)
for row in reader:
    print(row)