#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 20 Jun 2017 09:14:50 PM CST

# File Name: checkwebsite.py
# Description: Check if the web site in the README file is properly accessed

"""

import json
import os
import re
import requests
import markdown


def gethtmllist():
    """
        从README中获取链接列表
    """
    if not os.path.exists('./README.md'):
        print("File not exist..")
        exit()
    with open('README.md','r') as f:
        text = f.read().encode('utf-8')
        htmlmode = markdown.markdown(text)
        reg = r'href="(\S*)"'
        patten = re.compile(reg)
        urls = re.findall(patten, htmlmode)
        return filter(None,map(lambda x:x if x.startswith('http') else '', urls))

def getcode(url):
    header = {
        'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                       'AppleWebKit/537.36 (KHTML, like Gecko)'
                       'Chrome/56.0.2924.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    try:
        response = requests.get(url, headers = header)
        return response.status_code
    except:
        return 400
        
def main():
    get_badsite = []
    for url in gethtmllist():
        code = getcode(url)
        if code == 200:
            print("[ \033[1;35m %s \033[0m ] is OK!" %url)
        else:
            print("[ \033[1;35m %s \033[0m ] is bad website..." %url)
            get_badsite.append(url)

    if not os.path.exists('./badsite.txt'):
        with open('badsite.txt', 'w') as f:
            json.dump(get_badsite, f, indent=4)
    else:
        with open('badsite.json', 'w') as f:
            data = json.load(f)
            for item in get_badsite:
                if item in data:
                    continue
                else:
                    data.append(item)
            json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()
