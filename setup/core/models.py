
from urllib import response
from django.db import models
from uuid import uuid4


# Create your models here.
class Alternative(models.Model):
    ANSWER =(
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('Sem resposta', 'Sem resposta')

    )

    alternative_a = models.TextField(blank=False, null=False) 
    alternative_b = models.TextField(blank=False, null=False)
    alternative_c = models.TextField(blank=False, null=False)
    alternative_d = models.TextField(blank=False, null=False)
    answer_status = models.BooleanField(default=False)
    question_answer = models.CharField(max_length=255, choices=ANSWER, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.id}"
    ...


class Question(models.Model):
   
    tittle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    alternative_id = models.ForeignKey(Alternative, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.tittle}"
    ...

    
