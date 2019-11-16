from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django import http

# Create your views here.


# def index(request):
    # return HttpResponse("One World One Dream!")
#
#
# def get_body_form(request):
#     query_dict = request.POST
#     a = query_dict.get('a')
#     like = query_dict.getlist('like')
#     return HttpResponse('get_body_form')
#
#
# def get_json_body_str(request):
#     # body_byes = request.body
#     # body_str = body_byes.decode()
#     # json_dict = json.loads(body_str)
#     # json_dict = json.loads(request.body.decode())
#     return HttpResponse('get_body_json_str')
#
#
# def response_demo(request):
#     # return HttpResponse(content='hello world', content_type='text/html', status=200)
#     # response = HttpResponse("study")
#     # response['Itcast'] = 'Python32'
#     # return response
#     # data_dict = {"name": "zhangsan", "age": 18}
#     # return http.JsonResponse(data_dict)
#     data_list = ["name","zhangsan", "age", 18]
#     dict_data = {"data_list": data_list}
#     # return http.JsonResponse(data_list, safe=False)
#     return http.JsonResponse(dict_data)
#
#
# def redirect_demo(request):
    # return redirect('/index/')
#
# # 表单类型Form Data
# def get_body(request):
#     a = request.POST.get('world')
#     b = request.POST.get('Dream')
#     alist = request.POST.getlist('world')
#     print(a)
#     print(b)
#     print(alist)
#     return HttpResponse('OK')
#
#
# adict = {"a": 1, "b": 2}
#
#
# def get_body_json(request):
#     json_str = request.body
#     json_str = json_str.decode()
#     req_data = json.loads(json_str)
#     print(req_data['a'])
#     print(req_data['b'])
#     # json.loads(request.body.decode())
#     return HttpResponse('OK')
#
#
# # 请求头，request.META为字典类型
# def get_headers(request):
#     print(request.META['CONTENT_TYPE'])
#     return HttpResponse("META[CONTENT_TYPE]")
#
#
# # HttpResponse
# def view_demo(request):
#     # return HttpResponse('itcast', status=400)
#     # 或者
#     response = HttpResponse('itcast python')
#     response.status_code = 400
#     response['itcast'] = 'python'
#     return response
#
#
# def func_out(fn):
#     def func_inner(resquest, *args, **kwargs):
#         fn(resquest, *args, **kwargs)
#         return HttpResponse("good good study ")
#
#     return func_inner
#
#
# @func_out
# def fun():
#     print('外函数')


from .models import BookInfo, HeroInfo
from datetime import date
from django.db.models import F, Q

# book = BookInfo()
# book.btitle='碧血剑'
#
# book = BookInfo(
#     btitle='西游记',
#     bpub_date='1988-1-1',
#     bread=10000,
#     bcomment=200000
# )
# book.save()
#
# BookInfo.objects.create(
#     btitle='三国',
#     bpub_date='1922-1-1',
#     bread=109,
#     bcomment=901
# )
#
# hero = HeroInfo.objects.create(
#     hname='孙悟空',
#     hgender=0,
#     hbook=book
# )
# hero.save()
#
# hero = HeroInfo.objects.create(
#     hname='唐玄奘',
#     hgender=1,
#     hbook_id=book.id
#
# )
# hero.save()

# BookInfo.objects.all()
# book = BookInfo.objects.get(id=11)
# print(book)

# BookInfo.objects.get(id=2)
# BookInfo.objects.get(pk=2)

# try:
#     BookInfo.objects.get(id=100)
# except BookInfo.DoesNotExist:
#     pass
#
#
# BookInfo.objects.count()
#
#
# # exact:表示判等
# BookInfo.objects.filter(id=5)
#
# BookInfo.objects.filter(id__exact=1)
#
# # 模糊查询  contains:是否包含
# BookInfo.objects.filter(btitle__contains='传')
#
# # startswith以指定值开头
# BookInfo.objects.filter(btitle__startswith='雪')
# # endswith以指定值开头
# BookInfo.objects.filter(btitle__endswith='神')
#
# # 以上运算符都区分大小写，在这些运算符前加上i表示不区分大小写，如iexact、icontains、istartswith、iendswith.
#
# # 空查询
# BookInfo.objects.filter(btitle__isnull=False)
#
# # 范围查询
# # in:是否在其中
# BookInfo.objects.filter(id__in=[1, 3, 5])
#
# #  比较查询
# # gt 大于
# # gte 大于等于
# # lt 小于
# # lte 小于等于
# # exclude()不等于
# BookInfo.objects.filter(id__gt=2)
# BookInfo.objects.filter(id__gte=4)
# BookInfo.objects.filter(id__lt=5)
# BookInfo.objects.filter(id__lte=6)
# BookInfo.objects.exclude(id=3)
#
# # 日期查询(year, month, day, week_day, hour, minute, second:对日期时间类型的属性进行运算)
# BookInfo.objects.filter(bpub_date__year=1980)
# # 查询1998年后发表的图书
# BookInfo.objects.filter(bpub_date__gt=(1998,1,3))
#

# book_qs = BookInfo.objects.filter(bread__gt=F('bcomment'))
# print(book_qs)
# book_qs = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)
# book_qs = BookInfo.objects.filter(bread__gt=2, bcomment__gt=24)
# book_qs = BookInfo.objects.filter(Q(bread__gt=2), Q(bcomment__gt=34))
# book_qs = BookInfo.objects.filter(Q(bread__gt=10) | Q(bcomment__gt=34))
# book_qs = BookInfo.objects.all().order_by('bread')
# book_qs = BookInfo.objects.all().order_by('-bread')
# book_qs = BookInfo.objects.all().order_by('bread', '-bcomment')
# book_qs = BookInfo.objects.get(id=10).HeroInfo_set.all()
# book_qs = HeroInfo.objects.get(id=18).BookInfo
# book_qs = BookInfo.objects.filter(heroinfo_hname='郭靖')
# book_qs = BookInfo.objects.filter(heroinfo_hgender=1)
# hero_qs = HeroInfo.objects.filter(hbook_id=1)
# print(book_qs)
# print(hero_qs)
# book = BookInfo.objects.get(id=5)
# book.btitle = '鹿鼎记'
# book.save()
# book = BookInfo.objects.get(id=6)
# book.btitle = '神雕侠侣'
# book.save()
# BookInfo.objects.filter(id=7).update(btitle='碧血剑')
# BookInfo.objects.filter(id=8).update(btitle='连城诀')
# BookInfo.objects.filter(id=9).update(btitle='书剑恩仇录')






