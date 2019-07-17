from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict,on_delete=models.CASCADE,verbose_name='所在城市')
    name = models.CharField(max_length=50)
    des = models.TextField()
    cli_nums = models.IntegerField(default=0,verbose_name='点击数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏数')
    image = models.ImageField(upload_to='org/%Y/%m',max_length=200)
    address = models.CharField(max_length=100)
    students = models.IntegerField(default=0)
    course_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    work_year = models.IntegerField(default=0)
    work_company = models.CharField(max_length=50)
    work_position = models.CharField(max_length=50)
    points = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teacher/%Y/%m',max_length=200)
    cli_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name

