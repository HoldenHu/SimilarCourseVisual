#_*_ coding: utf-8_*_

"""
Get the modules from nusmods website
Using manual crawler
"""

import time
import urllib2
import os
import pickle
import numpy
import re
import sqlite3

# The unchanged first half and the second half of the url
CONSTANT_URL = ["https://nusmods.com/modules?p=" , "&sem[0]=1&sem[1]=2&sem[2]=3&sem[3]=4"]


# Get the request message
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4132.400')
    response = urllib2.urlopen(req)
    print("open"+url)
    print response.read().decode('utf-8')
    return response.read().decode('utf-8')

def get_one_module_infomation(url):
    return


#  Main API function used for crawl
def crawl_from_nusmods():
    page_count = 1  # Iteration of page number
    module_page_count = 4  #  Count of modules in one page, used for the stop of while cycle
    #while module_page_count < 4:


    #return All_Book


# if __name__=="__main__":
#     #crawl_from_nusmods()
#     open_url("https://nusmods.com/modules/?p=1168")

