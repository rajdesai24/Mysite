from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import person 
class create(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=person 
        fields= ('first_name','last_name','dp','bio',)
class change(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model=person
        fields=('dp','bio')