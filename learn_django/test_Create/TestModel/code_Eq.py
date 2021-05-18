# -*-coding:utf-8-*-

#给震情数据编码，使用时只需要调用code(),接受一个LIST，返回一个LIST
class Code_Eq():
    # 只有所有示例数据对应的城市，完整编码得下个数据库了，70w条数据
    def code_geo(self, dic):
        # 5级目录

        village_donghuamengjiedao = {'多福巷社区居委会': 110101001001,
                                     '银闸社区居委会': 110101001002,
                                     '东厂社区居委会': 110101001005}
        village_sijiedao = {'参府社区居委会': 140402002002}
        town_dongchengqu = {'东华门街道': village_donghuamengjiedao,
                            '东华门街道办事处': village_donghuamengjiedao}
        town_chengqu = {'西街街道办事处': village_sijiedao}
        country_shixiaqu = {'东城区': town_dongchengqu}
        country_changzhicity = {'城区': town_chengqu}
        city_shanxi = {'长治市': country_changzhicity}
        city_beijing = {'市辖区': country_shixiaqu}
        province_dic = {'北京市': city_beijing, '山西省': city_shanxi}

        province = dic['province']
        city = dic['city']
        country = dic['country']
        town = dic['town']
        village = dic['village']

        geo_code = province_dic.get(province).get(city).get(country).get(town).get(village)

        return str(geo_code)

    #给时间编码，转换为9位str
    def code_time(self, date):
        time = date
        time = time.replace(' ', '')
        time = time.replace(':', '')
        time = time.replace('-', '')
        time_code = time
        return time_code

    #生成ID
    # 救命啊，hwj怎么乱给数据啊！！！！无中生有
    def generate_ID(self, dic):
        geo_code = self.code_geo(dic);
        date_code = self.code_time(dic['date'])
        ID = int(geo_code + date_code)
        return ID

    #给所有需要编码的数据编码
    def code(self, disastersList):
        # 在字典内重新编码
        for disasterDic in disastersList:
            disasterDic["reportingUnit"] = str(501) + disasterDic["reportingUnit"]
            disasterDic['ID'] = self.generate_ID(disasterDic)

        return disastersList
