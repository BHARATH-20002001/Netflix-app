from django.urls import path
from app.views import *

app_name = 'app'
urlpatterns = [
    
    path('index/',index,name='index'),
    path('',login,name='login'),
    path('signup/',signup,name='signup'),
    path('my_list/',my_list,name='my_list'),
    
    
]