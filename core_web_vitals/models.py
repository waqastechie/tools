from django.db import models

# Create your models here.


class CoreWebVitals(models.Model):

    url = models.URLField(max_length=200)
    # lcp = models.FloatField(null=True)
    # fcp = models.FloatField(null=True)
    # si = models.FloatField(null=True)
    # tti = models.FloatField(null=True)
    # tbt = models.FloatField(null=True)
    # cls = models.FloatField(null=True)
    # score = models.FloatField(null=True)
    device = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    data = models.TextField()

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_web_vitals"
