from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cpe400.views',
	url(r'^$', 'index'),
	url(r'^(?P<problem_id>\d+)/$', 'detail'),
	url(r'^(?P<problem_id>\d+)/results/$', 'results'),
	url(r'^(?P<problem_id>\d+)/answer/$', 'answer'),
	)

urlpatterns += patterns('',
	url(r'^admin/', include(admin.site.urls)),
)