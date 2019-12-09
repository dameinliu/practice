import requests, json, re, os
from bs4 import BeautifulSoup

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}

# 根据歌手id获取前50首热门作品
def get_songs_by_singer_id(singer_id):
    singer_url = 'http://music.163.com/artist?id=' + str(singer_id)  # 获取歌手链接，根据歌手的id获取数据
    web_data = requests.get(singer_url, headers=headers)

    soup = BeautifulSoup(web_data.text, 'lxml')

    singer_name = soup.select("#artist-name")#获取歌手名字
    r = list(soup.find('ul', {'class': 'f-hide'}).find_all('a'))
    music_id_set = []#此歌手音乐的id列表
    music_name_set=[]#此歌手音乐的名字列表

    for each in r:
        song_name = each.text  # 歌曲名字 
        music_name_set.append(song_name)
        song_id = each.attrs["href"]
        music_id_set.append(song_id[9:])#歌曲id，从第九个字符开始取id，上面图片展示过
    
    dic = dict(map(lambda x, y: [x, y],  music_id_set,music_name_set))  # 将音乐名字和音乐id组成一个字典

    path = "E:/lyrics/"+singer_name
    if not os.path.exists(path):
        os.makedirs(path)

    for i in music_id_set:
        f=open(path+"/"+dic[i]+".txt",'w')
        lyric = get_lyric_by_music_id(i)#获取某一首歌的歌词
        if lyric==None:
            print("No lyric")
            continue
        else:
            print(dic[i])  # 单个文件存储一个歌手某一首歌以歌名命名
            try:
                for index in lyric:
                    f.write(index)

            except UnicodeEncodeError as u:
                continue
        f.close()

# 根据专辑id获取专辑歌词
def get_songs_by_album_id(album_id):
    album_url = 'http://music.163.com/album?id=' + str(album_id)  # 获取歌手链接，根据歌手的id获取数据
    web_data = requests.get(album_url, headers=headers)

    soup = BeautifulSoup(web_data.text, 'lxml')

    ### 获取专辑基本信息
    album_name = soup.select(".tit h2")[0].text #专辑名
    album_singer = soup.select("p.intr")[0].text #歌手
    album_pub_date = soup.select("p.intr")[1].text #发行日期
    album_publisher = soup.select("p.intr")[2].text #发行公司
    album_desc = soup.select("#album-desc-dot")[0].text # 专辑介绍

    ### 
    r = list(soup.find('ul', {'class': 'f-hide'}).find_all('a'))
    music_id_set = []#此歌手音乐的id列表
    music_name_set=[]#此歌手音乐的名字列表

    for each in r:
        song_name = each.text  # 歌曲名字 
        music_name_set.append(song_name)
        song_id = each.attrs["href"]
        music_id_set.append(song_id[9:])#歌曲id，从第九个字符开始取id，上面图片展示过

    dic = dict(map(lambda x, y: [x, y],  music_id_set,music_name_set))
    # 将音乐名字和音乐id组成一个字典
    # map() 会根据提供的函数对指定序列做映射
    # lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。例：
    #--- add = lambda x, y : x+y
    #--- add(1,2)  # 结果为3
    path = "D:/lyrics/"+album_name
    if not os.path.exists(path):
        os.makedirs(path)

    for i in music_id_set:
        f=open(path+"/"+dic[i]+".txt",'w')
        lyric = get_lyric_by_music_id(i)#获取某一首歌的歌词
        if lyric==None:
            print("No lyric")
            continue
        else:
            print(dic[i])  # 单个文件存储一个歌手某一首歌以歌名命名
            try:
                for index in lyric:
                    f.write(index)

            except UnicodeEncodeError as u:
                continue
        f.close()


#根据歌词id提取单首歌词
def get_lyric_by_music_id(music_id):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'

    lyric = requests.get(lrc_url, headers=headers)
    json_obj = lyric.text
    j = json.loads(json_obj) #json对象转化为python对象，dumps将python对象转化为json对象

    try:
        # 部分歌曲没有歌词，这里引入一个异常
        lrc = j['lrc']['lyric']
        lrc = re.sub(re.compile(r'\[.*\]'), "", lrc).strip()
        return lrc
    except KeyError as e:
        pass

if __name__ == '__main__':
    # get_songs_by_singer_id('6452')
    get_songs_by_album_id('14529')
    # get_lyric_by_music_id()