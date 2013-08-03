#encoding:utf-8

from django.conf.urls import patterns, include, url
from jeapsns.views import hello,current_time,index_temp,system_info,index_temp_file,delete,index,register
from jeapsns.views import *

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$',hello),
    (r'^hello/$',hello),
    (r'^accounts/register/$','jeapsns.views.register'),
    (r'^accounts/login.$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    (r'^delete/$',delete),
    (r'^edit/$',edit),
    (r'^current_time$',current_time),
    (r'^index_temp/(.){1,9}$',index_temp),
    (r'^system_info/$',system_info),
    (r'^index_temp_file/(\d{1,9})$',index_temp_file),
)
