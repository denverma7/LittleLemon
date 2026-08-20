from django.urls import path
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    path('bookings/', views.BookingView.as_view()),

    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('registration/', DjoserUserViewSet.as_view({'post': 'create'}), name='registration'),

    path('user/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('user/<str:username>/', views.UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='user-detail'),
]