import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

COULD_HTML_PATH = rootPath + "/docs/cloudWord.html" # The path of top frequency words cloud
STOPWORD_LOCATION = rootPath + "/db/Foxstoplist.txt" # The path of file that store the list of words which make no sense
DB_LOCATION = rootPath + "/db/db.sqlite3" # The path of Sqlite DB to store NUSModule info
MODEL_LOCATION = rootPath + "/db/word_embedding_corpus" # The path of model containing all words in DB
MODEL2_LOCATION = rootPath + "/db/keyword_embedding_corpus" # The path of model containing key words in DB
CONSTANT_DB_PATH = rootPath + "/db/db.sqlite3" # Alias of DB_LOCATION
MAIN_FUNCTION_PATH = rootPath + "/core/main.py" # Program entry

CONSTANT_DOMAIN = "http://api.nusmods.com/" # The domain name to get the info

RANDOM_SAMPLING_NUM = 100  # Random sampling number
SHOW_WORD_NUM = 100  # The number of points shown in the figure
