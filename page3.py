#-*- coding:utf-8 –*-
import urllib
import urllib2
import re
import thread
import time

class caihaopage3:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        self.pageStories = []
        self.url = 'http://hy.xuzhoujob.com/office-3.html'
        self.headers = {'User-Agent': self.user_agent}

    def getpage(self, index):
        user_agant = self.user_agent
        url = self.url
        headers = {'User-Agent': user_agant}
        result = urllib2.Request( url, headers=headers )
        response = urllib2.urlopen( result )
        pageCode = response.read()
        return pageCode

    def pageindex(self, index):
        pageCode = self.getpage( index )
        pattern = re.compile('<td class="list_o">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>',re.S)
        items = re.findall( pattern, pageCode )
        for i in items:
            input = raw_input()
            for g in i:
                
                print g

    def start(self):
        print "--------------------------------------page3------------------------------------"
        print "-------------             i'm    Separation   line         --------------------"
        self.getpage(index=caihaopage3)
        self.pageindex(index=caihaopage3)

