from django.db import models

# Create your models here.

from django.db import models


class Keyword(models.Model):

    keyword = models.CharField(unique=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "question_explorer_keywords"


class Suggestion(models.Model):

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "question_explorer_suggestions"
