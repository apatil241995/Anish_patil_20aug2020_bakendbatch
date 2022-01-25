from django.contrib.auth.models import User
from django.db import models


class UrlsTable(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ShortUrl = models.CharField(max_length=60)
    main_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=200)
    uuid = models.CharField(max_length= 10, null=True)