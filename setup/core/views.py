from rest_framework.response import Response
from rest_framework import viewsets
from .models import Question, Alternative
from .serializer import QuestionSerializers, AlternativeSerializers


class QuestionViewSet(viewsets.ModelViewSet):
   
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializers(queryset, many=True)
        return Response(serializer.data)


class AlternativeViewSet(viewsets.ModelViewSet):
   
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializers
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = AlternativeSerializers(queryset, many=True)
        return Response(serializer.data)
