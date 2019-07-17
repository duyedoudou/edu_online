# -*- coding: utf-8 -*-

import xadmin

from .models import CityDict,CourseOrg,Teacher


class CityDictAdmin(object):
    list_display = ['name','des','add_time']
    search_fields = ['name','des']
    list_filter = ['name','des','add_time']


class CourseOrgAdmin(object):
    list_display = ['city','name','des','cli_nums','fav_nums','address','students','course_num','add_time']
    search_fields = ['city','name','des','cli_nums','fav_nums','address','students','course_num']
    list_filter =  ['city','name','des','cli_nums','fav_nums','address','students','course_num','add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'age', 'work_year', 'work_company', 'work_position', 'points', 'cli_nums', 'fav_nums','add_time']
    search_fields = ['org', 'name', 'age', 'work_year', 'work_company', 'work_position', 'points', 'cli_nums', 'fav_nums']
    list_filter = ['org', 'name', 'age', 'work_year', 'work_company', 'work_position', 'points', 'cli_nums', 'fav_nums','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
