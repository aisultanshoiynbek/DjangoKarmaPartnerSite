from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    discription = models.TextField(blank=True)
    city = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    role = models.ForeignKey('Rol', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return (self.name,self.secondName)





class Rol(models.Model):
    roleName = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.roleName


class Goal(models.Model):
    goalName = models.CharField(max_length=255)
    goalDescription = models.TextField(blank=True)
    goalCategory = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    availableTime = models.CharField(max_length=255)

    def __str__(self):
        return self.goalName

    def get_absolute_url(self):
        return reverse('goal', kwargs = {post_id: self.pk})

class Category(models.Model):
    nameCategory = models.CharField(max_length=255, db_index=True, default='partner')

    def __str__(self):
        return self.nameCategory