from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import Course

# Create your models here.


class Userask(models.Model):
    name = models.CharField(max_length=20,verbose_name='用户名')
    mobile = models.CharField(max_length=11,verbose_name='联系方式')
    course_name = models.CharField(max_length=50,verbose_name='咨询课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户名')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程名')
    comment = models.CharField(max_length=200,verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户名')
    fav_id = models.IntegerField(default=0,verbose_name='喜欢的id')
    fav_type = models.IntegerField(choices=((1,'机构'),(2,'课程'),(3,'讲师')),default=3,verbose_name='喜欢类型')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name='用户名')   # 这是发给全员的消息
    message = models.CharField(max_length=500,verbose_name='消息内容')
    has_read = models.BooleanField(default=False,verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户名')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

