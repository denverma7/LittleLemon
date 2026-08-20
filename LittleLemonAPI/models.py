from django.db import models


class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class MenuItem(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.Title}: {self.Price}'

    def get_item(self):
        return f'{self.Title} : {str(self.Price)}'


class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_Guests = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return self.Name

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username