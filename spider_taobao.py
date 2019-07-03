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

    cookies = 'miid=8714148791278719518; cna=Cyu/E7Ov7VwCAd9oGfKm8Prj; hng=CN%7Czh-CN%7CCNY%7C156; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=kURVXibmZ9EPbYvDvg7UYeoDr8dubOxaVPFYqFLHfkJ2N5TVOqR4WVb641JyDLxbhzkGM%2BK8EIJlJ44oAHjHJw%3D%3D; t=37b1297954623ff4df508d4a3a2b86b2; _uab_collina=155723164805294996163853; UM_distinctid=16aea516c7e299-0f26df75014257-3e385b04-144000-16aea516c7f79e; tracknick=%5Cu8D75%5Cu6743525; lgc=%5Cu8D75%5Cu6743525; cookie2=1183875450159e20e0d0badedafbfccd; v=0; _tb_token_=f47dae3e53b58; dnk=%5Cu8D75%5Cu6743525; skt=5f4d1a7ac3869eb7; csg=ea2a1cd5; uc3=vt3=F8dBy34ZEYkEhI592jA%3D&id2=Uoe8izNc10cUZQ%3D%3D&nk2=tsVkEAalNw%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTU2MTQ0OTA1Mg%3D%3D; _cc_=VT5L2FSpdA%3D%3D; birthday_displayed=1; thw=cn; swfstore=86831; mt=ci=-1_0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=9d3fa56b636810f254e702ddc77d0982_1562127282590; _m_h5_tk_enc=799efde4bdb276ab7b2121befe2519bc; JSESSIONID=4CF0A49DD07CC3691F3711F64E7E3586; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UIHiLt3xSifiVqTH8o%2F0Qw%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTaGqykpoO1KA%3D%3D&tag=8&lng=zh_CN; isg=BLOzZMuW6kZCmKdAO66Zp2OFQrcdQELO6RDZ72VSClKAZNIG7Lv9-gO2HtQvCZ-i; l=bBa3_lqIvxP_pFNyBOfaCuI88ob9oQAb8NFzw4GGqICP_7fHgEl1WZHdxNTMC3GVZ6OwJ3WW5uN4B8TMyyCV.'
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