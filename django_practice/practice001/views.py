from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta

# Create your views here.
# Django登陆案例
def index(request):	
	# temp = loader.get_template('practice001/index.html')
	# context = RequestContext(request, {})
	# res_html = temp.render(context)

	# return HttpResponse(res_html)


	return render(request, 'practice001/index.html')

def login(request):
	if request.session.has_key('islogin'):
		return redirect('/index')
	else:
		if 'username' in request.COOKIES:
			# 获取记住的用户名
			username = request.COOKIES['username']
		else:
			username =''
		return render(request, 'practice001/login.html', {'username': username})
def login_check(request):
	# 1. 获取登陆信息
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')
	
	# 2. 进行登陆校验
	# 实际开发时用户名和密码放在数据库
	if username == 'smart' and password =='123':
		# 跳转到首页
		response = redirect('/index')
		if remember == 'on':
			response.set_cookie('username', username, max_age=7*24*3600)

		# 记住用户登录状态
		request.session['islogin'] = True
		return response
	else:
		return redirect('/login')
		# 跳转到登陆也
	# 3. 返回request
def ajax_test(request):
	# 显示ajax页面
	return render(request, 'practice001/test_ajax.html')

def ajax_handle(request):
	return JsonResponse({'res':1})

def login_ajax(request):
	return render(request, 'practice001/login_ajax.html')

def login_ajax_check(request):
	username = request.POST.get('username')
	password = request.POST.get('password')

	if username == 'smart' and password == '123':
		return JsonResponse({'res':1, 'username':'smart', 'password':'password'})

	else:
		return JsonResponse({'res':0, 'username':'smart2', 'password':'password2'})

def set_cookie(request):
	'''设置cookie信息'''
	response = HttpResponse('设置cookie')
	# 设置一个cookie信息，名字为mum，值为1
	response.set_cookie('num', 1, max_age=14*24*3600)
	# response.set_cookie('num', 1, expires=datetime.now()+timedelta(days=14))

	return response

def get_cookie(request):
	'''获取cookie信息'''
	num = request.COOKIES['num']
	return HttpResponse(num)

def set_session(request):
	request.session['username'] = 'smart'
	request.session['age'] = 18

	return HttpResponse('设置session')

def get_session(request):
	username = request.session['username']
	age = request.session['age']
	# age = request.session.get('键', '默认值')
	# 清除值
	# request.session.clear()
	# 完全清楚
	# request.session.flush() 
	# 删除指定键及值
	# del request.session['键']
	# 设置回话的超过时间，默认两周
	# value是整数，sessionid cookie在value秒后过期
	# 0关闭浏览器过期
	# 
	# request.session.set_expiry(value)

	return HttpResponse(username+':'+str(age))