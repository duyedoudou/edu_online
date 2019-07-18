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
错误信息记录：urls.py文件中，
    path('', TemplateView.as_view(template_name='index.html'), name='index')
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
一直报语法错误，误以为不能两个TemplateView.as_view一起用，实则是上一个path的最后没有加’逗号’。



