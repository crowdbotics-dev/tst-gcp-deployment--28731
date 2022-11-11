from django.conf import settings
from django.db import models
import requests

class Hello(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
class Hi(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    
    def test_method(self):
        response = requests.get("https://hello.com")
        data = response.json() 
        return data
