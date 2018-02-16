from django import forms


class MaterialStorageForm(forms.Form):
    Num = forms.IntegerField(required=True,min_value=1,max_value=200,error_messages={'required': 'can not be empty','min_value':'vale can not < 1','max_value': 'max value is 200'})
    Note = forms.CharField(required=False,max_length=200)
