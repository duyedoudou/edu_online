# -*- coding: utf-8 -*-
import xadmin

from .models import EmailVerifyRecord,UserProfile,Banner


class UserProfileAdmin(object):
    list_display = ['user','nick_name','birth','gender','address','mobile','image']  # 展示
    search_fields = ['user','nick_name','birth','gender','address','mobile','image']  # 搜索
    list_filter = ['user','nick_name','birth','gender','address','mobile','image']  # 过滤器


class EmailVerifyRecordAdmin(object):  # 是object
    list_display = ['code','email','send_type','send_time']  # 展示
    search_fields = ['code','email','send_type']       # 搜索
    list_filter = ['code','email','send_type','send_time']  # 过滤器


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(Banner,BannerAdmin)
