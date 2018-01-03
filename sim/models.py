from django.db import models
from tm.models import StudentInfo
# Create your models here.


class StudentUser(models.Model):
    studentInfo = models.OneToOneField(StudentInfo,on_delete=models.CASCADE,to_field="SerialNum")
    Password = models.CharField("password",max_length=10)
