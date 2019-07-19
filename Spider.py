# -*- coding: utf-8 -*-
import requests
from lxml import etree
import time
import csv

global x
global y
global z
global p
global s
#定义爬虫子函数
def crow_first(n):
  #定义爬取的url
	url = 'https://search.jd.com/Search?keyword=%E9%A5%AE%E6%96%99&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%A5%AE%E6%96%99&stock=1&page=' + str(2 * n - 1)
  head = {
			'authority': 'search.jd.com',
			'method': 'GET',
			'scheme': 'https',
			'referer': 'https://search.jd.com/Search?keyword=%E9%A5%AE%E6%96%99&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E9%A5%AE%E6%96%99&stock=1&page=5&s=100&click=0',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
			'Cookie': '__jdu=1525181626; shshshfpa=37188308-1727-af2d-6b3d-055a4098b166-1560399188; shshshfpb=jE%2FGWIAZnenBkxDYRrpS2Iw%3D%3D; pinId=sMa9OrOjJnE-EGfWMwHvu7V9-x-f3wj7; pin=jd_70f995117561e; unick=%E4%BA%8C%E8%83%A1%E5%A6%82%E4%BD%95%E6%8B%89%E7%9A%84%E4%B8%8D%E6%82%B2%E4%BC%A4; _tp=LPqWblrBK2EbSF19z4zTwOj5UuiTfBRCpRMLcHaPP9o%3D; _pst=jd_70f995117561e; xtest=6327.cf6b6759; qrsc=3; ipLocation=%u5c71%u4e1c; TrackID=1d2ThTktK40Z6ipchTWCdNiamZw9kqHDHuSO04a1NBTY0y7Fctr2GSHjYORib2B7zH52FsxaRB1_1KFqB2cAXGLvs3aetOqJnAijVVWj98vI; unpl=V2_ZzNtbURWSx11W0Bdfh5bAGJTR14RAEpAJQpGVn5OCwU1UBVcclRCFX0UR1JnGVsUZwcZXEtcRhxFCEdkeB5fA2AFEFlBZxBFLV0CCyFbMgNnChFaSlNEHHIIdmR4GWwFZjMSWUFTQxx1D0VTSylbNVczEFRAX0ATRQl2VUsZEQVjABZdS1dEFnI4R2R4; __jdv=122270672|baidu-nks|t_262767352_baidunks|cpc|71826956861_0_70991b7846644ad2bf8da3134ff1cb60|1563260947329; shshshfp=ec688e4f85742e0e56ba1f09732dba15; __jdc=122270672; rkv=V0100; PCSYCityID=1007; __jda=122270672.1525181626.1555574524.1563428387.1563431185.23; areaId=13; ipLoc-djd=13-1007-4909-0; 3AB9D23F7A4B3C9B=N2S2FDUWZY3N6NGZHKIRB5HZMIDTOD2GTD3FFM3M6WCVLSJCONC6SXR7IXZVZKHTLX5RSKIUS3QBMECG6275HB345U; __jdb=122270672.2.1525181626|23.1563431185; shshshsID=c397fac5388d524b70971ac75327b1b3_2_1563431321647'
			}
	r = requests.get(url, headers=head)
	r.encoding = 'utf-8'
	html1 = etree.HTML(r.text)
	for k in range(1, 30):
		m = '//*[@id="J_goodsList"]/ul/li[%d]'%k
		datas = html1.xpath(m)
		with open('JD_shopping.csv', 'a', newline='', encoding='utf-8')as f:
			write = csv.writer(f)
			for data in datas:
				price_xpath = m+'/div/div[@class="p-price"]/strong/i'
				shop_xpath = m+'/div/div[@class="p-shop"]/span/a'
				name_xpath = m+'/div/div[@class="p-name p-name-type-2"]/a/em'
				name1_xpath = m+'/div/div[@class="p-name p-name-type-2"]/a/em/font'
				p_price = html1.xpath(price_xpath)
				p_shop = html1.xpath(shop_xpath)
				p_name = html1.xpath(name_xpath)
				p_name1 = html1.xpath(name1_xpath)
				list = []
				for y, z, p, s in zip(p_name, p_name1, p_price, p_shop):
					name = y.text
					name1 = z.text
					shop = s.text
					price = p.text
					list = [name, name1, shop, price]
					print(list)
				write.writerow(list)
		f.close()
		
if __name__ == '__main__':
	for i in range(1, 30):
		print("************************开始**********************")
		try:
			print('   First_Page:   ' + str(i))
			crow_first(i)
			print('   Finish')
		except Exception as e:
			print(e)
		print('-----------------------')
