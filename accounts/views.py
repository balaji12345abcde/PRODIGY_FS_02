from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

def signupview(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return render(request,'employee_list.html')
    return render(request,'signup.html',{'form':form})
def loginview(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return render(request,'employee_list.html')
    return render(request,'login.html',{'form':form})
def logoutview(request):
    logout(request)
    return redirect('login')
from django.shortcuts import get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q
@login_required
def employee_list(request):
    query = request.GET.get("q")
    if query:
        employees = Employee.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(position__icontains=query)
        )
    else:
        employees = Employee.objects.all()
    
    return render(request, "employee_list.html", {"employees": employees, "query": query})

# Employee detail page
@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "employee_detail.html", {"employee": employee})

# Create employee
@login_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "employee_form.html", {"form": form})

# Update employee
@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employee_form.html", {"form": form})

# Delete employee
@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request, "employee_confirm_delete.html", {"employee": employee})
