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

    def k_nn(self, target, find_list, place_index):
        target = np.array(target)
        distance = []
        for i in find_list:
            distance.append(np.sqrt(np.sum(np.square(target - i))))

        sorted_distance = distance[:]
        sorted_distance.sort()
        min_2_distance = sorted_distance[0:2]

        if distance.index(min_2_distance[0]) == place_index:
            return distance.index(min_2_distance[1])
        else:

            return distance.index(min_2_distance[0])

# a=[[1,2,3],[3,4,5],[4,5,6],[7,8,9]]
# b=[4,5,6]
# d = DataUtils()
# print d.k_nn(b,a,2)
