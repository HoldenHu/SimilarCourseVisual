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
import json
from lib.global_variable import *
from mods_db import ModsDB
import logging


# Get the request message
def open_url(url):
    '''
    Get the pakage from given url. Camouflage man-made behavior
    :param url: http://...
    :return: response
    '''
    logging.info('Holden: Try to get the pakage from' + url)
    req = urllib2.Request(url)
    #  Camouflage man-made behavior
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36'
                   ' (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 QQBrowser/4.1.4132.400')
    response = urllib2.urlopen(req)

    logging.info('Holden: Successully get the pakage from url')
    return response.read()


def save_code_description(year_1, year_2, semester):
    '''
    Crawl course information online and save it in the database
    :param year_1: 2018
    :param year_2: 2019
    :param semester: 1
    :return:
    '''
    counter = 1
    code_list = json.loads(open_url(CONSTANT_DOMAIN + str(year_1) + "-" + str(year_2) + "/" + str(semester) + "/moduleCodes.json"))
    logging.info('Holden: Get code list from mods api successfully' + str(code_list))

    #  Store data to the database
    db = ModsDB(CONSTANT_DB_PATH)
    for each_code in code_list:
        if db.if_module_exist(each_code) == True:
            continue
        each_module_detail = json.loads(open_url(CONSTANT_DOMAIN + str(year_1) + "-" + str(year_2) + "/" + str(semester) + "/modules/" + each_code + ".json"))
        try:
            db.store_to_sqlite(counter, each_code, each_module_detail['ModuleDescription'])
            logging.info('Holden: Save one data of: ' + str(each_code))
        except Exception, e:
            print e
        counter = counter + 1

    logging.info('Holden: Store data to DB')
    del db
    logging.info('Holden: Delete DB handler')
    return