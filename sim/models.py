from django.db import models
from tm.models import Course
from tm.models import Grade
# Create your models here.
class StudentInfo(models.Model):
    Name = models.CharField("Name",max_length=15)
    SerialNum = models.CharField("StudentId",max_length=10,unique=True)
    Gender = models.PositiveSmallIntegerField("Gender",choices=((0,"female"),(1,"male")))
    Age = models.PositiveSmallIntegerField("Age")
    ElectiveCourses = models.ManyToManyField(Course,verbose_name="Elective Courses")
    Email = models.EmailField("Email",blank=True)
    Tel = models.CharField("Telephone Number",max_length=13,blank=True)
    Grade = models.ForeignKey(Grade,verbose_name="Grade",on_delete=models.SET_NULL,blank=True,null=True)
    Note = models.CharField("note",max_length=200)
    def __str__(self):
        return self.Name

class StudentUser(models.Model):
    studentInfo = models.OneToOneField(StudentInfo,on_delete=models.CASCADE,to_field="SerialNum")
    Password = models.CharField("password",max_length=10)
