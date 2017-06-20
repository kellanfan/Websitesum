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
if os.path.exists('./README.md'):
    print "File exist"

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
