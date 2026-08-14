from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, MenuItem
from .serializers import MenuItemSerializer, BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingsView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def index(request):
    return render(request, 'index.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def menu_item(request, pk):
    return render(request, 'menu_item.html', {'pk': pk})