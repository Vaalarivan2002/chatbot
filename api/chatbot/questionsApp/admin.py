from django.contrib import admin
from .models import Question, Log

# Register your models here.
admin.site.register([Question, Log])