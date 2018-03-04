"""ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import login,logout
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from sim.views import loginSuccess, detailInfo,changeInfo,changePassword,choseCources,materailsDetail,materailAdd
from tm.views import MaterialListView, materialStorage,GradeListView,allocMaterial, MaterialEntryListView,MaterialOutBoundListView
from django.contrib.admin import models


urlpatterns = [
    #主页
    path('admin/', admin.site.urls),
    #学生登录
    path('login/', login ,{'template_name': 'sim/login.html'}),
    path('login/success/', loginSuccess ),
    path('student/logout/', logout,{'next_page':'/login/'}),
    #学生信息
    path('student/detail/', detailInfo),
    path(r'student/change/', changeInfo),
    path('changePassword/',changePassword),
    path('chooseCources/',choseCources),
    #材料入库
    path(r'materialStorage/detail/',MaterialListView.as_view(), name = 'material_list'),
    path(r'materialStorage/add/', materialStorage),
    #材料分配
    path(r'materialAlloc/detail/',GradeListView.as_view(), name = 'grade_list'),
    path(r'materialAlloc/alloc/',allocMaterial),
    #出入库记录
    path(r'materialRecord/entry/', MaterialEntryListView.as_view(),  name='materialstoragemodel_list'),
    path(r'materialRecord/out/', MaterialOutBoundListView.as_view(), name='materialallocmodel_list')

]