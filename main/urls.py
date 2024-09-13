from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_list, name='menu_list'),
    path('add/', views.add_menu, name='add_menu'),
    path('delete/<int:pk>/', views.delete_menu, name='delete_menu'),
    path('update/<int:pk>/', views.update_menu, name='update_menu'),
]
