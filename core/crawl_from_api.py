#_*_ coding: utf-8_*_

"""
Get the modules from official nusmods api
Return Json pakage
e.g.
Get module code: http://api.nusmods.com/2018-2019/1/moduleCodes.json
Get module List: http://api.nusmods.com/2015-2016/1/moduleList.json
Get module details: http://api.nusmods.com/2014-2015/2/modules/FE5218.json
"""

import urllib2
import requests
import json
import store_to_db
from store_to_db import *

# Constant domain
CONSTANT_DOMAIN = "http://api.nusmods.com/"


# Get the request message
def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36'
                   ' (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4132.400')
    response = urllib2.urlopen(req)

    return response.read()


def get_code_description(year_1, year_2, semester):
    counter = 1
    code_list = json.loads(open_url(CONSTANT_DOMAIN + str(year_1) + "-" + str(year_2) + "/" + str(semester) + "/moduleCodes.json"))
    print code_list

    for each_code in code_list:
        if if_module_exist(each_code) == True:
            continue
        each_module_detail = json.loads(open_url(CONSTANT_DOMAIN + str(year_1) + "-" + str(year_2) + "/" + str(semester) + "/modules/" + each_code + ".json"))
        try:
            store_to_sqlite(counter, each_code, each_module_detail['ModuleDescription'])
        except Exception, e:
            print e
        counter = counter + 1
        print counter


if __name__ == "__main__":
    get_code_description(2018, 2019, 1)