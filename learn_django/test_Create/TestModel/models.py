from django.db import models

# Create your models here.

class DisasterInfo(models.Model):
    ID=models.CharField(primary_key=True,verbose_name=u"ID",unique=True,max_length=100)
    location=models.CharField(max_length=30,verbose_name=u"地理位置")
    date=models.CharField(max_length=30,verbose_name=u"日期")
    longitude=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u"经度")
    latitude=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u"纬度")
    depth=models.IntegerField(verbose_name=u"震源深度")
    magnitude=models.DecimalField(max_digits=3,decimal_places=1,verbose_name=u"震级")
    reportingUnit=models.CharField(max_length=30,verbose_name=u"上报单位")

class DeathStatistics(models.Model):
    earthquakeId=models.ForeignKey('DisasterInfo',on_delete=models.CASCADE)
    date=models.CharField(max_length=30,verbose_name=u"日期",unique=True)
    location = models.CharField(max_length=30,verbose_name=u"死亡地点")
    number=models.IntegerField(verbose_name=u"死亡人数")
    reportingUnit=models.CharField(max_length=30,verbose_name=u"上报单位")

class InjuredStatistics(models.Model):
    earthquakeId = models.ForeignKey('DisasterInfo', on_delete=models.CASCADE)
    date = models.CharField(max_length=30,verbose_name=u"日期",unique=True)
    location = models.CharField(max_length=30, verbose_name=u"受伤地点")
    number = models.IntegerField(verbose_name=u"受伤人数")
    reportingUnit = models.CharField(max_length=30, verbose_name=u"上报单位")

class MissingStatistics(models.Model):
    earthquakeId = models.ForeignKey('DisasterInfo', on_delete=models.CASCADE)
    date = models.CharField(max_length=30,verbose_name=u"日期",unique=True)
    location = models.CharField(max_length=30, verbose_name=u"失踪地点")
    number = models.IntegerField(verbose_name=u"失踪人数")
    reportingUnit = models.CharField(max_length=30, verbose_name=u"上报单位")

