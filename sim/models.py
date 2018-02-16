from django.db import models
from tm.models import StudentInfo
from django.contrib.auth.models import User
import hashlib
# Create your models here.


class StudentUser(models.Model):
    SerialNum = models.CharField("学号", max_length=15)
    Password = models.CharField("密码", max_length=15)
    Email = models.EmailField("邮箱", blank=True, null=True)
    studentInfo = models.OneToOneField(StudentInfo, on_delete=models.CASCADE)

    def is_authenticated(self):
        return True

    def hashed_password(self, password=None):
        if not password:
            return self.Password
        else:
            return hashlib.md5(password).hexdigest()

    def check_password(self, password):
        if self.hashed_password(password) == self.Password:
            return True
        return False

    # @staticmethod
    # def create_studentuser(studentinfo):
    #     obj = StudentUser.objects.get(SerialNum=studentinfo.SerialNum)
    #     if not obj :
    #         studentUser = StudentUser(SerialNum = studentinfo.SerialNum,Password='123456',studentInfo = studentinfo)
    #         user = User.objects.create_user(username=studentinfo.SerialNum, password='123456',email= studentinfo.Email)
    #         user.user_permissions.add(models.user.add)
    #         user.user_permissions.add(models.user.change)
    #         user.save()
    #         studentUser.save()
    #     return studentUser
