from django.db import models
import datetime

# Create your models here.

class ListingList(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Listing(models.Model):
    listingList = models.ForeignKey(ListingList, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    listingType = models.CharField(max_length=50)
    dateCreated = models.DateField(default=datetime.date.today)
    dateAvailable = models.DateField()
    price = models.IntegerField()
    phoneNumber = models.CharField(max_length=20)
    contacts = models.CharField(max_length=300)



