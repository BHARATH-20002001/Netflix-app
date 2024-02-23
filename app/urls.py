from django.urls import path
from app.views import *

app_name = 'app'
urlpatterns = [
    path('',login,name='login'),
    path('signup/',signup,name='signup'),
]