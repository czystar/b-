import requests
from lxml import etree
url = 'https://www.bilibili.com/v/popular/rank/all'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
    'cookie':"buvid3=1EB8D59F-3A08-4D98-8A8B-A0CD23512368190950infoc; rpdid=|(JY)k)klY~Y0J'ul~uuu~)ml; LIVE_BUVID=AUTO5415711177935363;fingerprint3=a79aa6162605e6a2e0d03b21636b516e; fingerprint_s=18da7071ee7757206838a26efa570a6f; _uuid=CA5CBF59-A525-98C1-E11F-4B84AB22A74D65467infoc; LNG=zh-CN; DedeUserID=35141053; DedeUserID__ckMd5=98ef095b6cadbe19; video_page_version=v_old_home; b_ut=5; i-wanna-go-back=2; nostalgia_conf=2; hit-dyn-v2=1; sid=au8giw47; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; SESSDATA=0094c563%2C1668595598%2Cd4707*51; bili_jct=f1391df8add5ff2c8feb973dbe17c075; go_old_video=1; bp_article_offset_35141053=682240037434163208; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; fingerprint=3e331eb13bf244d9539b268283bf29d6; buvid_fp=3e331eb13bf244d9539b268283bf29d6; buvid4=2148738C-3C00-5BD7-E003-E40F8FC5DD1286820-022012418-c8mC4VtaIp9sn3xNj0%2FQSA%3D%3D; bp_video_offset_35141053=691892830472241168; innersign=1; arrange=matrix; b_lsid=8B3A4B18_1827CAA51CD; b_timer=%7B%22ffp%22%3A%7B%22333.851.fp.risk_1EB8D59F%22%3A%221827C03FE82%22%2C%22333.1193.fp.risk_1EB8D59F%22%3A%221827CB7507E%22%2C%22444.8.fp.risk_1EB8D59F%22%3A%221827C04322B%22%2C%22333.788.fp.risk_1EB8D59F%22%3A%221827C455BBA%22%2C%22333.337.fp.risk_1EB8D59F%22%3A%221827CB74E9E%22%2C%22333.999.fp.risk_1EB8D59F%22%3A%221827C446AE7%22%2C%22888.2421.fp.risk_1EB8D59F%22%3A%221827CB50198%22%2C%22777.5.0.0.fp.risk_1EB8D59F%22%3A%221827CBB13ED%22%7D%7D; PVID=4"
}
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
tree = etree.HTML(res.text)
dict = {}
i = 1
#循环获取数据
for li in range(1,101):
    value = tree.xpath(f'//*[@id="app"]/div/div[2]/div[2]/ul/li[{li}]/div/div[2]/a/@href')
    key = tree.xpath(f'//*[@id="app"]/div/div[2]/div[2]/ul/li[{li}]/div/div[2]/a//text()')
    for k,v in zip(key,value):
        dict[str(i)+k]=v
    i+=1

print(dict)