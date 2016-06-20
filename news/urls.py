"""news app
"""
from django.conf.urls import url, include, patterns
from news.views import *

urlpatterns = patterns('news.views',
                       url(r'^admin/news/column/add/',  'column_add',name='column_add'),
                       url(r'^admin/news/column/update/(?P<id>\d+)/$',  'column_update',name='column_update'),
                       url(r'^admin/news/column/list/',  'column_list',name='column_list'),
                       url(r'^admin/news/column/del/(?P<id>\d+)/$', 'column_del',name='column_del'),

                       url(r'^admin/news/article/add/',  'article_add',name='article_add'),
                       url(r'^admin/news/article/update/(?P<id>\d+)/$',  'article_update',name='article_update'),
                       url(r'^admin/news/article/del/(?P<id>\d+)/$', 'article_del',name='article_del'),
                       url(r'^admin/news/article/list/', 'article_list',name='article_list'),
                       url(r'^admin/news/article/show/(?P<id>\d+)/$',  'article_show',name='article_show'),

                       #url(r'^index','article_list',name='article_list'),
                       )