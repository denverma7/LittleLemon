from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu, MenuItem


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['ID', 'Title', 'Price', 'Inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='username',
        lookup_url_kwarg='username',
    )

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']