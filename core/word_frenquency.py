# encoding: utf-8

from lib.global_variable import *

import pandas as pd
import re
from collections import Counter
import jieba
import jieba.analyse
from pyecharts import WordCloud
from mods_db import ModsDB

db = ModsDB(DB_LOCATION)
modules_db = db.read_all_from_sqlite(DB_LOCATION)
row_count = len(modules_db)
content = []
for row in range(row_count):
    content.append(modules_db[row][2])

stopwords = pd.read_csv(STOPWORD_LOCATION, sep='\n', names=['stopwords'],header=None)

pattern = re.compile('\d+')



def compute_word_count():
    # 存放词语和词频
    wordsCounter = Counter()

    for row in range(row_count):
        segs = jieba.lcut(modules_db[row][2])
        for seg in segs:
            if len(seg) > 1 and seg != '\r\n' and re.search(pattern, seg) == None:
                wordsCounter[seg] += 1

    print wordsCounter

    # 将Counter的键提取出来做list
    segment = list(wordsCounter)

    # 将分好的词列表转化为词典
    words = pd.DataFrame({'segment':segment})

    # 剔除停用词
    words = words[~words['segment'].isin(stopwords['stopwords'])]

    print words

    # 绘制词云
    def counter2list(_counter):
        wordslist,nums = [],[]
        for item in _counter:
            wordslist.append(item[0])
            nums.append(item[1])
        return wordslist,nums

    outputFile = '../docs/cloudWord.html'

    # 这个关键词抽取方法不唯一
    wordslist,nums = counter2list(wordsCounter.most_common(1000))

    cloud = WordCloud("wordCloud", width=1200, height=600, title_pos='center')
    cloud.add(
        ' ',
        wordslist, nums,
        shape='circle',
    )

    cloud.render(outputFile)

    print "Done the outputFile"
