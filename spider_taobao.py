#-*- coding: UTF-8 -*-   
import requests
import re
import json


def spider(sn, book_list=[]):
    """ 爬取淘宝网的图数数据 """
    url = 'https://s.taobao.com/search?q={}&imgfile=&commend=all&ssid=s5-e' \
          '&search_type=item&sourceId=tb.index' \
          '&spm=a21bo.2017.201856-taobao-item.1&ie=utf8' \
          '&initiative_id=tbindexz_20170306'.format(sn)

    cookies = 'cna=liZYFYESbFoCAXWdZlH79Vto; t=4cec82598192794763b66a4c4c70f45e; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _m_h5_tk=3012ab56a127bc1086521aba6fa135cb_1562946232566; _m_h5_tk_enc=01d281d8d1b57cb9c33b97275281f1d4; cookie2=1f34ceed6e1602f891ff90a1c8cc3b6c; v=0; _tb_token_=ebee018b33fbf; unb=2643700604; sg=%E9%97%B44c; _l_g_=Ug%3D%3D; skt=51a6db006ac33360; cookie1=B0Bbjnm7nh3t15QFJMlGFdHlQt8f6vCg%2BNF0r0%2BrIYY%3D; csg=7f618a9c; uc3=vt3=F8dBy3%2F9Edumm2KgReQ%3D&id2=UU6lTo85zYa1dg%3D%3D&nk2=sfniGR84E4c%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTU2MjkzNjkzMA%3D%3D; tracknick=%5Cu610F%5Cu73A9%5Cu7A7A%5Cu95F4; lgc=%5Cu610F%5Cu73A9%5Cu7A7A%5Cu95F4; _cc_=WqG3DMC9EA%3D%3D; dnk=%5Cu610F%5Cu73A9%5Cu7A7A%5Cu95F4; _nk_=%5Cu610F%5Cu73A9%5Cu7A7A%5Cu95F4; cookie17=UU6lTo85zYa1dg%3D%3D; tg=0; mt=ci=46_1; enc=fHnh3nbg%2B%2BDqHDI7pcWXQbeCOW5WfHa7%2B01P6PPrtQGgrlxuH0KV3zEaRgOIahkAvt4D3IwiCp9JbjJpaSqsIg%3D%3D; uc1=cookie14=UoTaGqSl9NF4sw%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=W5iHLLyFfX5Xzx7qNYvXUg%3D%3D&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; _mw_us_time_=1562937345890; isg=BN_f4BjO_r61jvtY5ZqYIi7ybjOp7Bhm1tZes3Es1A7VAP6CeRSsNhqSwtDbmAte; l=cBI3jeOcv0B5-JpLBOfZNuIRXS7OVIRb8sPzw4ZQiICPOJCH582cWZnODCYMCnGVp666R3-PX15aBtQwqsb9OBzDw8VMU'
    headers = {
        'Cookie': cookies,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    rest = requests.get(url, headers=headers)
    # rest.encoding = 'utf-8'
    json_str = re.search('g_page_config = (.*?)g_srp_loadCss', rest.text, re.S).group(1)
    json_obj = json.loads(json_str.strip().strip(';'))
    # print(json_obj)
    auctions = json_obj['mods']['itemlist']['data']['auctions']
    print("共抓取%s条" % len(auctions))

    for auction in auctions:
        pattern = re.compile(r'<[^>]+>', re.S)

        # 标题
        title = pattern.sub('', auction['title'])
        price = auction['view_price']
        link = "https:"+auction['detail_url']
        store = auction['nick']
        book_list.append({
            'title': title,
            'price': price,
            'link': link,
            'store': store
        })

if __name__ == '__main__':
    spider('9787115428028')
