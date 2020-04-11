#coding:utf-8
import xlrd

class OperationExcel(object):
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/xlsx_test.xlsx'
            self.sheet_id = 0
        self.book = self.get_data(self.file_name, self.sheet_id)

    def get_data(self,file_name=None,sheet_id=None):
        book = xlrd.open_workbook(self.file_name)
        sheets = book.sheets()[self.sheet_id]
        return sheets

    #获取单元格的行数
    def get_lines(self):
        sheets = self.book
        return sheets.nrows

    #获取单元格的内容
    def get_cell_value(self,row,col):
        return self.book.cell_value(row,col)

if __name__ == '__main__':
    opers = OperationExcel()
    r1 = opers.get_data('../dataconfig/xlsx_test.xlsx',1)
    r2 = opers.get_data()
    print(r2.nrows)
    print(opers.get_cell_value(1,1))
    print(r1.cell_value(1,2))
    print(r2.cell_value(1,2))