from django import forms
from tm.models import Grade
from tm.models import StudentInfo

class MaterialStorageForm(forms.Form):
    Num = forms.IntegerField(label="数量",required=True,min_value=1,max_value=200,error_messages={'required': 'can not be empty','min_value':'vale can not < 1','max_value': 'max value is 200'})
    Note = forms.CharField(label="备注",required=False,max_length=200)


class MaterialAllocForm(forms.Form):
    def __init__(self,studentsChocies = None, *args,**kwargs):
        super(MaterialAllocForm, self).__init__(*args,**kwargs)
        if studentsChocies:
            self.fields['Students'] = forms.ModelMultipleChoiceField(label="学生",queryset= studentsChocies)

    Grade = forms.ModelChoiceField(label="班级",queryset = Grade.objects.all())
    Students = forms.ModelMultipleChoiceField(label="学生",queryset= StudentInfo.objects.all())
    Note = forms.CharField(label="备注", required=False, max_length=200)


