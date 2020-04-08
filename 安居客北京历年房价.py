import requests
from lxml import etree
import csv

'''
https://www.anjuke.com/fangjia/beijing2011/
https://m.anjuke.com/fangjia/beijing2011/
'''

fp = open('beijing_fangjia.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('房价'))

headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'aQQ_ajkguid=B62559DA-04F4-B88E-59C5-F8928F28AB8F; ctid=20; 58tj_uuid=f7777725-0409-4eb5-acbd-7615533baebd; als=0; _ga=GA1.2.840804187.1586236028; __xsptplus8=8.3.1586267679.1586267679.1%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%232D7WsWZxLnepoqVvdkh1HWmIY-Ho5ibY%23; lps="/fangjia/beijing/|"; sessid=A34031C2-25B7-5996-97C4-418DFEDDBE56; new_session=1; init_refer=; new_uv=4; wmda_uuid=b2a11c5736be5d8dbb80fcbc6ffd6631; wmda_new_uuid=1; wmda_session_id_6145577459763=1586329708929-8463cfa1-fb64-aa82; wmda_visited_projects=%3B6145577459763; xzfzqtoken=cBXQlWcEmwjIzK3FMp5psetoxDbavCivSo8ugOGRhI4ovo%2BYCM6wObeeXP5lc0zCin35brBb%2F%2FeSODvMgkQULA%3D%3D',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


start = 2011
for i in range(0, 10):
    url = 'https://www.anjuke.com/fangjia/beijing'
    urls = url + str(start) + '/'
    start += 1
    print(urls)
    response = requests.get(urls,headers=headers)
    print(response)
    html = etree.HTML(response.content.decode('utf-8'))
    months = html.xpath("//div[@class='fjlist-wrap clearfix']/div[@class='fjlist-box boxstyle2']/ul/li/a[@class='nostyle']/b/text()")
    moneys = html.xpath("//div[@class='fjlist-wrap clearfix']/div[@class='fjlist-box boxstyle2']/ul/li/a[@class='nostyle']/span/text()")
    for month, money in zip(months,moneys):
        print(month, money)
        writer.writerow((month, money))