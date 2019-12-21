import json, re, os
# 导入歌词文件

with open(r'feel like summer.txt','r', encoding = 'utf-8') as file_open:
    data = json.load(file_open)

    lrc = data['lrc']['lyric'].split('\n')
    tlrc = data['tlyric']['lyric'].split('\n')

    pat = re.compile(r'\[.*\]')

    lyrics = []
    for i in lrc:
    	j = {'time': re.findall(pat,i)[0]}
    	lyrics.append(j)
    	# print(re.sub(re.compile(r'\[.*\]'),"",i).strip())




    # lrc = re.sub(re.compile(r'\[.*\]'), "", lrc).strip()
    # tlrc = re.sub(re.compile(r'\[.*\]'), "", tlrc).strip()

