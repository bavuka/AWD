from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self,request):
        return render(request,'dataentry/home.html')