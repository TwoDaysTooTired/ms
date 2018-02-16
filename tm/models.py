from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Material(models.Model):
    SerialNum = models.CharField("MaterialId",max_length=15,unique=True)
    Name = models.CharField("MaterialName",max_length=15)
    Type = models.IntegerField("MaterialType",choices=((0,"Book"),(1,'WorkBook'),(2,'ExperimentEquipMent'),(3,'Other')))
    InventoryLimitNum = models.PositiveSmallIntegerField("InventoryLimit",default=50)
    InventoryNum = models.PositiveSmallIntegerField("InventoryNum",default=0)
    Price = models.PositiveSmallIntegerField("Price")
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
    def __str__(self):
        return self.Name

class Grade(models.Model):
    SerialNum = models.CharField("GradeId",max_length=15,unique=True)
    Name = models.CharField("GradeName",max_length=15)
    LimitNum = models.PositiveSmallIntegerField("MaxNum",default=50)
    Courses = models.ManyToManyField(Course,verbose_name="Base Courses",blank=True)
    Note = models.CharField("Grade Description", max_length=200, blank=True)
    hasAllocNum = models.PositiveSmallIntegerField("AllocedNum",default=0)
    def __str__(self):
        return self.Name
    def studentNum(self):
        return  self.studentinfo_set.count()
    studentNum.short_description = "Num of Student"

    def materials(self):
        material_list = []
        for course in self.Courses.all():
            for materail in course.Materials.all():
                material_list.append(materail)
        return material_list
    def isEnoughN(self):
        for material in self.materials():
            if material.InventoryNum < self.studentNum():
                return False
        return True
    def fullNum(self):
        return self.studentNum() * len(self.materials())
    def isFullAlloc(self):
        return self.hasAllocNum >= self.fullNum()

    def alloc(self):
        studentNum = self.studentNum()
        for material in self.materials():
            material.InventoryNum -= studentNum
            MaterialAllocModel.objects.create(Material=material,Num=studentNum)
            self.hasAllocNum += studentNum
            material.save()
        self.save()



class StudentInfo(models.Model):
    Name = models.CharField("Name",max_length=15)
    SerialNum = models.CharField("StudentId",max_length=10,unique=True)
    Gender = models.PositiveSmallIntegerField("Gender",choices=((0,"female"),(1,"male")),null=True,blank=True)
    Age = models.PositiveSmallIntegerField("Age",null=True,blank=True)
    ElectiveCourses = models.ManyToManyField(Course,verbose_name="Elective Courses")
    Email = models.EmailField("Email",blank=True,null=True)
    Tel = models.CharField("Telephone Number",max_length=13,blank=True,null=True)
    Grade = models.ForeignKey(Grade,verbose_name="Grade",on_delete=models.SET_NULL,blank=True,null=True)
    Note = models.CharField("note",max_length=200,null=True, blank=True)
    actionDetail = '/student/detail/'
    actionChangeInfo = "/student/change/"
    actionChangePassword = '/changePassword/'
    actionChangeGrade = '/chooseCources/'

    def __str__(self):
        return self.Name

    def electiveCoursesNum(self):
        return self.ElectiveCourses.count()

    @staticmethod
    def createStudentUser(self):
        if  User.objects.filter(username=self.SerialNum).count() == 0 :
            user = User.objects.create_user(username=self.SerialNum, password='123456', email=self.Email)
            user.save()

class MaterialStorageModel(models.Model):
    Num = models.PositiveSmallIntegerField('num')
    Material = models.ForeignKey(Material,on_delete=models.CASCADE,blank=False)
    Data = models.DateTimeField('data time',auto_now_add=True)
    Note = models.CharField('note',max_length=200,blank=True,null=True)
    def __str__(self):
        return self.id
    def get_admin_url(self):
        return "/login/success"

class MaterialAllocModel(models.Model):
    Num = models.PositiveSmallIntegerField('num')
    Material = models.ForeignKey(Material,on_delete=models.CASCADE,blank=False)
    Data = models.DateTimeField('data time', auto_now_add=True)
    Note = models.CharField('note', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Material.Name + self.Num

