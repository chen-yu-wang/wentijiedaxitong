#_*_coding:utf-8_*_                                        #删除点赞模型类
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User               #新增
import django.utils.timezone as timezone
'''用户组表,用户组名称不能相同,长度为64,返回用户组名
'''
class UserGroup(models.Model):

    name = models.CharField(max_length=64,unique=True)

    def __unicode__(self):
        return self.name
'''用户信息表,包括用户名,用户组,
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    groups = models.ManyToManyField(UserGroup)
    def __unicode__(self):
        return self.name
'''
帖子板块,长度.板块不能重复.用户权限
'''
class Category(models.Model):

    name = models.CharField(max_length=64,unique=True)
    admin = models.ManyToManyField(UserProfile)
    def __unicode__(self):
        return self.name
'''帖子数据库表,标题,需要设置标题长度,标题不能重复.帖子隶属于板块,帖子插入的图片存储位置,内容以及优先级,帖子内容长度,帖子发布者需要联用用户列表,
如果用户列表在帖子列表下面需要加双引号.
    '''
class Article(models.Model):

    title = models.CharField(u"文章标题",max_length=255,unique=True)
    category = models.ForeignKey(Category,verbose_name=u"板块",on_delete=models.CASCADE)
    #head_img = models.ImageField(upload_to="uploads")
    summary = models.CharField(max_length=255)
    content = models.TextField(u"内容")
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)             #修改
    hidden = models.BooleanField(default=True)
    priority = models.IntegerField(u"优先级",default=1000)
    grade = models.IntegerField(default=0)                                #修改
    good_num = models.IntegerField(default=0)                             #修改
    bad_num = models.IntegerField(default=0)                              #修改
    def __unicode__(self):
        return "<%s, author:%s>" %(self.title,self.author)


'''
评论数据库表,评论的帖子需要联用帖子列表,评论者需要调用用户表,评论内容
'''
class Comment(models.Model):

    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self',related_name='p_comment',blank=True,null=True,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)                     #修改
    def __unicode__(self):
        return "<%s, user:%s>" %(self.comment,self.user)
