from django.db import models

# Create your models here.


class EmailValidator(models.Model):

    email = models.EmailField(unique=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "email_validator"
