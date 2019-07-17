from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    nick_name = models.CharField(max_length=50)
    birth = models.DateTimeField(blank=True,null=True)
    gender = models.CharField(max_length=8,choices=(('male','男'),('female','女')),default='male')
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=200)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    send_type = models.CharField(max_length=20,choices=(('register','注册'),('forget','找回密码'),('upemail','修改邮箱')))
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}:{}'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner/%Y/%m',default='image/fault.png',max_length=200)
    url = models.URLField(max_length=200)
    index = models.IntegerField(default=100)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '轮播'
        verbose_name_plural = verbose_name