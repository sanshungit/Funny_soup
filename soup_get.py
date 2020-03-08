from time import time
import requests

            
class Downloadhandler(object):

    def __init__(self,url):
        self.url=url

    def refresh_load(self):
        resp=requests.get(self.url)
        data_model=resp.json()
        return data_model['newslist'][0]['content']
    
def main():
    url='http://api.tianapi.com/txapi/dujitang/index?key=<申请的key>'
    f=open('./毒鸡汤.txt','a+')

    print('开始抓取....')
    for _ in range(1000):
       soup_str= Downloadhandler(url).refresh_load()
       f.write(soup_str+'\n')
    f.close()
    print('抓取完成！！！')

if __name__=='__main__':
    main()
