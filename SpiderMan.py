# coding:utf-8
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownLoader
from HtmlParser import HtmlParser
from URLManager import UrlManager


class SpiderMan(object):

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownLoader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url，同时判断取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<10):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print(self.manager.old_url_size())
                print(data)
            except Exception as e:
                print('crawl failed')

        self.output.output_question()
        self.output.output_answer()


spider_man = SpiderMan()
spider_man.crawl("https://baike.baidu.com/item/%E4%B8%AD%E5%A4%AE%E5%A4%84%E7%90%86%E5%99%A8/284033?fr=aladdin")
