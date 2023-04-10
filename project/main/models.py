from django.db import models

# Create your models here.
# creating a model
class AlgoModel(models.Model) : 
    algo_name = models.CharField(max_length=100)
    document_text = models.CharField(max_length=1000000)
    