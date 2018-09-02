from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^index_new/$', views.index_new, name='index_new'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^join/$', views.join, name='join'),
    url(r'^join_done/$', views.join_done, name='join_done'),
    url(r'^login_sent/$', views.login_sent, name='login_sent'),
    url(r'^match/$', views.match, name='match'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^hooray/$', views.hooray, name='hooray'),
    url(r'^please/$', views.please, name='please'),
    url(r'^site_info/$', views.site_info, name='site_info'),
]
