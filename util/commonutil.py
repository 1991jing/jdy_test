#coding:utf-8
import string
class  CommonUtil(object):
    #one是查找的字符串，two是被查找的字符串
    def is_contain(self,str_one,str_two):
        # if isinstance(str_one,):
        #     str_one=str_one
        str_one =str(str_one)
        str_two =str(str_two)
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
