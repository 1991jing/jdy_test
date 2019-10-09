#coding:utf-8
class global_val(object):
    Id='0'
    name='1'
    ulr='2'
    run='3'
    request_way='4'
    header='5'
    case_depend='6'
    data_depend='7'
    field_depend='8'
    data='9'
    expect='10'
    result ='11'
    #获取id
    def get_id(self):
        return global_val.Id
    def get_url(self):
        return global_val.ulr
    def get_run(self):
        return global_val.run
    def get_request_way(self):
        return global_val.request_way
    def get_header(self):
        return global_val.header
    def get_case_depend(self):
        return global_val.case_depend
    def get_data_depend(self):
        return global_val.data_depend
    def get_field_depend(self):
        return global_val.field_depend
    def get_data(self):
        return global_val.data
    def get_except(self):
        return global_val.expect
    def get_result(self):
        return global_val.result
    def get_header_value(self):
        header ={"Accept-Language": "en,zh","Accept": "text/plain, text/html"}

if __name__=="__main__":
    q=global_val()
    print(q.get_run())
