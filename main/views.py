from django.shortcuts import render

# Create your views here.
# coding:utf-8

from django.http import HttpResponse
from main.backends.command import checkSQL


def Hello(request):
    return HttpResponse(checkSQL('/*--user=root;--password=sf123456;--host=10.202.4.39;--execute=1;--port=3306;*/\
inception_magic_start;\
use db1;\
insert into hotnews(id,title)values("19","title2");\
inception_magic_commit;'))


def Command(request):
    return render(request, 'Console.html')


def SQLCheck(request):
    sql = request.POST.getlist('sql')
    sql = sql[0]
    result = checkSQL(sql)
    print result
    return HttpResponse(content=result,content_type="application/json")

