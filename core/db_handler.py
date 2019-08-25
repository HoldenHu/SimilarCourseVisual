from lib.global_variable import *
from mods_db import ModsDB
from rake_nltk import Rake

r = Rake()

def keywords_list_from_db(mods_db):
    classcode_list = []
    keywords_list = []
    modules_db = mods_db.read_all_from_sqlite()

    row_count = len(modules_db)
    for row in range(row_count):
        r.extract_keywords_from_text(modules_db[row][2])
        classcode_list.append(modules_db[row][1])
        keywords_list.append(r.get_word_degrees().keys())

    return classcode_list, keywords_list


# if __name__=="__main__":
#     mods_db = ModsDB(DB_LOCATION)
#     classcode_list, keywords_list = keywords_list_from_db(mods_db)
#     print classcode_list
