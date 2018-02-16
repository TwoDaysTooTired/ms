from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Material(models.Model):
    SerialNum = models.CharField("材料编号",max_length=15,unique=True)
    Name = models.CharField("材料名",max_length=15)
    Type = models.IntegerField("材料类型",choices=((0,"书"),(1,'工作簿'),(2,'实验器材'),(3,'其他')))
    InventoryLimitNum = models.PositiveSmallIntegerField("最大库存",default=50)
    InventoryNum = models.PositiveSmallIntegerField("库存数量",default=0)
    Price = models.PositiveSmallIntegerField("价格")
    Note = models.CharField("备注",blank=True,max_length=200)
    def __str__(self):
        return self.Name
    def isOverflow(self):
        return self.InventoryNum > self.InventoryLimitNum
    class Meta:
        verbose_name = '材料'
        verbose_name_plural = '材料'


class Course(models.Model):
    SerialNum = models.CharField("课程编号",max_length=15,unique=True)
    Name = models.CharField("课程名",max_length=15)
    Materials = models.ManyToManyField(Material,verbose_name="教学材料",blank=True)
    Type = models.IntegerField("课程类型",choices=((0,'室内'),(1,'练习'),(2,'视屏')))
    Class = models.PositiveSmallIntegerField("类",default=20)
    Note = models.CharField("课程描述",max_length=200,blank=True)
    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
    def __str__(self):
        return self.Name


class Grade(models.Model):
    SerialNum = models.CharField("班级编号",max_length=15,unique=True)
    Name = models.CharField("班级名",max_length=15)
    LimitNum = models.PositiveSmallIntegerField("最大人数",default=50)
    Courses = models.ManyToManyField(Course,verbose_name="基础课程",blank=True)
    Note = models.CharField("班级描述", max_length=200, blank=True)
    hasAllocNum = models.PositiveSmallIntegerField("已分配数",default=0)
    def __str__(self):
        return self.Name
    def studentNum(self):
        return  self.studentinfo_set.count()
    studentNum.short_description = "Num of Student"
    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

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
    Name = models.CharField("姓名",max_length=15)
    SerialNum = models.CharField("学号",max_length=10,unique=True)
    Gender = models.PositiveSmallIntegerField("性别",choices=((0,"female"),(1,"male")),null=True,blank=True)
    Age = models.PositiveSmallIntegerField("年龄",null=True,blank=True)
    ElectiveCourses = models.ManyToManyField(Course,verbose_name="选修课")
    Email = models.EmailField("邮箱",blank=True,null=True)
    Tel = models.CharField("电话号码",max_length=13,blank=True,null=True)
    Grade = models.ForeignKey(Grade,verbose_name="班级",on_delete=models.SET_NULL,blank=True,null=True)
    Note = models.CharField("备注",max_length=200,null=True, blank=True)
    actionDetail = '/student/detail/'
    actionChangeInfo = "/student/change/"
    actionChangePassword = '/changePassword/'
    actionChangeGrade = '/chooseCources/'
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

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
    Num = models.PositiveSmallIntegerField('数量')
    Material = models.ForeignKey(Material,verbose_name='材料',on_delete=models.CASCADE,blank=False)
    Data = models.DateTimeField('日期时间',auto_now_add=True)
    Note = models.CharField('备注',max_length=200,blank=True,null=True)
    def __str__(self):
        return self.id
    def get_admin_url(self):
        return "/login/success"
    class Meta:
        verbose_name = '材料入库记录'
        verbose_name_plural = '材料入库记录'


class MaterialAllocModel(models.Model):
    Num = models.PositiveSmallIntegerField('数量')
    Material = models.ForeignKey(Material,verbose_name='材料',on_delete=models.CASCADE,blank=False)
    Data = models.DateTimeField('日期时间', auto_now_add=True)
    Note = models.CharField('备注', max_length=200, blank=True, null=True)
    class Meta:
        verbose_name = '材料分配记录'
        verbose_name_plural = '材料分配记录'

    def __str__(self):
        return self.Material.Name + self.Num


