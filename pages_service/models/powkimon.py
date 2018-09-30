from django.db import models
from django.contrib import admin


class Powkimon(models.Model):
	""" Sample model representing a little fighting monster

	This is a random model just to show how ot could works. Once loaded in database,
	every property inheriting from models will have their equivalent in the created table.
	"""
	number = models.IntegerField(max_length=2)
	name = models.CharField(max_length=64)
	type = models.CharField(max_length=256)
	level = models.IntegerField(2)


class PowkimonAdmin(admin.ModelAdmin):
	""" That is a model descriptor, specifying an admin interface configuration	"""

	# Selecting properties to display in the recap array:
	list_display = ['name', 'type']
	# Enable ordering on the following object properties:
	ordering = ['type']
	# Same thinkg, but for a research field:
	search_fields = ['name']
