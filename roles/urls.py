from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_dashboard, name='role_dashboard'),
    path('add/', views.add_role, name='add_role'),
    path('edit/<int:pk>/', views.edit_role, name='edit_role'),
    path('delete/<int:pk>/', views.delete_role, name='delete_role'),
]
