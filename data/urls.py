from django.urls import path,include
from  .views import homepage,signup,login 
from django.contrib import auth
urlpatterns= [ 
    path('home/',homepage.as_view(),name='home'),
    path('signup/',signup.as_view(),name='signup'),
    path('',login.as_view(),name='login' )
]