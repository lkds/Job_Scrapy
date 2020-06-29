# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import Request, Response
import requests


class JobSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JobDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self):
        self.retry_count = 5

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def get_proxy(self):
        return requests.get("http://47.113.123.159:5010/get/").json()

    def delete_proxy(self,proxy):
        requests.get("http://47.113.123.159:5010/delete/?proxy={}".format(proxy))

    # your spider code

    def modifyRequest(self,request,times):
        # ....
        if (times == 0):
            return None
        proxy = self.get_proxy().get("proxy")
        retry_count=3
        while retry_count>0:
            try:
                html = requests.get(request.url, proxies={"http": "http://{}".format(proxy)},allow_redirects=False)
                if html.status_code == 200:
                    request.meta['proxy'] = "http://%s" % proxy
                    return request
                retry_count -= 1
            except Exception:
                retry_count -= 1
        # return None
        # 出错5次, 删除代理池中代理
        self.delete_proxy(proxy)
        return self.modifyRequest(request,times-1)

        
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # proxy = requests.get(
        #     "http://47.113.123.159:5010/get/").json()['proxy']
        # request.meta['proxy'] = "http://%s" % proxy
        # print(request)
        self.modifyRequest(request,5)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        if not response.status == 200:
            return self.modifyRequest(request)
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        # return self.modifyRequest(request)
        pass
        # return None

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
