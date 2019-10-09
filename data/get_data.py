from util.operation_excel import OperationExcel
from data.data_config import *
from util.operation_json import OperationJson

class GetData(object):
    def __init__(self):
        self.data_config =global_val()
        self.opera_excel=OperationExcel()
    #去获取Excel的行数，就是case数量
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    #是否执行
    def get_is_run(self,row):
        flag=None
        col =int(self.data_config.get_run())
        run_model=self.opera_excel.get_cell_value(row,col)
        if run_model=='yes':
            flag=True
        else:
            flag=False
        return flag
    #是否携带header
    def is_heard(self,row):
        col = int(self.data_config.get_header())
        header = self.opera_excel.get_cell_value(row,col)
        if header =='yes':
            return self.data_config.get_header_value()
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col =int(self.data_config.get_request_way())
        request_method=self.opera_excel.get_cell_value(row,col)
        return request_method
    #获取url
    def get_request_url(self,row):
        col=int(self.data_config.get_url())
        url=self.opera_excel.get_cell_value(row,col)
        return url
    #获取请求数据
    def get_request_data(self,row):
        col=int(self.data_config.get_data())
        data=self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        else:
            return data
    #通过关键字获取数据
    def get_data_for_json(self,row):
        operjson =OperationJson()
        operjson.get_data(self.get_request_data(row))
    #获取预期结果
    def get_expect_result(self,row):
        col=int(self.data_config.get_except())
        expect=self.opera_excel.get_cell_value(row,col)
        #expect=200
        if expect=='':
            return None
        return int(expect)
if __name__=="__main__":
    getdata =GetData()
    print(getdata.get_expect_result(1))
    print(type(getdata.get_expect_result(1)))






