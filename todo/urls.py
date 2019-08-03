# -*- coding: utf-8 -*-
__author__ = 'caokun'
__date__ = '2019/8/3 3:44'


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='待办事项主页'),
    path('about/', views.about,name='待办事项关于'),
    path('edit/', views.edit,name='编辑'),

]