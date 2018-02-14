from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django import forms
from django.contrib import auth
# Create your views here.
from tm.models import StudentInfo
from sim.models import StudentUser
class StudentUserForm(forms.Form):
    SerialNum = forms.CharField(label='StudentId',max_length=15)
    Password = forms.CharField(label="Password",max_length=15)
    
class StudentUserLoginView(View):
    def get(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username = username, password = password)
        if request.POST:
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse("loginSuccess")
            else:
                return render(request,"sim/login.html", {'form.errors':"wrong u sername or password"})
        else:
            return render(request, 'sim/login.html', {'next':'admin'})


def loginSuccess(request):
    if request.method == "GET":
        serialNum = request.user.username;
        student = StudentInfo.objects.get(SerialNum=serialNum)
        if student:
            return render(request, "sim/loginSuccess.html", {'student' : student})
        return HttpResponse("error")