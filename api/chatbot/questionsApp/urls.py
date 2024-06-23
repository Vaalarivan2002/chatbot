from django.urls import path
from .views import getAnswer, initializeModel

app_name = "questionsApp"

urlpatterns = [
    path('initialize/', initializeModel),
    path('answers/', getAnswer),
]