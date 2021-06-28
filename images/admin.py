from django.contrib import admin
from .models import TypeOf, Animal



class AnimalAdmin(admin.TabularInline):
	model = Animal

class TypeOfAdmin(admin.ModelAdmin):
	inlines=[AnimalAdmin]

	list_display = ['animalType']

admin.site.register(TypeOf, TypeOfAdmin)