from django.urls import path
from app.employee.views import index, employee_detail

app_name = 'Employee_App'

urlpatterns = [
    path('',index),
    path('details/<int:employee_id>/', employee_detail, name='employee_details'),
]