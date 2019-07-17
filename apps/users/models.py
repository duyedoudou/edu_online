from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True,verbose_name='用户名')
    nick_name = models.CharField(max_length=50,verbose_name='昵称')
    birth = models.DateTimeField(blank=True,null=True,verbose_name='生日')
    gender = models.CharField(max_length=8,choices=(('male','男'),('female','女')),default='male',verbose_name='性别')
    address = models.CharField(max_length=200,verbose_name='地址')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号')
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=200,verbose_name='头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name='验证码')
    email = models.EmailField(max_length=20,verbose_name='邮箱')
    send_type = models.CharField(max_length=20,choices=(('register','注册'),('forget','找回密码'),('upemail','修改邮箱')),verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now,verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):      # 返回
        return '{}我和你{}'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name='图片名字')
    image = models.ImageField(upload_to='banner/%Y/%m',default='image/fault.png',max_length=200,verbose_name='图片')
    url = models.URLField(max_length=200,verbose_name='图片地址')
    index = models.IntegerField(default=100,verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播'
        verbose_name_plural = verbose_name