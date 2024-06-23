from django.urls import path
from .views import addQuestionAnswer, getLog

app_name = "doubtSupport"

urlpatterns = [
    path('add-new-question/', addQuestionAnswer),
    path('get-log/', getLog),
]