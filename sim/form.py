from django import forms
from django.forms import ModelForm
from tm.models import StudentInfo
class StudentInfoForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = ('Name','Gender','Grade','Age','Email','Tel','Note')

class StudentCoursesChooseForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = ('ElectiveCourses','Grade')
        widgets = {
            'ElectiveCourses': forms.CheckboxSelectMultiple(attrs={'class': "form-control"}),
        }

class PasswordChangeForm(forms.Form):
    oldPassword = forms.CharField(widget=forms.PasswordInput(),label="old password:",min_length=6,max_length=16,required=True,strip=True,
                                  error_messages={'required': 'can not be empty','min_length':'password length needd > 6','max_length': 'password lenght must  < 16'})
    newPassword = forms.CharField(widget=forms.PasswordInput(),label="old password:",min_length=6,max_length=16,required=True,strip=True,
                                  error_messages={'required': 'can not be empty','min_length':'password length needd > 6','max_length': 'password lenght must  < 16'})
    confirmPassword = forms.CharField(widget=forms.PasswordInput(),label="old password:",min_length=6,max_length=16,required=True,strip=True,
                                  error_messages={'required': 'can not be empty','min_length':'password length needd > 6','max_length': 'password lenght must  < 16'})
