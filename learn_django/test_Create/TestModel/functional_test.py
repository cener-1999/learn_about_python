# -*-coding:utf-8-*-
from TestModel.oi_xml import OIxml
from TestModel.code_Eq import Code_Eq
from TestModel.code_situation import Code_situation
from TestModel.Store import Storage

class fun_test:
    def if_stroge_eq(self,file):
        read = OIxml()
        eqList = read.readxml(file)
        storage = Storage()
        code = Code_Eq()
        eqList=code.code(eqList)
        storage.disasters_storage(eqList)

    def if_stroge_sit(self,file):
        flie = 'Template.xml'
        read = OIxml()
        dsList = read.readxml(file)
        storage = Storage()
        code= Code_situation()
        code.code(dsList)
        for dic in dsList:
            flag = code.sort(dic)
            if (flag=='11'):
                storage.death_storage(dic)
            elif (flag == '12'):
                storage.injured_storage(dic)
            elif(flag=='13'):
                storage.missing_storage(dic)

file = 'EarthquakeTemplate.xml'
file1='Template.xml'
test1=fun_test()
test1.if_stroge_eq(file)
test1.if_stroge_sit(file1)

