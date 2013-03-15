from django.conf.urls import patterns, url
from django.conf import settings
import os
from challenge import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<problem_id>\d+)/$', views.problem, name='problem'),
)

ROOT_DIR = os.path.abspath("")
urlpatterns += patterns('django.views',
        url(r'^static/styles/^$', 'static.serve',
            {'document_root': ROOT_DIR + 'static/css/'}, name='css-root'),
        (r'^static/images/^$', 'static.serve',
            {'document_root': ROOT_DIR + 'static/images/'}),
        (r'^static/javascript/^$', 'static.serve',
            {'document_root': ROOT_DIR + 'static/javascript/'}),
)