#_*_ coding: utf-8_*_

"""
Package method function
"""

import urllib2
import requests
import numpy as np


class NetworkUtils:
    '''
    Pakage class used for netword request
    '''
    # The unchanged first half and the second half of the url
    CONSTANT_URL = ["https://nusmods.com/modules?p=", "&sem[0]=1&sem[1]=2&sem[2]=3&sem[3]=4"]

    def __init__(self):
        pass

    def get_func(self, url):
        return requests.get(url)

    def open_url(self, url):
        req = urllib2.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4132.400')
        response = urllib2.urlopen(req)
        print("open" + url)
        return response.read().decode('utf-8')


class DataUtils:
    '''
    Used for some data caculating process
    '''
    def __init__(self):
        pass

    def random_sample(self, num, _in_num):
        random_arr = np.arange(len(_in_num))
        np.random.shuffle(random_arr)
        return random_arr[0:num]
