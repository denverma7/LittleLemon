from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-item-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item-detail-items'),
]
