import requests, openpyxl
# 引用requests模块

'''
# 爬取歌曲评论页面
'''
# for i in range(5):
# 	res_comments = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum='+str(i)+'&pagesize=15&lasthotcommentid=song_102065756_3202544866_44059185&domain=qq.com&ct=24&cv=10101010')
# 	# 调用get方法，下载评论列表
# 	json_comments = res_comments.json()
# 	# 使用json()方法，将response对象，转为列表/字典
# 	list_comments = json_comments['comment']['commentlist']
# 	# 一层一层地取字典，获取评论列表
# 	for comment in list_comments:
# 	# list_comments是一个列表，comment是它里面的元素
# 	    print(comment['rootcommentcontent'])
# 	    # 输出评论
# 	    print('-----------------------------------')
# 	    # 将不同的评论分隔开来


'''
# 爬取所有歌曲，并存储到excel中
'''
wb = openpyxl.Workbook()
#创建工作薄
sheet = wb.active
#获取工作薄的活动表
sheet.title = 'song'
#工作表重命名为song。

sheet['A1'] ='歌曲名'
sheet['B1'] ='所属专辑'
sheet['C1'] ='播放时长'
sheet['D1'] ='播放链接'

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 将参数封装为字典
    json_music = requests.get(url, params=params).json()
    # 调用get方法，下载这个列表，并使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
        name = music['name']
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name']
        # 查找专辑名，把专辑名赋给album
        time = music['interval']
        # 查找播放时长，把时长赋值给time
        link = 'https://y.qq.com/n/yqq/song/' + str(music['file']['media_mid']) + '.html\n\n'
        # 查找播放链接，把链接赋值给link
        sheet.append([name,album,time,link])
        # 把name、album、time和link写成列表，用append函数多行写入Excel
        print('歌曲名：' + name + '\n' + '所属专辑:' + album +'\n' + '播放时长:' + str(time) + '\n' + '播放链接:'+ url)

wb.save('Jay.xlsx')