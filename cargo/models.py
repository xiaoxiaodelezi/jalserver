from django.db import models

# Create your models here.
#机场和国家二字代码的对应
class Airport(models.Model):
    station=models.CharField(max_length=3)
    country=models.CharField(max_length=2)
    def __str__(self):
        return self.station

#国家全称和2字代码的转换
class Country(models.Model):
    full_name=models.CharField(max_length=100)
    short_name=models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

#表示需要特别留意的uld类型
class Special_uld(models.Model):
    uld=models.CharField(max_length=10)
    def __str__(self):
        return self.uld
