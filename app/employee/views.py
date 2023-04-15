from django.shortcuts import render
from app.employee.models import Employee

# Create your views here.
def index(request):
    employee_qs = Employee.objects.all()
    context = {
       'employee_qs': employee_qs
    }
    return render(request,'index.html',context)

def employee_detail(request,employee_id):
    employee_obj = Employee.objects.get(pk=employee_id)

    context = {
        'employee_obj': employee_obj
    }

    return render(request,'details.html',context)