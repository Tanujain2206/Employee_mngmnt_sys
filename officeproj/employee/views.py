from django.shortcuts import render,HttpResponse
from .models import department,role,employe
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'employee/index.html')

def view_emp(request):
    emps=employe.objects.all()
    return render(request,'employee/view_emp.html',{'emps':emps})

def add_emp(request):
    
    if request.method=='POST':
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        salary=int(request.POST['salary'])
        bonous=int(request.POST['bonous'])
        phn_no=int(request.POST['phn_no'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=employe(f_name=f_name,l_name=l_name,salary=salary,bonous=bonous,phn_no=phn_no,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("employee addedd successfully")
    elif request.method=="GET":
        return render(request,'employee/add_emp.html') 
    else:
        return HttpResponse("An exception occured") 
    
      
def remove(request,emp_id=0):
    if emp_id:
        try:
            emp_removed=employe.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse("employee id removed")
        except:
            return HttpResponse("enter valid id")
    emps=employe.objects.all()
    return render(request,'employee/remove.html',{'emps':emps})

def filter(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=employe.objects.all()
        if name:
            emps=emps.filter(Q(f_name__icontains=name) | Q(l_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept) 
        if role:
            emps=emps.filter(role__name=name)
        return render(request,'employee/view_emp.html',{'emps':emps})           
    elif request.method=="GET":
        return render(request,'employee/filter.html')
    else:
        HttpResponse("invalid")


