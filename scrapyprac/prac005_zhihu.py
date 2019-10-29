import requests, csv
from bs4 import BeautifulSoup

csv_file=open('articles.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)

list2=['标题','链接','摘要']
writer.writerow(list2)

url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

for x in range(0,40,20):
	params = {
		'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
		'offset': x,
		'limit': 20,
		'sort_by': 'voteups'
	}

	res=requests.get(url,headers=headers,params=params)
	articles=res.json()['data']

	for article in articles:
		list1 = [article['title'], article['url'], article['excerpt']]
		writer.writerow(list1)

	x+=20

csv_file.close()

print('ok')



# bstitle=BeautifulSoup(res.text,'html.parser')
# #用bs进行解析
# title=bstitle.findAll(class_='ContentItem-title')

# #提取我们想要的标签和里面的内容
# print(title[0].text)
# #打印title