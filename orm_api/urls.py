from django.urls import path
from . import views

app_name = 'orm_api'

urlpatterns = [
    path('', views.student_list, name='student_data'),
    
]