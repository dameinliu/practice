import json, re, os
# 导入歌词文件

with open(r'feel like summer.txt','r', encoding = 'utf-8') as file_open:
    data = json.load(file_open)

    lrc = data['lrc']['lyric'].split('\n')
    tlrc = data['tlyric']['lyric'].split('\n')

    pat = re.compile(r'\[.*\]')

    lyrics = []
    tlyrics = []
    # print(lrc)
    ### 原版歌词
    for i in lrc:
        try:
            if len(re.findall(pat,i)) > 0:
                time = re.findall(pat,i)[0]
                ly = {'time':time, 'lyrics':re.sub(pat,"",i)}
                lyrics.append(ly)
            else:
                pass
        except KeyError as e:
            pass
    ### 翻译版歌词
    for i in tlrc:
        try:
            if len(re.findall(pat,i)) > 0:
                time = re.findall(pat,i)[0]
                ly = {'time':time, 'lyrics':re.sub(pat,"",i)}
                tlyrics.append(ly)
            else:
                pass
        except KeyError as e:
            pass

    	# print(re.sub(re.compile(r'\[.*\]'),"",i).strip())

    ### 组合歌词
    ### flyric是一个包含歌词和翻译歌词对应的列表
    flyrics = []
    for i in lyrics:
        for j in tlyrics:
            if i['time'] == j['time']:
                ly = {'lyrics':i['lyrics'], 'tlyrics':j['lyrics']}
                flyrics.append(ly)





    # lrc = re.sub(re.compile(r'\[.*\]'), "", lrc).strip()
    # tlrc = re.sub(re.compile(r'\[.*\]'), "", tlrc).strip()

