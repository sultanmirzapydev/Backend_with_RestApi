from django.db import models


class TypeOf(models.Model):
        animalType = models.CharField(max_length=10)

        def __str__(self):
                return self.animalType

class vendorName(models.Model):
        name = models.CharField(max_length=15)
        avatar = models.TextField(null=True)
        

        def __str__(self):
                return self.name


class Animal(models.Model):
        typeOf = models.ForeignKey(TypeOf, related_name='typeOf', on_delete=models.CASCADE , null=True)
        vendor = models.ForeignKey(vendorName, related_name='vendor', on_delete=models.CASCADE, null=True)
        name = models.CharField(max_length=20, null=True) 
        description = models.TextField(null=True)
        imgUrl = models.TextField(null=True)

        count = models.IntegerField(null=True)
        total_liked = models.IntegerField(null=True)
        isLiked = models.BooleanField(default=False)
        price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
        offers = models.DecimalField(max_digits=4, decimal_places=2, null=True)

        def __str__(self):
                return self.name


