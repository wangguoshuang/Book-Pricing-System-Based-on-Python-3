#-*- coding: UTF-8 -*-   
from spider_dangdang import spider as dangdang
from spider_jd import spider as jd
from spider_yhd import spider as yhd
from spider_taobao import  spider as taobao
import openpyxl

def main(sn):
    """ 图书比价工具整合 """
    book_list = []
    # 当当网的数据
    print('当当网数据爬取完成')
    dangdang(sn, book_list)

    # 京东网数据
    print('京东网数据爬取完成')
    jd(sn, book_list)

    # 1号店数据
    print('1号店数据爬取完成')
    yhd(sn, book_list)

    # 淘宝数据
    print('淘宝网数据爬取完成')
    taobao(sn, book_list)

    print('----------------开始排序-----------')

    # 排序书的数据
    book_list = sorted(book_list, key=lambda item: float(item["price"]), reverse=False)

    # 创建excel
    xls = openpyxl.Workbook()
    # 激活sheet
    sheet = xls.active
    # 要保存的列头
    title = ['书名', '链接', '价格', '书店']
    # 添加列头
    sheet.append(title)

    for item in book_list:
        sheet.append([item['title'], item['link'], item['price'], item['store']])

    # 保存
    xls.save(sn+'.xlsx')

    print("----------------保存成功-----------")


if __name__ == '__main__':
    sn = input('请输入ISBN:')
    main(sn)