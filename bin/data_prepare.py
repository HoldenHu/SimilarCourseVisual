import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from core.crawl_from_api import *

save_code_description(2018, 2019, 1)  # Crawl course information online and save it in the database
