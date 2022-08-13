#coding:utf-8
import os
import unittest
from ddt import ddt,data,unpack
import xlrd

# def base_dir():
#     return os.path.dirname(os.path.dirname(__file__))
#
# def readExcel():
#     lists=[]
#     sheet=xlrd.open_workbook(os.path.join(base_dir(),'data','sina.xls'))
#     book=sheet.sheet_by_index(0) #excel文件中的第一个表 索引为0
#     for item in range(1,book.nrows): #从第一行开始读取它的所有行
#         lists.append(book.row_values(item)) #读取行内的所有值 将这些值添加到列表里
#     return lists

# if __name__ == '__main__':
#     list=readExcel()
#     print(list)
#     print(len(list))


class ReadExcel:

    @staticmethod
    def get_data(excle_file_path,sheet_index):
        # 创建一个空的List
        row_list = []
        # 打开工作簿
        book = xlrd.open_workbook(excle_file_path)
        # 获取第一个sheet
        '''
        1、sheet.nrows: 工作表中有值总行数
        2、sheet.ncols：工作表中有值总列数
        3、sheet.row_values(rowx, start_colx=0, end_colx=None)：
           返回给定行中单元格值的一部分(开始行，开始列默认是0，结束列)
        '''
        sheet = book.sheet_by_index(sheet_index)
        for i in range(1, sheet.nrows):
            #row_value = sheet.row_values(i,0, sheet.ncols-1)
            row_value = sheet.row_values(i,0)
            row_list.append(row_value)
        return row_list


# if __name__ == '__main__':
#     list=ReadExcel().get_data()
#     print(list)
#     print("list列表中有效的数据为：",len(list))