from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class TestingTypes(models.Model):
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    resource_count = models.IntegerField(
        validators=[MaxValueValidator(2000),MinValueValidator(10)]
    )
    notes = models.CharField(max_length=300,null=True)
    # auto id already added by django

    def __str__(self):
        return f"type:{self.type} description:{self.description} resouce_count:{self.resource_count}"




