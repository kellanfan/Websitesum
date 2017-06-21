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


def gethtmllist():
    if not os.path.exists('./README.md'):
        print "File not exist"
    f = open('README.md','r')
    text = f.read().decode('utf-8')
    htmlmode = markdown.markdown(text)
    reg = r'href="(\S*)"'
    patten = re.compile(reg)
    f.close()
    return re.findall(patten, htmlmode)
    

def getcode(url):
    header = {
        'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                       'AppleWebKit/537.36 (KHTML, like Gecko)'
                       'Chrome/56.0.2924.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    req = urllib2.Request(url, headers = header)
    try:
        code = urllib2.urlopen(req, timeout = 10).getcode()
        return code
    except:
        return 400
        
if __name__ == '__main__':
    urllist = gethtmllist()
    get_badsite = {}
    for url in urllist:
        code = getcode(url)
        if code == 200:
            print "[ \033[1;35m %s \033[0m ] is OK!" %url
        else:
            print "[ \033[1;35m %s \033[0m ] is bad website..." %url
            get_badsite[url] = code

with open('badsite.json') as f:
    data = json.load(f)
for key in get_badsite:
    if data.has_key(key):
        data[key] = data[key] + 1
    else:
        data[key] = 400
with open('badsite.json', 'w') as f:
    json.dump(data, f, indent=4)
