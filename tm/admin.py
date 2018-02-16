from django.contrib import admin
from .models import Material
from .models import Course
from .models import Grade
from .models import StudentInfo
from .models import MaterialStorageModel
from django.contrib.auth.models import User
from sim.models import StudentUser
# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    fields = ['SerialNum','Name','Type','InventoryLimitNum','Price','Note']
    list_display = ['id','Name','SerialNum','Type','InventoryNum','Price','Note']
    list_display_links = ['Name']
    search_fields = ['Name','SerialNum']
    list_filter = ['Type','Price']
    list_per_page = 15

class CourseAdmin(admin.ModelAdmin):
    fields = ['SerialNum','Name','Type','Materials','Class','Note']
    list_display = ['id', 'Name', 'SerialNum', 'Type', 'Class', 'Note']
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum']
    list_filter = ['Type', 'Class']
    list_per_page = 15

class GradeAdmin(admin.ModelAdmin):
    fields = ['SerialNum', 'Name', 'LimitNum', 'Courses','Note']
    list_display = ['id', 'Name', 'SerialNum', 'studentNum', 'Note']
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum']
    list_per_page = 15

class StudentInfoAdmin(admin.ModelAdmin):
    fields = ['SerialNum', 'Name']
    list_display = ['id', 'Name', 'SerialNum', 'Gender', 'Age',"electiveCoursesNum","Email","Tel","Grade","Note"]
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum','Email','Tel']
    list_filter = ['Gender','Age','Grade']
    list_per_page = 15

    def save_model(self, request, obj, form, change):
        obj.save()
        StudentInfo.createStudentUser(obj)







admin.site.register(Material,MaterialAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Grade,GradeAdmin)
admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.site_url='/admin'