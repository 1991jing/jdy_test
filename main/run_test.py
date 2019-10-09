from base.runmethod import RunMethod
from data.get_data import GetData
from util.commonutil import CommonUtil
import sys
#sys.path.append()

class RunTest(object):
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.commountil=CommonUtil()
    #程序主入口
    def go_on_run(self):
        res = None
        rows_count=self.data.get_case_lines()
        for i in range(1,rows_count):
            print(1)
            url=self.data.get_request_url(i)
            method=self.data.get_request_method(i)
            is_run =self.data.get_is_run(i)
            data=self.data.get_data_for_json(i)
            header= self.data.is_heard(i)
            expcet=self.data.get_expect_result(i)
            if is_run:
                res=self.run_method.run_main(method,url,data,header)
                if self.commountil.is_contain(expcet,res):
                    print("test is ok")
                else:
                    print("fail")

if __name__=="__main__":
    run=RunTest()
    print(run.go_on_run())
