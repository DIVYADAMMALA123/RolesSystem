from django.shortcuts import render, redirect, get_object_or_404
from .models import Role
from .forms import RoleForm

def role_dashboard(request):
    roles = Role.objects.filter(status=True)
    return render(request, 'roles/dashboard.html', {'roles': roles})

def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('role_dashboard')
    else:
        form = RoleForm()
    return render(request, 'roles/form.html', {'form': form})

def edit_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_dashboard')
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/form.html', {'form': form})

def delete_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    role.status = False
    role.save()
    return redirect('role_dashboard')
