# Generated by Django 2.2.3 on 2019-07-17 20:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190717_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='image/fault.png', max_length=200, upload_to='banner/%Y/%m', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='顺序'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=100, verbose_name='图片名字'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.URLField(verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', max_length=200, upload_to='image/%Y/%m', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(max_length=50, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]
