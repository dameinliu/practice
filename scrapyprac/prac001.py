import requests

content = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html').content.decode('utf8')

print(content)

f = open('content.html', 'a+', encoding='utf8')
f.write(content.replace(u'\xa9',u''))
f.close()