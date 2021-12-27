from django.shortcuts import render, redirect

from staff.forms import *
from staff.models import *


# # получение данных из бд
def post_list_by_department(request):
    department = None
    departments = Department.objects.all()
    context = {'department': department, 'departments': departments}
    return render(request, 'post_list_by_department.html', context)


def post_employees(request):
    post = None
    posts = Post.objects.all()
    context = {'post': post, 'posts': posts}
    return render(request, 'post_employees.html', context)


def employees_detail(request):
    employees = None
    employees = Employees.objects.all()
    context = {'employees': employees}
    return render(request, 'employees_detail.html', context)


# сохранение данных в бд
def create_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:post_list_by_department')
    else:
        form = DepartmentForm()
    return render(request, 'post_list_by_department.html', {'form': form, })


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:post_employees')
    else:
        form = PostForm()
    return render(request, 'post_employees.html', {'form': form, })


def create_employees(request):
    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff:employees_detail')
    else:
        form = EmployeesForm()
    return render(request, 'employees_detail.html', {'form': form, })


# # изменение данных в бд
def edit_employees(request):
    employees = Employees.objects.get(id=request.GET.get('id'))
    if request.method == "POST":
        form = EditEmployeesForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect('staff:employees_detail')
    else:
        form = EditEmployeesForm(instance=employees)
    context = {'form': form, "employees": employees, }
    return render(request, 'edit_employees_detail.html', context)


# # удаление данных из бд
def delete_department(request):
    Department.objects.filter(id=request.GET.get('id')).delete()
    return redirect('staff:post_list_by_department')


def delete_post(request):
    Post.objects.filter(id=request.GET.get('id')).delete()
    return redirect('staff:post_employees')


def delete_employees(request):
    Employees.objects.filter(id=request.GET.get('id')).delete()
    return redirect('staff:employees_detail')
