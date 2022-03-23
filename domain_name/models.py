from django.db import models

# Create your models here.


# class DomainName(models.Model):

#     domain_name = models.CharField(max_length=500)
#     registrar = models.CharField(max_length=500)
#     whois_server = models.CharField(max_length=500)
#     referral_url = models.CharField(max_length=500)
#     updated_date = models.DateTimeField()
#     creation_date = models.DateTimeField()
#     expiration_date = models.DateTimeField()
#     name_servers = models.CharField(max_length=500)
#     status = models.CharField(max_length=1000)
#     emails = models.EmailField()
#     dnssec = models.CharField(max_length=500)
#     name = models.CharField(max_length=1000)
#     org = models.CharField(max_length=1000)
#     address = models.TextField(max_length=2000)
#     city = models.CharField(max_length=500)
#     state = models.CharField(max_length=500)
#     zipcode = models.IntegerField(max_length=500)
#     country = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "domain_names_info"
