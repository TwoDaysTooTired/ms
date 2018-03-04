from django.contrib import admin
from .models import Material
from .models import Course
from .models import Grade
from .models import StudentInfo
from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.shortcuts import render
from .models import MaterialStorageModel
from django.contrib.auth.models import User
from sim.models import StudentUser
# Register your models here.


def updateDetailOfModel(self,request,queryset):
    if not queryset.count() == 1:
        self.message_user(request,u"必须选择一个进行更改")
    else:
        model = queryset[0]
        info = (model._meta.app_label, model._meta.model_name)
        #return HttpResponseRedirect(reverse('admin:%s_%s_changelist' % info, current_app=self.name))
        requestAdd =request.path+str(model.id)+"/"+'change'
        return HttpResponseRedirect(requestAdd)


updateDetailOfModel.short_description = u'修改所选的'


def getChangeFunc(verbose_name):
    updateDetailOfModel.short_description = u'修改所选的' + verbose_name
    updateDetailOfModel.__name__ = verbose_name
    return updateDetailOfModel

class MaterialAdmin(admin.ModelAdmin):
    fields = ['SerialNum','Name','Type','InventoryLimitNum','Price','Note']
    list_display = ['id','Name','SerialNum','Type','InventoryNum','Price','Note']
    list_display_links = ['Name']
    search_fields = ['Name','SerialNum']
    list_filter = ['Type','Price']
    list_per_page = 15
    actions = [updateDetailOfModel]

    def get_actions(self, request):
        actions = super(MaterialAdmin,self).get_actions(request)
        mod = actions['updateDetailOfModel']
        newMod = (mod[0],mod[1],mod[2] +" "+ self.model._meta.verbose_name)
        actions['updateDetailOfModel'] = newMod
        return actions


class CourseAdmin(admin.ModelAdmin):
    fields = ['SerialNum','Name','Type','Materials','Class','Note']
    list_display = ['id', 'Name', 'SerialNum', 'Type', 'Class', 'Note']
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum']
    list_filter = ['Type', 'Class']
    list_per_page = 15
    actions = [updateDetailOfModel]

    def get_actions(self, request):
        actions = super(CourseAdmin, self).get_actions(request)
        mod = actions['updateDetailOfModel']
        newMod = (mod[0], mod[1], mod[2] + " " + self.model._meta.verbose_name)
        actions['updateDetailOfModel'] = newMod
        return actions

class GradeAdmin(admin.ModelAdmin):
    fields = ['SerialNum', 'Name', 'LimitNum', 'Courses','Note']
    list_display = ['id', 'Name', 'SerialNum', 'studentNum', 'Note']
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum']
    list_per_page = 15
    actions = [updateDetailOfModel]

    def get_actions(self, request):
        actions = super(GradeAdmin, self).get_actions(request)
        mod = actions['updateDetailOfModel']
        newMod = (mod[0], mod[1], mod[2] + " " + self.model._meta.verbose_name)
        actions['updateDetailOfModel'] = newMod
        return actions

class StudentInfoAdmin(admin.ModelAdmin):
    fields = ['SerialNum', 'Name']
    list_display = ['id', 'Name', 'SerialNum', 'Gender', 'Age',"electiveCoursesNum","Email","Tel","Grade","Note"]
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum','Email','Tel']
    list_filter = ['Gender','Age','Grade']
    list_per_page = 15
    actions = [updateDetailOfModel]

    def get_actions(self, request):
        actions = super(StudentInfoAdmin, self).get_actions(request)
        mod = actions['updateDetailOfModel']
        newMod = (mod[0], mod[1], mod[2] + " " + self.model._meta.verbose_name)
        actions['updateDetailOfModel'] = newMod
        return actions

    def save_model(self, request, obj, form, change):
        obj.save()
        StudentInfo.createStudentUser(obj)



admin.site.register(Material,MaterialAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Grade,GradeAdmin)
admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.site_url='/admin'