from django.shortcuts import render
from .models import person
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView
from .forms import create
from django.contrib.auth.views import LoginView
class homepage(ListView):
    model= person
    template_name='home.html'
class signup(CreateView):
    model=person
    fields=['first_name','last_name','dp','bio']
    reverse_lazy('login')
    template_name='signup.html'
class login(LoginView):
    model=person
    
# Create your views here.
