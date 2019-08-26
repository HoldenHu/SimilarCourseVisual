# encoding: utf-8

from lib.global_variable import *

import pandas as pd
import re
from collections import Counter
import jieba
import jieba.analyse
from pyecharts import WordCloud
from mods_db import ModsDB
import logging


def draw_word_count(word_counter):
    '''
    Express the frequency of occurrences of words in the corpus in the most intuitive way
    :param word_counter: WordsCounter
    :return: Save the drawing files
    '''
    wordsCounter = word_counter

    # draw word cloud
    def counter2list(_counter):
        wordslist,nums = [],[]
        for item in _counter:
            wordslist.append(item[0])
            nums.append(item[1])
        return wordslist,nums

    outputFile = '../docs/cloudWord.html'

    # Extract keywords
    wordslist,nums = counter2list(wordsCounter.most_common(1000))

    cloud = WordCloud("wordCloud", width=1200, height=600, title_pos='center')
    cloud.add(
        ' ',
        wordslist, nums,
        shape='circle',
    )

    cloud.render(outputFile)
    logging.info('Done draw cloud')
    return

