from django.db import models

# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(auto_created=True, primary_key=True)
    question = models.TextField(unique=True)
    answer = models.TextField()
    
# Create log table
class Log(models.Model):
    log_id = models.AutoField(auto_created=True, primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    time_to_generate_answer = models.DurationField()
    question_timestamp = models.DateTimeField()