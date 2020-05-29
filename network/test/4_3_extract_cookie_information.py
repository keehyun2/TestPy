#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import cookielib 
import urllib
import urllib2

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = 'keehyun2@gmail.com'
PASSWORD = 'asdfdg93'
LOGIN_URL = 'https://bitbucket.org/account/signin/?next=/'
NORMAL_URL = 'https://bitbucket.org/'

BROWSER = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0'

def extract_cookie_info():
    """ Fake login to a site with cookie"""
    # setup cookie jar
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME : USERNAME, 
                                   ID_PASSWORD : PASSWORD})
    # create url opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', BROWSER)]
    resp = opener.open(LOGIN_URL, login_data)

    # send login info 
    for cookie in cj:
        print "----First time cookie: %s --> %s" %(cookie.name, cookie.value)
    print "Headers: %s" %resp.headers

    # now access without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print "++++Second time cookie: %s --> %s" %(cookie.name, cookie.value)
    
    print "Headers: %s" %resp.headers

if __name__ == '__main__':
    extract_cookie_info()
