from django.contrib import admin
from .models import Question, Alternative
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'id']
    search_fields = ['tittle','id']
    list_per_page = 10
    ...


@admin.register(Alternative)
class AlternativeAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['tittle','id', 'answer_status']
    list_per_page = 40
    ... 
