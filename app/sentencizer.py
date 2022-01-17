# -*- coding: UTF-8 -*-

import glob
import re
from utils import filehelper as fh

def sentencize(input_path):
    """
    Sentencize the contents of a file
    """
    LOWER_BOUND = 15
    UPPER_BOUND = 400
    articles_content = fh.concat_articles_content(input_path)
    sentencized = []
    for sentence in fh.split(articles_content):
        if (not contains_credit_msg(sentence) and
            n_words(sentence) > LOWER_BOUND and
            n_words(sentence) < UPPER_BOUND and
            not contains_photo_enum(sentence) and
            not contains_redirect_links(sentence.lower()) and
            not contains_links(sentence) and
            not contains_pic_links(sentence)
            ):
            sentencized.append(sentence)
    return sentencized

def sentencize_n_save(input_path, output_file):
    """
    Sentencize and save to disk
    """
    sentencized_lst = sentencize(input_path)
    fh.write_list_into(output_file, sentencized_lst)

# Aid functions
# ==============================================================================

def contains_credit_msg(text):
    """
    Contains credit msg
    """
    contains = False

    credit_freq_expr = ['Reprodução', 'Foto', 'Imagem', 'Divulgação', 'Crédito', 'Legenda']

    for expr in credit_freq_expr:
        contains = contains or expr in text
    return contains

def n_words(text):
    """
    Counts the number of words in a text
    """
    return len(text.split(" "))

def contains_photo_enum(text):
    """
    Checks if there are photo enumeration
    """
    result = re.match(r'\d+ de \d+', text)
    return True if result else False

def contains_redirect_links(text):
    """
    Checks if sentence contains redirect links
    """
    redirect_freq_expr = ['veja também', 'saiba mais', 'saiba como', 'veja:']
    contains = False
    for expr in redirect_freq_expr:
        contains = contains or expr in text
    return contains

def contains_links(text):
    """
    Returns `True` if `http` is in `text`
    """
    return "http" in text

def contains_pic_links(text):
    """
    Returns `True` if `pic.twitter.com` is in `text`
    """
    return True if "pic.twitter.com" in text else False
