# -*- coding: utf-8 -*-

import xadmin

from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display = ['name','des','degress','student','fav_nums','cli_nums','time_len','chapter','category','add_time']
    search_fields = ['name','des','degress','student','fav_nums']
    list_filter = ['name','des','degress','student','fav_nums']


class LessonAdmin(object):
    list_display = ['course','name','time_len','add_time']
    search_fields = ['course','name','time_len']
    list_filter = ['course__name','name','time_len','add_time']  # __name 就能搜索外键的name


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'time_len', 'add_time']
    search_fields = ['lesson', 'name', 'time_len']
    list_filter = ['lesson', 'name', 'time_len', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)