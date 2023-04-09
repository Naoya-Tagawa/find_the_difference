from django.db import models
class Document(models.Model):
    description = models.CharField(max_length=255,blank=True)
    document = models.ImageField(upload_to='')
    upload_at = models.DateTimeField(auto_now_add=True)
    output = models.ImageField(upload_to = 'output/')
# Create your models here.
