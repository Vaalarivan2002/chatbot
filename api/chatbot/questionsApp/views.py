from rest_framework.decorators import api_view
from rest_framework.response import Response
from .nlp.retrieveRelevantAnswers import retrieveRelevantAnswers, initializeEmbeddings
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
from datetime import datetime
from .models import Log
import csv

@api_view(['GET'])
def getAnswer(request):
    question = request.GET.get('question')

    if (question == ''):
        return Response({ "answers": 'Please provide a valid query!' })  

    time_before_operation = datetime.now()
    answer = retrieveRelevantAnswers(question=question)
    time_after_operation = datetime.now()
    duration = time_after_operation - time_before_operation

    log_object = Log(question=question, answer=answer, time_to_generate_answer=duration, question_timestamp=time_before_operation)

    log_object.save()
    
    return Response({ "answers": answer })

@api_view(['GET'])
def initializeModel(request):
    try:
        initializeEmbeddings()
        return Response({ "operation": 'success' })
    except Exception as e:
        return Response({ "operation": "Something went wrong!" })
    