from django.db import models
# Create your models here.
class Material(models.Model):
    SerialNum = models.CharField("MaterialId",max_length=15,unique=True)
    Name = models.CharField("MaterialName",max_length=15)
    Type = models.IntegerField("MaterialType",choices=((0,"Book"),(1,'WorkBook'),(2,'ExperimentEquipMent'),(3,'Other')))
    InventoryLimitNum = models.PositiveSmallIntegerField("InventoryLimit",default=50)
    InventoryNum = models.PositiveSmallIntegerField("InventoryNum",default=0)
    Price = models.PositiveSmallIntegerField("Price",blank=True)
    Note = models.CharField("Note",blank=True,max_length=200)
    def __str__(self):
        return self.Name
    def isOverflow(self):
        return self.InventoryNum > self.InventoryLimitNum

class Course(models.Model):
    SerialNum = models.CharField("CourseId",max_length=15,unique=True)
    Name = models.CharField("CourseName",max_length=15)
    Materials = models.ManyToManyField(Material,verbose_name="Teach Materilas",blank=True)
    Type = models.IntegerField("Course Type",choices=((0,'ClassRoom'),(1,'Practice'),(2,'Video')))
    Class = models.PositiveSmallIntegerField("Class",default=20)
    Note = models.CharField("Course Description",max_length=200,blank=True)


class Grade(models.Model):
    SerialNum = models.CharField("GradeId",max_length=15,unique=True)
    Name = models.CharField("GradeName",max_length=15)
    LimitNum = models.PositiveSmallIntegerField("MaxNum",default=50)
    Courses = models.ManyToManyField(Course,verbose_name="Base Courses",blank=True)
    Note = models.CharField("Grade Description", max_length=200, blank=True)
    def __str__(self):
        return self.Name
    def studentNum(self):
        return  self.studentinfo_set.count()
    studentNum.short_description = "Num of Student"



