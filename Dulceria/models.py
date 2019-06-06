from django.db import models

# Create your models here.

class Golosina(models.Model):
    # TODO

    class Meta:
        abstract = True
    
    def __str__(self):
        return self # TODO