from django.contrib import admin
from .models import TypeOf, Animal



class AnimalAdmin(admin.TabularInline):
	model = Animal

class AnimalAdminDab( admin.ModelAdmin):
	model = Animal

admin.site.register(Animal,AnimalAdminDab)

class TypeOfAdmin(admin.ModelAdmin):
	inlines=[AnimalAdmin]

	list_display = ['animalType']

admin.site.register(TypeOf, TypeOfAdmin)