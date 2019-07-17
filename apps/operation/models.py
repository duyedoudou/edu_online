from django.db import models

from users.models import UserProfile
from courses.models import Course

# Create your models here.


class Userask(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    course_name = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0,verbose_name='喜欢的id')
    fav_type = models.IntegerField(choices=((1,'机构'),(2,'课程'),(3,'讲师')),default=1)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0)   # 这是发给全员的消息
    message = models.CharField(max_length=500)
    has_read = models.BooleanField(default=False)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

