from django.contrib import admin

from .models import Question


# Register model to admin site.
admin.site.register(Question)