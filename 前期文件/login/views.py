from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django import forms
from rnapp.models import User


##定义UserForm表单用于注册和登录页面，ChangeForm表单用于修改密码页面
class UserForm(forms.Form):
    phone = forms.CharField(label='用户名')
    password = forms.CharField(label='密   码', widget=forms.PasswordInput())
    # last_login = forms.DateTimeField()


class ChangeForm(forms.Form):
    phone = forms.CharField(label='用户名')
    old_password = forms.CharField(label='原密码', widget=forms.PasswordInput())
    new_password = forms.CharField(label='新密码', widget=forms.PasswordInput())


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            phone = uf.cleaned_data['phone']
            password = uf.cleaned_data['password']

            ##判断用户原密码是否匹配
            user = User.objects.filter(phone=phone)
            if user:
                info = '用户名已存在!'
            elif len(user) == 0:
                info = '注册成功!'
                user = User()
                user.phone = phone
                user.password = password
                user.save()

            return HttpResponse(info)
    else:
        uf = UserForm()

    return render(request, 'public/regist.html', locals())


def login(request):
    if request.method == 'POST':
        ##获取表单信息
        uf = UserForm(request.POST)
        if uf.is_valid():
            phone = uf.cleaned_data['phone']
            password = uf.cleaned_data['password']

            ##判断用户密码是否匹配
            user = User.objects.filter(phone=phone)
            if user:
                passwd = User.objects.filter(phone=phone, password=password)
                if passwd:
                    info = '登录成功！'
                else:
                    info = '请检查密码是否正确!'
            elif len(user) == 0:
                info = '请检查用户名是否正确!'

            return HttpResponse(info)
    else:
        uf = UserForm()

    return render(request, 'public/login.html', locals())


def change_pass(request):
    if request.method == 'POST':
        uf = ChangeForm(request.POST)
        if uf.is_valid():
            phone = uf.cleaned_data['phone']
            old_password = uf.cleaned_data['old_password']
            new_password = uf.cleaned_data['new_password']

            ##判断用户原密码是否匹配
            user = User.objects.filter(phone=phone)
            if user:
                passwd = User.objects.filter(phone=phone, password=old_password)
                if passwd:
                    User.objects.filter(phone=phone, password=old_password).update(
                        password=new_password)  ##如果用户名、原密码匹配则更新密码
                    info = '密码修改成功!'
                else:
                    info = '请检查原密码是否输入正确!'
            elif len(user) == 0:
                info = '请检查用户名是否正确!'

        return HttpResponse(info)
    else:
        uf = ChangeForm()
    return render(request, 'public/change.html', {'uf': uf})


def index(request):
    return render(request, "index.html")

