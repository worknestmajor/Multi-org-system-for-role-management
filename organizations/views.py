from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Organization, CustomUser
from .forms import RegistrationForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

def homepage(request):
    organizations = Organization.objects.all()
    return render(request, 'homepage.html', {'organizations': organizations})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'VIEWER' 
            user.save()
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def organization_users(request, org_id):
    organization = Organization.objects.get(id=org_id)
    if request.user.organization != organization:
        return HttpResponseForbidden("You are not allowed to access this organization.")

    users = CustomUser.objects.filter(organization=organization)
    is_admin = request.user.role == 'ADMIN'

    return render(request, 'organization_users.html', {'organization': organization,'users': users, 'is_admin': is_admin})


def is_admin(user):
    return user.role == 'ADMIN'

@login_required
@user_passes_test(is_admin)
def assign_role(request, org_id):
    organization = Organization.objects.get(id=org_id)

    if request.user.organization != organization:
        return HttpResponseForbidden("You are not allowed to manage roles for this organization.")

    users = CustomUser.objects.filter(organization=organization)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        role = request.POST.get('role')
        try:
            user = CustomUser.objects.get(id=user_id, organization=organization)
            user.role = role
            user.save()
        except CustomUser.DoesNotExist:
            return HttpResponseForbidden("Invalid user.")
        return redirect('assign_role', org_id=org_id)

    return render(request, 'assign_role.html', {'users': users})

