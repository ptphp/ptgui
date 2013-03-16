#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2012-10-21

@author: Administrator
'''
from BeautifulSoup import BeautifulSoup
import urllib,urllib2
from urlparse import urlparse
import os,re,time
from hashlib import md5

pro_dir = r"D:\PtProject\workspace\projects\offline\Public"
root_url = 'http://localhost:8004'

def getCharset(res):
    charset = ''
    if re.search('charset=(.*?)>',res):
       charset = re.search('charset=(.*?)>',res).group(1)
       charset =  charset.replace('/','').strip().strip('"')
    return charset

def makeDir(path):
    try:
        if os.path.isdir(path) == False:
            makeDir(os.path.dirname(path))        
            return os.mkdir(path)
    except Exception as what:
        print what
        pass
        
    return True

def putContent(path,content,f = False,name = ''):
    if os.path.isfile(path) and f == False:
        pass
    else:
        _path = os.path.dirname(path)
        makeDir(_path)                       
        f = open(path,'w')
        f.write(content)
        f.close()
        

class Offliner(object):
    url = None;
    replaceList = []
    charset = None
    def __init__(self,charset = None):
        self.charset = charset
    def setUrl(self,url):        
        self.url = url
    def getContent(self,url):
        #print url
        req = urllib2.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
        try:
            response = urllib2.urlopen(req)
            res = response.read()
            self.charset = getCharset(res)
            #print self.charset
            if self.charset:
                res = res.decode(self.charset)
            response.close()
        except Exception as what:
            print url
            print what
            res = ''
        return res
    def soup(self,html):
        return BeautifulSoup(html)
    
    
    def parseRelaceList(self, url, path):
        hash = md5(url).hexdigest()
        value = {'from':url,'to':path}
        obj = {hash:value}
        self.replaceList.append(obj)
            
    def retrieveFile(self, url, path):  
        #print path
        if os.path.isfile(path) == False:
            #print path
            try:
                res =urllib2.urlopen(url).read()
                f = open(path,'wb')
                f.write(res)
                f.close()  
            except Exception as what:
                print what
                pass                
                      
            #urllib.urlretrieve(url, path)   
            
    def getSavePath(self,path):
        if path[0] == '/':
            path = path[1:]
        _path = os.path.join(pro_dir,path) 
        
        dir = os.path.dirname(_path)
        #print dir
        #print _path
        if os.path.isdir(dir) == False:
            makeDir(dir)               
        return _path

    #解析CSS
    def parseCss(self, css_url):
        cssContent = self.getContent(css_url)
        p = re.compile("url\((.*?)\)")
        imgs = re.findall(p,cssContent)
        #print urlparse(css_url).path
        o = urlparse(css_url)
        http_host = "%s://%s" % (o.scheme,o.netloc)
        for img in imgs:
            img_path = img.strip('"').strip('\'')
            path = urlparse(img_path)
            if path.scheme:
                img_url = img_path
                img_path = path.path
            else:
                img_url = http_host+img_path
                
            img_save_path = self.getSavePath(img_path)
            #print img_save_path
            self.retrieveFile(img_url, img_save_path)
 
    def processCss(self, res):
        soup = self.soup(res)
        cssFiles = soup('link',href=True)
        for css in cssFiles:
            if ".css" in css['href']:
                css_url = css['href']
                css_path = urlparse(css_url).path
                #print css_path
                css_save_path = self.getSavePath(css_path)
                self.retrieveFile(css_url, css_save_path)                
                self.parseRelaceList(css_url,css_path)
                self.parseCss(css_url)
    
    def processJs(self, res):
        soup = self.soup(res)
        jsFiles =  soup.findAll('script',src=True)
        for js in jsFiles:
            js_url = js['src']
            js_path = urlparse(js_url).path
            js_save_path = self.getSavePath(js_path)
            self.retrieveFile(js_url, js_save_path)
            
            self.parseRelaceList(js_url,js_path)
            #print js_save_path

    def processImg(self, res):
        soup = self.soup(res)
        img_pre = ['.gif','.jpg','.png']
        imgFiles =  soup.findAll('img',src=True)
        for img in imgFiles:
            img_url = img['src']
            
            img_path = urlparse(img_url).path            
            #if img_url == 'http://fun.51fanli.com/topheader/ajaxGetInfoForTopbar/type/kf/size/big':
            #    continue
            img_save_path = self.getSavePath(img_path)
            self.retrieveFile(img_url, img_save_path)
            self.parseRelaceList(img_url, img_path)
    
    def run(self):
        print self.url
        res = self.getContent(self.url)
        #path = urlparse(self.url).path
        path = urlparse(self.url).path
        
        path = path+'.html'
        
        self.processJs(res)
        #print self.replaceList
        self.processCss(res)
        self.processImg(res)
        #保存HTML
        save_path = self.getSavePath(path)
        
        for rep in self.replaceList:
            for i in rep:
                v = rep[i] 
              
            res = res.replace(v['from'], v['to'])
        if self.charset:            
            res = res.replace(self.charset, )
            res = res.encode('utf-8')
        if(os.path.exists(save_path)):
            save_path = save_path+str(time.time())
        putContent(save_path,res,True)
       

def main():
    off = Offliner()

    urls = []
    urls.append("http://www.51fanli.com/index.html")
    urls.append("http://www.51fanli.com/procat.asp")
    urls.append("http://www.51fanli.com/product-1359.html")
    url = "http://www.51fanli.com/gift.asp"
    urls.append(url)
    url = 'http://www.51fanli.com/gift.asp?gid=605128'
    urls.append(url)
    url = 'http://passport.51fanli.com/login'
    urls.append(url)
    url = 'http://passport.51fanli.com/reg?action=yes'
    urls.append(url)
    url = 'http://passport.51fanli.com/reg/agreement'
    urls.append(url)
    url = 'http://help.51fanli.com/a/xinshouxuetang/index.html'
    urls.append(url)
    url = 'http://www.51fanli.com/gift.asp?t=1&u=0&p=0&c=0&isindex=0'
    urls.append(url)
    url = 'http://www.51fanli.com/procat.asp?cid=34'
    urls.append(url)
    url = 'http://www.51fanli.com/invite.asp?ref=topbara'    
    urls.append(url)
    
    for _url in urls:        
        #print _url
        off.setUrl(_url)
        off.run()

if __name__ == '__main__':
    main()
    
    
    
    
    