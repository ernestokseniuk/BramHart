from django.db import models
from django.utils import timezone
class MainCategory(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="media/kategorie")
    visited = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Category(models.Model):
    category = models.ForeignKey(MainCategory, on_delete = models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="media/podkategorie")
    visited = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Object(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="media/images")
    visited = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Ratings(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=40)
    Rate = models.IntegerField(default=5)
    Text = models.TextField(max_length=200, blank = True)
    pub_date = models.DateTimeField(auto_now_add=True)
    Is_Deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.Text

class Contact(models.Model):
    brandName = models.CharField(max_length=126)
    email = models.EmailField()
    telefon = models.CharField(max_length=12)
    adres = models.CharField(max_length=126)
    def __str__(self):
        return "Dane kontaktowe"

class Messages(models.Model):
    deleted = models.BooleanField(default=False)
    opened = models.BooleanField(default=False)
    author = models.TextField(max_length=64)
    phone = models.TextField(max_length=13)
    email = models.TextField(max_length=64)
    text = models.TextField(max_length=2048)
    pub_date = models.DateTimeField(auto_now_add=True)

class Done(models.Model):
    fences = models.IntegerField(default=0)
    people = models.IntegerField(default=0)
    construction = models.IntegerField(default=0)

class Context(models.Model):
    Onas = models.TextField()

