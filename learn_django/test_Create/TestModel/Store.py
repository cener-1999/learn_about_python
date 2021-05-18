import os
import django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'test_Create.settings')
django.setup()

from TestModel.models import DisasterInfo,DeathStatistics,InjuredStatistics,MissingStatistics

#下一步存数据库就行了-_-

class Storage:
    def disasters_storage(self,disastersList):
        for disasterDic in disastersList:
            disaster=DisasterInfo(ID=str(disasterDic['ID']),location=disasterDic['location'],
            date=disasterDic['date'],longitude=float(disasterDic['longitude']),
            latitude=float(disasterDic['latitude']),depth=int(disasterDic['depth']),
            magnitude=float(disasterDic['magnitude']),reportingUnit=disasterDic['reportingUnit'])
            disaster.save()
            disaster.clean()

    def death_storage(self, deathDic):
        try:
            death = DeathStatistics(
                                    earthquakeId=DisasterInfo.objects.get(ID=str(deathDic['earthquakeId'])),
                                    location=deathDic['location'],
                                    date=deathDic['date'],
                                    number=deathDic['number'],
                                    reportingUnit=deathDic['reportingUnit'])
            death.save()
            death.clean()
        except django.db.utils.IntegrityError:
            print('信息重复，插入失败')

    def injured_storage(self, injuredDic):
        try:
            injured = InjuredStatistics(
                                        earthquakeId=DisasterInfo.objects.get(ID=str(injuredDic['earthquakeId'])),
                                        location=injuredDic['location'],
                                        date=injuredDic['date'],
                                        number=injuredDic['number'],
                                        reportingUnit=injuredDic['reportingUnit'])
            injured.save()
            injured.clean()
        except django.db.utils.IntegrityError:
            print('信息重复，插入失败')

    def missing_storage(self, missingDic):
        try:
            missing = MissingStatistics(
                                        earthquakeId=DisasterInfo.objects.get(ID=str(missingDic['earthquakeId'])),
                                        location=missingDic['location'],
                                        date=missingDic['date'],
                                        number=missingDic['number'],
                                        reportingUnit=missingDic['reportingUnit'])
            missing.save()
            missing.clean()
        except django.db.utils.IntegrityError:
            print('信息重复，插入失败')




