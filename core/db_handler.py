import numpy as np
import logging

from lib.global_variable import *
from mods_db import ModsDB
from rake_nltk import Rake

r = Rake()


def keywords_list_from_db(mods_db):
    '''
    Return all the course codes in the database and the keywords in the description to the two lists.
    :param mods_db: ModsDB()
    :return: ['CS5242',], [['word',],]
    '''
    classcode_list = []
    keywords_list = []
    modules_db = mods_db.read_all_from_sqlite()

    row_count = len(modules_db)
    for row in range(row_count):
        r.extract_keywords_from_text(modules_db[row][2])
        classcode_list.append(modules_db[row][1])
        keywords_list.append(r.get_word_degrees().keys())

    return classcode_list, keywords_list


def random_keywords_list_from_db(mods_db):
    '''
    Return random courses' codes in the database and the keywords in the description to the two lists.
    :param mods_db: ModsDB()
    :return: ['CS5242',], [['word',],]
    '''
    rand_classcode_list = []
    rand_keywords_list = []
    classcode_list, keywords_list = keywords_list_from_db(mods_db)

    random_arr = np.arange(len(classcode_list))
    np.random.shuffle(random_arr)
    logging.info('Holden: Sample class')
    for i in random_arr[0:RANDOM_SAMPLING_NUM]:
        logging.info('moduleid: '+str(i))
        rand_classcode_list.append(classcode_list[i])
        rand_keywords_list.append(keywords_list[i])

    return rand_classcode_list, rand_keywords_list


# if __name__=="__main__":
#     mods_db = ModsDB(DB_LOCATION)
#     classcode_list, keywords_list = keywords_list_from_db(mods_db)
#     print classcode_list
