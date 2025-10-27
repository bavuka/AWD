from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .utils import get_custom_models

class ImportDataForm(View):
    def get(self,request):
        custom_models=get_custom_models
        return render(request,'dataentry/importdata.html',{"models":custom_models})
    def post(self,request):
        pass




# Create your views here.
