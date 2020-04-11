# coding:utf-8
import json
class OperationJson:

    def __init__(self,jsonurl=None):
        self.jsonurl ='../dataconfig/json_test.json'
        self.data = self.read_data

    #读取json文件中数据
    def read_data(self,jsonurl=None):
        if jsonurl is None:
            jsonurl = self.jsonurl
        with open(jsonurl) as fp:
            data = json.load(fp)
            return data

    #获取json文件中数据
    def get_data(self,key,jsonurl=None):
        # if jsonurl is None:
        #     jsonurl = self.jsonurl
        return self.data(jsonurl)[key]
if __name__ =="__main__":
    testjs =OperationJson()
    # print(testjs.read_data('../dataconfig/json_test.json'))
    # print(testjs.read_data())

    # 这样的顺序调用jsonurl的默认值被更改了？？？
    print(testjs.get_data('event01','../dataconfig/json_test.json'))
    print(testjs.get_data('event02'))

