#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 20 Jun 2017 09:14:50 PM CST

# File Name: checkwebsite.py
# Description: Check if the web site in the README file is properly accessed

"""

import urllib2, urllib, json
import os, re
import markdown
if not os.path.exists('./README.md'):
    print "File not exist"

header = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/56.0.2924.87 Safari/537.36'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}



def test(url):
    page = urllib2.urlopen(url)
    try:
        code = page.getcode()
        return code
    except:
        print error
f = open('README.md','r')
text = f.read().decode('utf-8')
htmlmode = markdown.markdown(text)
reg = r'href="(\S*)"'
patten = re.compile(reg)
urllist = re.findall(patten, htmlmode)
for url in urllist:
    print test(url)
