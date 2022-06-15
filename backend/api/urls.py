from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todo-list/', views.ShowAll),
    path('todo-detail/<int:pk>/', views.ViewProduct),
    path('todo-bool/<int:pt>/', views.ViewBool),
    path('todo-create/', views.CreateProduct),
    path('todo-update/<int:pk>/', views.updateProduct),
    path('todo-delete/<int:pk>/', views.deleteProduct),
]
