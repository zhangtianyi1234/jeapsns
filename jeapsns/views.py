#encoding:utf-8

#加入源代码包
from django.template import RequestContext
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
import os
from django.shortcuts import render_to_response,redirect
#管理员注册管理包
from django.contrib.auth.forms import *
from django.contrib import admin
#加入的本应用包
from jeapsns.forms import SnsForm
from jeapsns.models import sns

#admin.site.register(sns)
def index(request):
    if request.user.is_authenticated():
            return render_to_response("index.html",{'name':request.user.username})
    return HttpResponseRedirect("/accounts/register/")
def hello(request):
   # if 'id'in request.GET:
    #    id=request.GET['id']
     #   id=int(d)
      #  if id=='0':
       #     l2=sns.objects.all()
       # else:
        #    l2=sns.objects.get(id=id)
    #    return render_to_response('hello.html',{'l2',l2})
   # return HttpResponse("Hello world")
    if request.method=='POST':
        n=sns()
        n.content=request.POST['content']
        n.save()
    f=SnsForm()
    ls=sns.objects.all()
    return render_to_response('hello.html',{'ls':ls,'f':f},context_instance=RequestContext(request))

def delete(request):
    if 'id' in request.GET:
        n=sns.objects.get(id=int(request.GET['id']))
        n.delete()
    return redirect('/hello')

def current_time(request):
    s=datetime.datetime.now()
    return HttpResponse(s)    

def index_temp(request,input_name):
	t = Template('My name is{{ name }}.')
	c = Context({'name': input_name})
	return HttpResponse(t.render(c))

def system_info(request):
    s=os.getcwd()
    return HttpResponse(s)

def index_temp_file(request,id):
    if id=='0':
        l1=sns.objects.all()
    else:
        #l1=sns.objects.get(id=id)
	l1=sns.objects.filter(id=id)
    return render_to_response('index_temp_file.html',{'l1':l1})

def edit(request,mid):
    if request.method=='GET':  
        mb=Sns.objects.get(id=mid)
        f=SnsForm({'name':mb.name,'content':mb.content})
        return reder_to_response('edit.html',{'f':f},context_instance=RequestContext(request))
    if request.method=='POST':
        mb=Sns.objects.get(id=mid)
        mb.name=request.POST['name']
        mb.content=request.POST['content']
        mb.save()
        return HttpResponseRedirect('/hello/?list=1')

def register(request):
    form =UserCreationForm()
    if request.method=='GET':
        return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            return redirect('/hello')
        return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
