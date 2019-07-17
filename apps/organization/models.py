from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=50,verbose_name='城市名字')
    des = models.CharField(max_length=200,verbose_name='城市描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict,on_delete=models.CASCADE,verbose_name='所在城市')
    name = models.CharField(max_length=50,verbose_name='机构名字')
    des = models.TextField(verbose_name='机构描述')
    cli_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m',max_length=200,verbose_name='机构照片')
    address = models.CharField(max_length=100,verbose_name='机构地址')
    students = models.IntegerField(default=0,verbose_name='学生人数')
    course_num = models.IntegerField(default=0,verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE,verbose_name='所属机构')
    name = models.CharField(max_length=50,verbose_name='讲师姓名')
    age = models.IntegerField(default=20,verbose_name='讲师年龄')
    work_year = models.IntegerField(default=0,verbose_name='工龄')
    work_company = models.CharField(max_length=50,verbose_name='所属公司')
    work_position = models.CharField(max_length=50,verbose_name='工作地点')
    points = models.CharField(max_length=200,)
    image = models.ImageField(upload_to='teacher/%Y/%m',max_length=200,verbose_name='讲师头像')
    cli_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name

