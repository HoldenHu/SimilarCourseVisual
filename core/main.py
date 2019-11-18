# encoding: utf-8
import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from lib.global_variable import *
from crawl_from_api import *
from training_data import build_model
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from collections import Counter
from db_handler import *
from word_frenquency import draw_word_count
from mods_db import ModsDB
import logging

logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)


def build_corpus(keywords_list):
    '''
    Count the frequency of occurrences of all the words in the description
    :param keywords_list: [['word','word'],]
    :return: [('word':count),]
    '''
    wordsCounter = Counter()

    for each_list in keywords_list:
        for each_word in each_list:
            if len(each_word) > 1 and each_list != '\r\n':
                wordsCounter[each_word] += 1

    logging.info('Holden: Finish build_corpus')
    return wordsCounter


def word_and_vec_list(corpus):
    '''
    Return the SHOW_WORD_NUM most frequently occurring words in the entire library and their encodings back
    :param corpus: [('word':count),]
    :return: ['word',], [[0,0],]
    '''
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

    logging.info('Holden: Finish turn corpus to most frequently occurring words in the entire library')
    return words_list, words_vectors


def plot_tsne2d(word_vectors, words_list):
    '''
    Convert vector to 2D coordinates, display on 2D chart and draw
    :param word_vectors: np.array([[0,0,],])
    :param words_list: ['word',]
    :return: show figure
    '''
    plt.cla()
    plt.close("all")

    tsne = TSNE(n_components=2, random_state=0, n_iter=10000, perplexity=20)
    # In the console output process, the default decimal is output in the form of scientific notation
    np.set_printoptions(suppress=True)
    T = tsne.fit_transform(word_vectors)
    labels = words_list

    plt.figure(figsize=(14, 10))
    plt.scatter(T[:, 0], T[:, 1], c='blue', edgecolors='k')

    for label, x, y in zip(labels, T[:, 0], T[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points',)
    plt.show()

    logging.warning('Holden: Finish draw plt')
    return


def word2vec_by_class(list):
    '''
    Convert the list of keywords in each class into a vector collection
    :param list: [['word','word',],]
    :return: [[[0,0,],],]
    '''
    classvec_by_class_list = []
    for each_class in list:
        eachclass_vec_list = []
        for each_word in each_class:
            try:
                eachclass_vec_list.append(model.wv.get_vector(each_word))
            except Exception, e:
                logging.error('Holden: ERROR: ' + str(e))
                print e
        classvec_by_class_list.append(eachclass_vec_list)

    return classvec_by_class_list


def mean_class_vec_list(classvec_by_class_list):
    '''
    Average all word vectors for each course, representing the vector for each course
    :param classvec_by_class_list: [[[0,0,],],]
    :return: [[0,0,],]
    '''
    classvec_list = []
    for each_classvec in classvec_by_class_list[0:SHOW_WORD_NUM]:
        each_classvec_np = np.array(each_classvec)
        classvec_list.append(np.mean(each_classvec_np, axis=0))

    classvec_list = np.array(classvec_list)
    return classvec_list


def draw_top_frequency(keywords_list):
    '''
    Draw the most frequently occurring words in the entire corpus into Wordcloud, and draw plot of them
    :param keywords_list: [['word','word'],]
    :return: Draw plot
    '''
    corpus = build_corpus(keywords_list)  # A word counter including all keywords
    draw_word_count(corpus)
    print("saved the words cloud")

    # Store the 100 words with the highest frequency and their Vec
    words_list, words_vectors = word_and_vec_list(corpus)
    plot_tsne2d(words_vectors, words_list)

    logging.info('Holden: Finish drawing top frequency word')
    logging.info('Holden: corpus:')
    logging.info(str(corpus))
    return


def draw_modules_relation(keywords_list,classcode_list):
    '''
    Draw the modules'relationships based on the entire corpus, and draw plot of them
    :param keywords_list: [["word",],]
    :param classcode_list: ["CS5242",]
    :return: Draw plot
    '''
    classvec_by_class_list = word2vec_by_class(keywords_list)
    classvec_list = mean_class_vec_list(classvec_by_class_list)

    plot_tsne2d(classvec_list, classcode_list)
    logging.info('Holden: Finish drawing class relationship')
    return


if __name__=="__main__":

    mods_db = ModsDB(DB_LOCATION)  # Handler of Database

    #  keywords_list contain keywords in every module' descriptions, store one by one. All data
    all_classcode_list, all_keywords_list = keywords_list_from_db(mods_db)

    sample_classcode_list, sample_keywords_list = random_keywords_list_from_db(mods_db)

    if os.path.exists(MODEL2_LOCATION):
        model = Word2Vec.load(MODEL2_LOCATION)  # Load trained model
    else:
        model = build_model(all_keywords_list)  # Training data from scratch, embedding words

    # Save the word cloud to docs/cloudWord.html. And draw the similarity graph of top frequency words
    if sys.argv[1] == "drawWords":
        print("start to draw to frequency words")
        draw_top_frequency(all_keywords_list)

    # draw the similarity graph of sample modules
    if sys.argv[1] == "drawModules":
        draw_modules_relation(sample_keywords_list, sample_classcode_list)



