from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('organization/<int:org_id>/', views.organization_users, name='organization_users'),
    path('organization/<int:org_id>/assign_role/', views.assign_role, name='assign_role'),

]

