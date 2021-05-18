# -*-coding:utf-8-*-
import xml.etree.ElementTree as ET
class OIxml:
    def readxml(self,xmlfile):
        # 读xml文件，存入list,list里是字典
        tree = ET.parse(xmlfile)
        disasters = tree.getroot()

        disastersList = []
        for disaster in disasters:
            disasterDic = dict()  # dic会变，字典不能作为临时变量吗,不是我自己好蠢
            for node in disaster:
                disasterDic[node.tag] = node.text
            # print(disasterDic)
            disastersList.append(disasterDic)
        return disastersList

   #def creatxml(self,list):
   #输出xml文件，待完成

