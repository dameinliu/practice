from django.urls import path, re_path
from practice001 import views

urlpatterns = [
    re_path(r'^index$', views.index),
    re_path(r'^login$', views.login),
    re_path(r'^login_check$', views.login_check),
    re_path(r'^test_ajax$', views.ajax_test),
    re_path(r'^ajax_handle$', views.ajax_handle),
    re_path(r'^login_ajax$', views.login_ajax),
    re_path(r'^login_ajax_check$', views.login_ajax_check),
    re_path(r'^set_cookie$', views.set_cookie),
    re_path(r'^get_cookie$', views.get_cookie),
    re_path(r'^get_session$', views.get_session),
    re_path(r'^set_session$', views.set_session),
]
