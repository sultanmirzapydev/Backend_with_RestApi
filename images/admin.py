from django.contrib import admin
from .models import  Image

class ImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'id', 'added_date')
	readonly_fields = ('added_date',)

admin.site.register(Image, ImageAdmin)
