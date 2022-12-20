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

#表示需要检查的品名
class Suspicious_good(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

#代理领取运单记录
class Awb_distribution(models.Model):
    agent=models.CharField(max_length=3)
    piece=models.IntegerField()
    #str(uuid.uuid4())
    distribution_uuid=models.CharField(max_length=36)
    distribution_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.agent +"  " + str(self.distribution_date)

#运单记录
class Awb_info(models.Model):
    number=models.CharField(max_length=12)
    agent=models.CharField(max_length=3)
    distribution_uuid=models.CharField(max_length=36)

    def __str__(self):
        return self.number