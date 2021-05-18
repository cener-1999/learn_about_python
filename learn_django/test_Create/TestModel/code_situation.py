# -*-coding:utf-8-*-
#给灾情数据编码，目前只有到人员伤亡部分
class Code_situation:
    def sort(self, Dic):
        if Dic['category'] == '人员死亡':
            return '11'
        elif Dic['category'] == '人员受伤':
            return '12'
        elif Dic['category'] == '人员失踪':
            return '13'

    #来源地址编码，从云端的话应该有一个path参数，从path可以得到前3位，现在不考虑；
    def code(self, List):
        # 在字典内重新编码
        for Dic in List:
            Dic["reportingUnit"] = str(101) + Dic["reportingUnit"]
        return List

