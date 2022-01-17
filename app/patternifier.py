# -*- coding: UTF-8 -*-

import json
from utils import filehelper as fh

def patternify(input_path):
    """
    Converts strings into spacy pattern file
    """
    concatenated_text = fh.concat_articles_content(input_path)
    patternified_lst = []
    for line in fh.split(concatenated_text):
        if (not line):
            continue
        entity, label = line.split('\t')
        token_lst = []
        for token in entity.split(' '):
            token_lst.append({"lower": token.lower()})
        item = json.dumps({"pattern": token_lst, "label": label})
        patternified_lst.append(item)
    return patternified_lst

def patternify_n_save(input_path, output_file):
    """
    Converts strings into spacy pattern file and saves it to the disk
    """
    patternified_lst = patternify(input_path)
    fh.write_list_into(output_file, patternified_lst, end='\n')
