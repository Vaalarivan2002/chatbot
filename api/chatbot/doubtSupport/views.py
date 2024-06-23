from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from questionsApp.models import Question, Log
from questionsApp.nlp.retrieveRelevantAnswers import initializeEmbeddings
import json
from django.forms.models import model_to_dict

# Create your views here.
@api_view(['POST'])
def addQuestionAnswer(request):
    dataSent = json.loads(request.body)
    question = dataSent.get('question')
    answer = dataSent.get('answer')
    newQuestionAnswer = Question(
        question=question,
        answer=answer,
    )
    newQuestionAnswer.save()
    initializeEmbeddings()
    return JsonResponse({'message': 'New question answer pair created successfully!'}, status=201)  

@api_view(['GET'])
def getLog(request):
    query_logs = Log.objects.all()
    query_logs_dict = []
    for query_log in query_logs:
        query_log = model_to_dict(query_log)
        query_log['responses'] = query_log['answer']
        del query_log['answer']
        query_logs_dict.append(query_log)
    return Response({ 'logs': query_logs_dict })
