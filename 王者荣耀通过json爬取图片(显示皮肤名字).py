import os
import requests
import re

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件
# print(herolist.text)
herolist_json = herolist.json()  # 转化为json格式
# print(herolist_json)
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
# print(hero_name)
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号
# # 尝试过从json文件中提取数据，如下，虽然提取到了，但是如果要将它和皮肤名字一一对应，恐怕有点难
# # skin_names = re.compile('"skin_name": "(.*?)"', re.S)
# # sss = skin_names.findall(herolist.text)
# # print(sss)
# # ['正义爆轰|地狱岩魂', '恋之微风|万圣前夜|天鹅之梦|纯白花嫁|缤纷独角兽', '苍天翔龙|忍●炎影|未来纪元|皇家上将|嘻哈天王|白执事|引擎之心', '和平守望|金属风暴|龙骑士|进击墨子号', '魅
#
# yx_urls = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'
os.mkdir(r'E:\Python社区版\王者荣耀皮肤图片1')
# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        yx_url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(str(j))
        r = requests.get(yx_url)
        # 创建文件夹
        try:
            os.mkdir(r'E:\Python社区版\王者荣耀皮肤图片1\\' + hero_name[i])
        except:
            pass
        # 进入创建好的文件夹
        os.chdir(r'E:\Python社区版\王者荣耀皮肤图片1\\' + hero_name[i])
        i += 1
        # #经过一系列转化，将皮肤转成列表格式方便遍历
        pifu = re.compile('<ul class="pic-pf-list pic-pf-list3" data-imgname="(.*?)">', re.S)
        ssss = pifu.findall(r.content.decode("gbk"))[0]
        # print("ssss:", ssss)
        aaaa = ssss.replace("|", "")
        # print("aaaa:", aaaa)
        bbbb = re.sub(r'&\d*', '", "', aaaa)
        cccc = '["{}"]'.format(bbbb)
        # 将字符串转化为列表
        dddd = eval(cccc)
        # 删除列表最后的""
        del dddd[-1]
        # print("dddd:", dddd)

        for k, l in enumerate(dddd):
            # print(k+1, l)
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(j) + '-bigskin-' + str(k+1) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                f = open(str(l) + '.jpg', 'wb')
                print('{}正在下载{}皮肤😁😁'.format(i, l))
                f.write(im.content)  # 写入文件
                f.close()
# #
#         # w = len(hero_name)-j+1
#         # print("{}的皮肤下载成功！！".format(hero_name[w]))
#
downloadPic()
