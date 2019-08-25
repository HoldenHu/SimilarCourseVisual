# encoding: utf-8
import os
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

from lib.global_variable import *
from store_to_db import *
from crawl_from_api import *
from training_data import build_model
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from collections import Counter
from db_handler import *
from mods_db import ModsDB


SHOW_WORD_NUM =50


def build_corpus(keywords_list):
    wordsCounter = Counter()
    for each_list in keywords_list:
        for each_word in each_list:
            if len(each_word) > 1 and each_list != '\r\n':
                wordsCounter[each_word] += 1

    return wordsCounter


def word_and_vec_list(corpus):
    words_list = []
    words_vectors = []
    # Add the top 50 words with the highest frequency
    for i in range(SHOW_WORD_NUM):
        words_list.append(corpus.most_common(SHOW_WORD_NUM)[i][0])
    # Add the vector representation of each word
    for each_word in words_list:
        try:
            words_vectors.append(model.wv.get_vector(each_word))
        except:
            words_list.remove(each_word)
    words_vectors = np.array(words_vectors)

    return words_list, words_vectors


def plotTsne2D(word_vectors, words_list):
    plt.cla()
    plt.close("all")

    tsne = TSNE(n_components=2, random_state=0, n_iter=10000, perplexity=20)
    # 在控制台输出过程中，默认小数会以科学计数法的形式输出，若不需要加上下面这句
    np.set_printoptions(suppress=True)
    T = tsne.fit_transform(word_vectors)
    labels = words_list

    plt.figure(figsize=(14, 10))
    plt.scatter(T[:, 0], T[:, 1], c='blue', edgecolors='k')

    for label, x, y in zip(labels, T[:, 0], T[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')

    plt.show()


if __name__=="__main__":
    # save_code_description(2018, 2019 ,1)  # Crawl course information online and save it in the database
    # update_database()
    mods_db = ModsDB(DB_LOCATION)  # Handler of Database

    #  keywords_list contain keywords in every module' descriptions, store one by one
    classcode_list, keywords_list = keywords_list_from_db(mods_db)

    if os.path.exists(MODEL2_LOCATION):
        model = Word2Vec.load(MODEL2_LOCATION)  # Load trained model
    else:
        model = build_model(keywords_list)  # Training data from scratch, embedding words

    corpus = build_corpus(keywords_list)  # A word counter including all keywords

    # Store the 100 words with the highest frequency and their Vec
    words_list, words_vectors = word_and_vec_list(corpus)

    print len(words_vectors)

    plotTsne2D(words_vectors, words_list)

