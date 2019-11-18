# coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new__urls = set()   # 未爬取URL集合
        self.old_urls = set()   # 已爬取URL集合

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_url = self.new__urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        将新的URL添加到未爬取的URL集合中
        :param url:单个url
        :return:
        '''
        if url is None:
            return
        if url not in self.new__urls and url not in self.old_urls:
            self.new__urls.add(url)

    def add_new_urls(self, urls):
        '''
        将新的URL添加到未爬取的URL集合中
        :param urls:url集合
        :return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        获取已经爬取url集合的大小
        :return:
        '''
        return len(self.new__urls)

    def old_url_size(self):
         '''
         获取已经爬取url集合的大小
         :return:
         '''
         return len(self.old_urls)

