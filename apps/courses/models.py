from datetime import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name='课程名字')
    des = models.CharField(max_length=200,verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    img = models.ImageField(upload_to='course/%Y/%m',max_length=200,verbose_name='封面图')
    degress = models.CharField(choices=(('dj','低级'),('zj','中级'),('gj','高级')),max_length=3,verbose_name='课程难度')
    student = models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    cli_nums = models.IntegerField(default=0,verbose_name='点击人数')
    time_len = models.IntegerField(default=0,verbose_name='课程时长')
    chapter = models.IntegerField(default=0,verbose_name='章节数')
    category = models.CharField(max_length=20,default='后端开发',verbose_name='课程类别')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    name = models.CharField(max_length=50,verbose_name='章节名称')
    time_len = models.IntegerField(default=0,verbose_name='章节时长')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name='章节')
    name = models.CharField(max_length=50)
    time_len = models.IntegerField(default=0,verbose_name='视频时长')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程资源')
    name = models.CharField(max_length=50,verbose_name='资源名字')
    download = models.FileField(upload_to='course/resource/%Y/%m',verbose_name='资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '资源下载'
        verbose_name_plural = verbose_name