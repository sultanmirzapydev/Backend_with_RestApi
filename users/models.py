from django.db import models

# Create your models here.

#class Meta:
#	db_table='tablename'


class Images(models.Model):
	uploader_name = models.CharField(max_length=150)
	image         = models.ImageField(upload_to='api_images/')
	profile_pic   = models.ImageField(upload_to='api_images/propic/')