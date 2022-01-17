# -*- coding: UTF-8 -*-

import json
from random import randint
import re

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')

def save_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def convert(old_, sent_number):
    new_ = {}
    text = old_['text']
    #new_['text'] = text
    new_['spans'] = []
    for span in old_['spans']:
        inner_ = {}
        tk_start = span['start']
        tk_end = span['end']
        inner_['start'] = tk_start
        inner_['end'] = tk_end
        inner_['text'] = text[tk_start:tk_end]
        inner_['label'] = span['label']
        new_['spans'].append(inner_)

    new_['tokens'] = []
    for token in old_['tokens']:
        inner_t = {}
        tk_start = token['start']
        tk_end = token['end']
        inner_t['sent_number'] = sent_number

        inner_t['start'] = tk_start
        inner_t['end'] = tk_end
        inner_t['text'] = token['text']

        assigned_label = False
        for span in new_['spans']:
            span_start = span['start']
            span_end = span['end']

            if (tk_start >= span_start and tk_end <= span_end):
                if (tk_start == span_start):
                    inner_t['label'] = "B-" + span['label']
                else:
                    inner_t['label'] = "I-" + span['label']
                assigned_label = True
                break
        if (not assigned_label):
            inner_t['label'] = "O"
        new_['tokens'].append(inner_t)

    return new_

def split_train_tests(all_samples, perc):
    n_samples = len(all_samples)
    n_tests = int(n_samples * perc)
    indexes = set()
    train, tests = [], []
    while (len(indexes) < n_tests):
        k = randint(0, n_samples)
        indexes.add(k)

    for idx in indexes:
        tests.append(all_samples[idx])

    for i in range(len(all_samples)):
        if (not i in indexes):
            train.append(all_samples[i])
    return train, tests

def to_tsv(samples):
    sent_in_tsv = ""
    for sent_json in samples:
        for token in sent_json['tokens']:
            sn, txt, lbl = token['sent_number'], token['text'], token['label']
            sent_in_tsv += f"{sn}\t{txt}\t{lbl}\n"
    return sent_in_tsv

def main(filename):
    lines = read_file(filename)
    all_samples = []
    sent_counter = 0
    for line in lines:
        if (not line):
            continue
        a_json = json.loads(line)
        sent_counter += 1
        new_ = convert(a_json, sent_counter)
        all_samples.append(new_)

    #train, tests = split_train_tests(all_samples, 0.3)
    str_train = to_tsv(all_samples)
    #str_tests = to_tsv(tests)
    save_file('data/zmb-iob-annotations-train-full.tsv', str_train)
    #save_file('data/zmb-iob-annotations-tests.tsv', str_tests)

filename = 'data/annotated-sentences/exported-annotations-from-zmbner_train_v3_db_2022-01-11-1.jsonl'
main(filename)
