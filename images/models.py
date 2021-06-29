from django.db import models


class TypeOf(models.Model):
        animalType = models.CharField(max_length=10)

        def __str__(self):
                return self.animalType

class vendorName(models.Model):
        name = models.CharField(max_length=15)

        def __str__(self):
                return self.name

class Animal(models.Model):
        typeOf = models.ForeignKey(TypeOf, on_delete=models.CASCADE)
        nameOfVendor = models.ForeignKey(vendorName, on_delete=models.CASCADE)

        name = models.CharField(max_length=20) 
        imgUrl = models.TextField()
        count = models.IntegerField()
        likedCount = models.IntegerField()
        isLiked = models.BooleanField(False)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        offers = models.DecimalField(max_digits=4, decimal_places=2)

        def __str__(self):
                return self.name
