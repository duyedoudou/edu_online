# edu_online
django在线卖课平台

## 2019.7.16
设计了apps相关的models，并放在apps文件夹下，分别为users,courses,organization,operation四个应用。

在setting.py文件中添加进新建的应用。

在setting.py文件中将apps文件夹和根目录join，作为搜索源目录。

## 2019.7.17
django2.环境下，github上下载xadmin2分支的源码的zip包。https://github.com/sshwsfc/xadmin/tree/django2

下载下来后，在你的django项目下新建一个extra_apps文件夹，ZIP包解压到这个文件夹里。在虚拟环境下，进入这个extra_apps，然后

python setup.py install

这时候要耐心的等他装依赖环境。等就行了。

安装好了后，把别的文件都删了，只留下xadmin就行。

一定要看，但是下面的👇博客的前半部分写的不完全对，要接着我上述的看，余下看博客。

余下写在这个博客里：https://www.jianshu.com/p/fa7944bdcc1b

## 2019.7.17
在各个app文件夹中，增加adminx.py文件，在其中写models的注册。注意，和admin中是不一样的（继承上）。

models中的verbose_name，在后台显示出来了。

## 2019.7.17 晚
在users/adminx.py文件中增加两个类，功能是使后台增加切换主题功能、更改后台页面的title和footer。

修改各个app的apps.py和__init__.py文件，_init__.py文件增加default_app_config；apps.py文件增加verbose_name 

使各个app能够在后台显示中文。具体可查看源码。

## 2019.7.18
1)错误信息记录：urls.py文件中，

    path('', TemplateView.as_view(template_name='index.html'), name='index')
    
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    
一直报语法错误，误以为不能两个TemplateView.as_view一起用，实则是上一个path的最后没有加’逗号’。

2)错误记录：登录页面点击提交后，跳转到/login/login.html地址。原因：login.html文件中，<form那一行，action=的位置没有修改，应该是当前地址

.和/login/都行。

3)实现使用用户名或者邮箱都能登录。

在setting.py文件中增加AUTHENTICATION_BACKENDS字段。功能：重定向authenticate函数。

在user/views.py文件中，增加类CustomBackend，重写authenticate函数的功能，其中引入大Q方法，用来实现‘或’的功能。

4)增加form类文件，form的主要功能是，举个例子：在用户登录时，用户名和密码如果为空，或者长度不满足，就会被form的实例拦截，不会在传递给authenticate函数。

这样实现了与处理的功能。

通过逻辑判断，传不同的字典给前端html，对不同的错误类型返回不同的提示信息。

5)使用静态文件：{% load staticfiles %}这样就能使用相对路径了，举例：href={% static 'css/reset.css' %}

6）注册时，使用验证码：安装django-simple-captcha。github地址：https://github.com/mbi/django-simple-captcha

说明文档地址：https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation



