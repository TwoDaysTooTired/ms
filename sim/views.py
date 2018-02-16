from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
from django.http import HttpResponse,Http404
from django import forms
from django.contrib import auth
# Create your views here.
from tm.models import StudentInfo,Material
from sim.form import StudentInfoForm, PasswordChangeForm, StudentCoursesChooseForm

from django.shortcuts import get_object_or_404

    
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

def detailInfo(requst):
    serialNum = requst.user.username;
    student = StudentInfo.objects.get(SerialNum=serialNum)
    if student:
        return render(requst, "sim/detail.html",{'student':student})
    return HttpResponse("error")


def changeInfo(request):
    serialNum = request.user.username
    student = StudentInfo.objects.get(SerialNum=serialNum)
    if student:
        if request.method == "GET":
            f = StudentInfoForm(instance=student)
            return render(request, "sim/changeInfo.html",{'student':student,'form':f})
        else:
            f = StudentInfoForm(request.POST)
            if f.is_valid():
                student.Email = f.cleaned_data['Email']
                student.Name = f.cleaned_data['Name']
                student.Gender = f.cleaned_data['Gender']
                student.Grade = f.cleaned_data['Grade']
                student.Age = f.cleaned_data['Age']
                student.Tel  = f.cleaned_data['Tel']
                student.Note = f.cleaned_data['Note']
                student.save()
                return render(request, "sim/loginSuccess.html", {'student': student})
            return render(request, "sim/changeInfo.html", {'student': student, 'form': f})
        return HttpResponse("error")

def changePassword(request):
    serialNum = request.user.username
    student = StudentInfo.objects.get(SerialNum=serialNum)
    if student:
        if request.method == "GET":
            f = PasswordChangeForm()
            f.username = serialNum
            return render(request, "sim/changePwd.html",{'student':student,'form':f})
        else:
            f = PasswordChangeForm(request.POST)
            if f.is_valid():
                oldpwd = f.cleaned_data['oldPassword']
                newpwd = f.cleaned_data['newPassword']
                confirmpwd = f.cleaned_data['confirmPassword']
                obj = auth.authenticate(username =serialNum,password=oldpwd)
                if obj:
                    if newpwd == confirmpwd:
                        request.user.set_password(newpwd)
                        request.user.save()
                        return render(request,template_name='sim/changePwdSuccess.html')
                    else:
                        msg = "Entered passwords differ"
                        f.initial = {'oldPassword':oldpwd,'newPassword':newpwd,'confirmPassword':confirmpwd}
                        return render(request, "sim/changePwd.html",{'form':f,'errors':msg})
                else:
                    msg = "Original password error"
                    f.initial = {'oldPassword': oldpwd, 'newPassword': newpwd, 'confirmPassword': confirmpwd}
                    return render(request, "sim/changePwd.html", {'student':student,'form': f,'errors':msg})
            else:
                return render(request, "sim/changePwd.html", {'student':student,'form': f})
        return HttpResponse("error")

def choseCources(request):
    serialNum = request.user.username
    student = StudentInfo.objects.get(SerialNum=serialNum)
    if student:
        if request.method == "GET":
            f = StudentCoursesChooseForm(instance=student)
            return render(request,'sim/choseCources.html', {'student':student,'form':f})
        else:
            f = StudentCoursesChooseForm(request.POST)
            if f.is_valid():
                cources = f.cleaned_data['ElectiveCourses']
                student.ElectiveCourses.clear()
                for cource in cources:
                    student.ElectiveCourses.add(cource)
                student.Grade = f.cleaned_data['Grade']
                student.save()
                return redirect('/student/detail/')
    return Http404("error")

def materailsDetail(request):
    materials = Material.objects.all()
    return render(request, "tm/material_list.html", {'materail_list':materials})

def materailAdd(request):
    return Http404("error")




