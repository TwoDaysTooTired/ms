from django.contrib import admin
from sim.models import StudentUser
# Register your models here.

class StudentInfoAdmin(admin.ModelAdmin):
    fields = ['SerialNum', 'Name']
    list_display = ['id', 'Name', 'SerialNum', 'Gender', 'Age',"electiveCoursesNum","Email","Tel","Grade","Note"]
    list_display_links = ['Name']
    search_fields = ['Name', 'SerialNum','Email','Tel']
    list_filter = ['Gender','Age','Grade']
    list_per_page = 15

admin.site.register(StudentUser, StudentInfoAdmin)