import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xiachufang.com/explore/').text
bs = BeautifulSoup(res, 'html.parser')

# food_lists = bs.find_all('div', class_='info pure-u')
# foods = []

# for food in food_lists:
# 	food_name = food.find('a').text.strip()
# 	food_url = "http://www.xiachufang.com"+food.find('a')['href']
# 	food_ing = food.find('p', class_='ing ellipsis').text.strip()

# 	foods.append([food_name, food_url, food_ing])

# for food in foods:
# 	print(food[0])

	# print("菜谱名："+food_name+"\n"+"URL："+food_url+"\n"+"食材："+food_ing)
	# print("====================")

'''
第二种思路
'''

names = bs.find_all('p', class_='name')
urls = bs.find_all('p', class_='name')
ings = bs.find_all('p', class_='ing ellipsis')

foods = []

for i in range(len(names)):
	name = names[i].text.strip()
	url = 'http://www.xiachufang.com'+urls[i].find('a')['href']
	ing = ings[i].text.strip()

	foods.append([name, url, ing])

for food in foods:
	print(food[0]+'\n'+food[1]+'\n'+food[2])
	print('====================')