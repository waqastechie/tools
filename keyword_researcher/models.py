from django.db import models

# Create your models here.


class Keyword(models.Model):

    keyword = models.CharField(unique=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "keyword_researcher_keywords"


class Suggestion(models.Model):

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "keyword_researcher_suggestions"
