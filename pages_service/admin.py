from django.contrib import admin
from .models.powkimon import *


# For every registered model, it's interesting to specify an adminModel (second parameter)
admin.site.register(Powkimon, PowkimonAdmin)
