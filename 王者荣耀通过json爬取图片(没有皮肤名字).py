import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号
yx_urls = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'
# 首先创建一个总的文件夹
os.mkdir(r'E:\Python社区版\王者荣耀')
# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        yx_url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(str(j))
        r = requests.get(yx_url)
        # 创建皮肤汇总的文件夹
        try:
            os.mkdir(r'E:\Python社区版\王者荣耀\\' + hero_name[i])
        except:
            pass
        # 进入创建好的文件夹
        os.chdir(r'E:\Python社区版\王者荣耀\\' + hero_name[i])
        i += 1
        for k in range(10):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            # 到后面没有皮肤时，随着k的增大，onehero_link所构成的网址为无效
            # 例如http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/195/195-bigskin-8.jpg为无效网址
            if im.status_code == 200:
                f = open(str(k) + '.jpg', 'wb')
                f.write(im.content)  # 写入文件
                f.close()
        w = len(hero_name)-j+1
        print(i)
        print(hero_name[w] + '的皮肤下载成功！！')

downloadPic()
