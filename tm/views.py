from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,FormView, CreateView
from .models import Material,MaterialAllocModel,MaterialStorageModel,Grade
from django.http import Http404,HttpResponse,JsonResponse
from .form import  MaterialStorageForm
from .form import  MaterialAllocForm
from .models import StudentInfo
import json
from django.shortcuts import render_to_response
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

def materialAlloc(request):
    cascade_select_list = [('Grade', 'Students', Grade, StudentInfo),
                           ""]
    if request.is_ajax():
        # id = request.POST.get("grade_id")
        # grade = Grade.objects.get(SerialNum=id)
        # students = StudentInfo.objects.filter(Grade=grade)
        # f= MaterialAllocForm(studentsChocies=students, initial={'Grade':grade})

        return handle_cascade_select(request,MaterialAllocForm,cascade_select_list,"isAlloc = 0")
    elif request.method == "GET":
        f = MaterialAllocForm()
        return render(request,'tm/materialAlloc.html', {"form":f,"cascade_select_list":cascade_select_list})
    else:
        f = MaterialAllocForm(request.POST)
        if f.is_valid():
            num = f.cleaned_data['Num']
            note = f.cleaned_data['Note']
            return render(request, 'tm/materialstorageSuccess.html')


def allocdetail(request):
    materialNames = {}
    allMaterial = []
    if request.GET:
        lists=  json.loads(request.GET.get('id_list'))
        for studentId in lists:
            student = StudentInfo.objects.all().get(Name=studentId)
            if student is not None:
                gradeMaterials = student.Grade.materials()
                electiveCoursesmaterials = student.electiveCoursesMaterials()
                materials = student.allMaterial()
                for material in materials:
                    allMaterial.append(material)
                    if materialNames.get(material.Name):
                        materialNames[material.Name] +=1
                    else:
                        materialNames[material.Name] = 1

        ##comment_json = json.dumps(materialNames,ensure_ascii=False)
        AllMaterial = list(set(allMaterial))
        MaterialEnough = {}
        MaterialNums = {}
        for material in AllMaterial:
                remainCount = material.InventoryNum
                needCount = materialNames[material.Name]
                MaterialEnough[material.Name] = 1 if remainCount >= needCount else 0
                MaterialNums[material.Name] = remainCount

        jsonData = {'n':materialNames,'v':MaterialEnough,'s':MaterialNums}
        return JsonResponse(jsonData)
    return Http404("error")


def handle_cascade_select(request, form_class, cascade_select_list,otherfilter = None):
    cascade_select_list.pop()
    form =form_class()
    for event_element, filter_element, event_model, filter_model in cascade_select_list:
        if event_element in request.GET:
            try:
                event_element_object = get_object_or_404(event_model, id = int(request.GET[event_element]))
            except Exception:
                form.fields[filter_element].queryset = filter_model.objects.none()
            else:
                if otherfilter:
                    condition = ['%s_id = %s  and %s' % (event_element, event_element_object.id, otherfilter)]
                    form.fields[filter_element].queryset = filter_model.objects.extra(where=condition)
                else:
                    form.fields[filter_element].queryset = filter_model.objects.extra(
                        where=['%s_id = %s' % (event_element, event_element_object.id)] )
            return HttpResponse(str(form[filter_element]))


