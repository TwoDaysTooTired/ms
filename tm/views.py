from django.shortcuts import render
from django.views.generic import ListView, DetailView,FormView, CreateView
from .models import Material,MaterialAllocModel,MaterialStorageModel,Grade
from django.http import Http404,HttpResponse
from .form import  MaterialStorageForm
# Create your views here.
class MaterialListView(ListView):
    model = Material

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)
        return context

class GradeListView(ListView):
    model =  Grade

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GradeListView, self).get_context_data(**kwargs)
        return context


class MaterialEntryListView(ListView):
    model = MaterialStorageModel

class MaterialOutBoundListView(ListView):
    model = MaterialAllocModel


def materialStorage(request):
    material = Material.objects.get(id=request.GET['mid'])
    if material:
        if request.method == 'GET':
            f = MaterialStorageForm()
            return render(request,'tm/materialstorage_form.html',{'form':f,'material':material})
        else:
            f= MaterialStorageForm(request.POST)
            if f.is_valid():
                num = f.cleaned_data['Num']
                note = f.cleaned_data['Note']
                material.InventoryNum +=num
                material.save()
                MaterialStorageModel.objects.create(Num=num,Note=note,Material=material)
                return render(request, 'tm/materialstorageSuccess.html',{'material':material,'num':num})
        return Http404()


def allocMaterial(request):
    grade = Grade.objects.get(id=request.GET['gid'])
    if grade:
        if request.method == 'GET':
            material_list = grade.materials()
            isEnogh = grade.isEnoughN()
            return render(request,'tm/gradealloc.html',{'grade':grade,'material_list':material_list,'isEnough':isEnogh})
        else:
            grade.alloc()
            return render(request, 'tm/materialstorageSuccess.html',{'grade':grade})
    return Http404()



