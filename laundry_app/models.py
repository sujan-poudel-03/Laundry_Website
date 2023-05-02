from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Catogary_name(models.Model):
    catg_name = models.CharField(max_length=265, unique=True)

    def __str__(self):
        return self.catg_name


class Item_detail(models.Model):
    Catogary   = models.CharField(max_length=50, default=" ")
    Item_name = models.CharField(max_length=50, default=" ")
    Washing_price = models.CharField(max_length=50, default="")
    Dryclean_price =  models.CharField(max_length=50, default="")

    def __str__(self):
        return self.Item_name

class Branch(models.Model):
    Name = models.CharField(max_length=50, default=" ")
    Service_Available = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return self.Name

class ClientDetail(models.Model):
    Client_Id = models.AutoField(primary_key=True) 
    First_Name = models.CharField(max_length=50, default="")
    Last_Name = models.CharField(max_length=50, default="")
    Address = models.CharField(max_length=80, default="")
    Subscription_Package = models.CharField(max_length=30, default="")
    Phone = models.CharField(max_length=50, default=" ")
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=50, default="")
    Conform_Password = models.CharField(max_length=50, default=" ")

    def __str__(self):
        return str(self.Client_Id) +" : " + self.First_Name +"   "+self.Last_Name +"  "+ str(self.Phone)

# Learn Section
# -------------------- 

class person(models.Model):
    firstName = models.CharField(max_length=255, default=" ")
    lastName = models.CharField(max_length=255, default= " ")
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.firstName +"  "+ self.lastName + " :- " + self.email

class modelForm(models.Model):
    pass


class registeration(models.Model):
    Username = models.CharField(max_length=50,default="")
    Password = models.CharField(max_length=50,default="")
    CPassword = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.Username +" & " + self.Password

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

# FILE UPLOAD TUTORIAL
class uploadFile(models.Model):
    htmlupload = models.FileField()
    formupload = models.FileField()
    modelupload = models.FileField(upload_to='upload_file')

class CRUD(models.Model):
    StudentId = models.CharField(max_length=50)  
    StudentName = models.CharField(max_length=50)
    StudentPhone = models.CharField(max_length=50)
    Birthday = models.DateField(blank = True)

    def __str__(self):
        return self.StudentId +' '+ self.StudentName