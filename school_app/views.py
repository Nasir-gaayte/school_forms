from django.shortcuts import render,redirect
# from .forms import SchoolForm,StudentForm
from . import models
from django.contrib import messages
from django.views.generic import View,TemplateView,DeleteView,ListView
# Create your views here.


def base(request):
    return render(request, 'school_app/home.html')
# def home(request):
#     return render(request, 'school_app/home.html')

class HomeView(ListView):
    
    model = models.School
    


class HomeDetailView(DeleteView):
    model = models.School
    template_name = 'school_app/detail.html'
    
    

def register_req(request):
    return render(request, 'school_app/register.html')
#     if request.method == 'POST':
#         a_form = SchoolForm(request.POST)
#         b_form = StudentForm(request.POST)
#         if a_form.is_valid() and b_form.is_valid():
#             a_form.save(commit=True)
#             b_form.save(commit=True)
#             messages.success(request,"you save new student")
#             return redirect('home')
#         else:
#             messages.error(request,"somthin gos wrong")
#             return redirect('register')
#     a_form = SchoolForm
#     b_form = StudentForm
#     return render(request, 'school_app/register.html',{
#         'a_form':a_form,
#         'b_form':b_form 
#     })    