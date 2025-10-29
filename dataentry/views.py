from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .utils import get_custom_models
from uploads.models import Upload

class ImportDataForm(View):
    def get(self,request):
        custom_models=get_custom_models
        return render(request,'dataentry/importdata.html',{"models":custom_models})
    def post(self,request):
        file_path=request.FILES.get("file_path")
        model_name=request.POST.get("model_name")
        upload=Upload.objects.create(file_path=file_path,model_name=model_name)
        return redirect("importdata")




# Create your views here.
