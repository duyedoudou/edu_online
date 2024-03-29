# Generated by Django 2.2.3 on 2019-07-17 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='image/fault.png', max_length=200, upload_to='banner/%Y/%m')),
                ('url', models.URLField()),
                ('index', models.IntegerField(default=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '轮播',
                'verbose_name_plural': '轮播',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('upemail', '修改邮箱')], max_length=20)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=50)),
                ('birth', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8)),
                ('address', models.CharField(max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('image', models.ImageField(default='image/default.png', max_length=200, upload_to='image/%Y/%m')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
