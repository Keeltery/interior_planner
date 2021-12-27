#from django.db import models
from django.db import models
from django.contrib.auth.models import User # Модель базового пользователя джанго
# Create your models here.


class Users(models.Model):
    ID = models.AutoField("User ID", auto_created=True, primary_key=True, max_length=1000)
    UserName = models.CharField('NickName', max_length=150, unique=True)
    password = models.CharField('Password', max_length=30, unique=True)
    email = models.EmailField(unique=True)

class Product(models.Model):
    ID = models.AutoField("Product ID", auto_created=True, primary_key=True, max_length=1000)
    name = models.CharField("Product name", max_length = 150, unique=True)
    TypeOfProduct = models.CharField("Type of furniture", max_length = 150, unique=True)
    ModelOfProduct = models.CharField("Furniture model", max_length = 150, unique=True)

class PurchaseHistory(models.Model):
    ID = models.AutoField("Product ID", auto_created=True, primary_key=True, max_length=1000)
    productname = models.CharField("Product name", max_length = 150, unique=True)
    date = models.DateTimeField()


    def get_participants(self):
        return EventUser.objects.filter(event=self)

class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Users, on_delete=models.CASCADE)
