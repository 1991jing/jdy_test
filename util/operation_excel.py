import xlrd

# data =xlrd.open_workbook("../data_config/接口测试.xlsx")
# sheets =data.sheet_by_index(0)
# print(sheets)
#
# print(sheets.nrows)
# print(sheets.cell_value(1,1))

class OperationExcel(object):
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name="../data_config/接口测试.xlsx"
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        sheets = data.sheet_by_index(self.sheet_id)
        return sheets
    #获取单元格行数
    def get_lines(self):
        tables=self.data
        return tables.nrows
    #获取单元格的内容
    def get_cell_value(self,row,col):
        return  self.data.cell_value(row,col)

if __name__ == "__main__":
    opers = OperationExcel()
    print(opers.get_lines())
    print(opers.get_cell_value(1,1))


