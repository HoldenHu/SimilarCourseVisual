# encoding: utf-8
import multiprocessing
import pandas as pd
import re
import jieba
import logging

from gensim.models import Word2Vec
from lib.global_variable import *
from mods_db import ModsDB

stopwords = pd.read_csv(STOPWORD_LOCATION, sep='\n', names=['stopwords'],header=None)

pattern = re.compile('\d+')


def build_model(keywords_list):
    '''
    Embedding data by using Word2Vec
    :param keywords_list: [["word",],]
    :return: model
    '''
    # Training model
    model = Word2Vec(keywords_list, min_count=1, sg=0, workers=multiprocessing.cpu_count())
    logging.info('Holden: Embedding word successfully')

    model.save(MODEL2_LOCATION)
    logging.info('Holden: Save model to' + MODEL2_LOCATION)
    return model


def test_similar_from_bd(db, test_list):
    '''
    Find most similar word in the corpus
    :param db: ModsDB
    :param test_list: ["word",]
    :return: [("word",0.9),]
    '''
    modules_db = db.read_all_from_sqlite(DB_LOCATION)
    row_count = len(modules_db)

    corpus = []

    # Convert the stop word dataFrame to a list
    stopwords_list = stopwords['stopwords'].tolist()
    # print(stopwordsList[:10])
    for row in range(row_count):
        segs = jieba.lcut(modules_db[row][2])
        segs = filter(lambda x: len(x) > 1, segs)
        segs = filter(lambda x: re.search(pattern, x) == None, segs)
        segs = filter(lambda x: x not in stopwords_list, segs)

        corpus.append(list(segs))

    # Training model
    model = Word2Vec(corpus, min_count=20, sg=0, workers=multiprocessing.cpu_count())

    # Query and input a list with high relevance
    return model.wv.most_similar(test_list, topn=15)


def test_similar_from_model(test_list):
    '''
    Find most similar word in the corpus, but the model is loaded by trained model
    :param test_list: ["word",]
    :return: [("word",0.9),]
    '''
    model = Word2Vec.load(MODEL2_LOCATION)
    logging.info('Holden: Load model from ' + MODEL2_LOCATION + 'sucessfully')

    return model.wv.most_similar(test_list, topn=15)