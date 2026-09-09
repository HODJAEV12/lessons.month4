from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")

# get - Backend -> Fontend
# post - Fontend -> Backend