# -*- coding: UTF-8 -*-

import json
from utils import filehelper as fh

def jsonlify(input_path):
    """
    Converts strings to the JSONL format
    """
    sentences = fh.concat_articles_content(input_path)
    jsonlified_lst = []
    for sentence in fh.split(sentences):
        jsonlified_lst.append(json.dumps({"text": sentence}))
    return jsonlified_lst

def jsonlify_n_save(input_path, output_file):
    """
    Converts strings to the JSONL format and saves it to the disk
    """
    jsonlified_lst = jsonlify(input_path)
    fh.write_list_into(output_file, jsonlified_lst, end='\n')
