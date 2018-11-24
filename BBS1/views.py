#_*_coding:utf-8_*_
from django.shortcuts import render,HttpResponseRedirect
#import models
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger    #新增
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import ArticleForm,handle_uploaded_file
# Create your views here.
def index(request):
    '''首页'''
    articles = Article.objects.all()
    return render(request,'index.html',{'articles': articles})
def category(request,category_id):                                       #修改
    '''二级分类'''
    articles = Article.objects.filter(category_id=category_id)
    paginator = Paginator(articles,3)
    page = request.GET.get('page',1)
    page=int(page)
    try:
        articles1 = paginator.page(page)
    except PageNotAnInteger:
        articles1 = paginator.page(1)
    except EmptyPage:
        articles1 = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'articles': articles1})

def categoryTime(request,category_id):                                  #新增
    articles = Article.objects.filter(category_id=category_id).order_by('id')
    return render(request,'index.html',{'articles': articles})
def categoryQuality(request,category_id):                               #新增
    for i in Article.objects.filter(category_id=category_id):
        i.grade = 10*i.good_num-10*i.bad_num
        i.save()
    articles = Article.objects.filter(category_id=category_id).order_by('grade')
    return render(request,'index.html',{'articles': articles})

def getGood_num(request,category_id,id):                                #新增
    article = Article.objects.get(id=id)
    article.good_num=article.good_num+1
    article.grade=article.grade+10
    article.save()
    return HttpResponseRedirect(reverse('category', args=(category_id,)))

def getBad_num(request,category_id,id):                                 #新增
    article = Article.objects.get(id=id)
    article.good_num=article.good_num+1
    article.grade=article.grade-10
    article.save()
    return HttpResponseRedirect(reverse('category', args=(category_id,)))

def getGood_num1(request,category_id,id):                               #新增
    article = Article.objects.get(id=id)
    article.good_num=article.good_num+1
    article.grade=article.grade+10
    article.save()
    return HttpResponseRedirect(reverse('categoryQuality', args=(category_id,)))

def getBad_num1(request,category_id,id):                                #新增
    article = Article.objects.get(id=id)
    article.good_num=article.good_num+1
    article.grade=article.grade-10
    article.save()
    return HttpResponseRedirect(reverse('categoryQuality', args=(category_id,)))

def article_detail(request,article_id):
    '''帖子内容'''
    try:
        article_obj = Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request,'404.html',{'err_msg':u"文章不存在！"})
    return render(request,'article.html', {'article_obj':article_obj})
def acc_logout(request):
    '''退出登陆'''
    logout(request)
    return HttpResponseRedirect('/')
def acc_login(request):
    '''登陆'''
    print(request.POST)
    err_msg =''
    if request.method == "POST":
        print('user authention...')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            err_msg = "Wrong username or password!"
    return render(request,'login.html',{'err_msg':err_msg})


def new_article(request):
    '''最新帖子'''
    if request.method == 'POST':
        print(request.POST)
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            print("--form data:",form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id

            new_img_path = handle_uploaded_file(request,request.FILES['head_img'])
            form_data['head_img'] = new_img_path
            new_article_obj = Article(**form_data)
            new_article_obj.save()
            return  render(request,'new_article.html',{'new_article_obj':new_article_obj})
        else:
            print('err:',form.errors)
    category_list = Category.objects.all()
    return render(request,'new_article.html', {'category_list':category_list})







