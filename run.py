#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import *
import argparse
from app.sentencizer import sentencize_n_save
from app.jsonlifier import jsonlify_n_save
from app.patternifier import patternify_n_save
from app.scrapper import scrape_n_save

# Main
# ==============================================================================

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    help_msg = \
	"""
	The apps to be executed, separated by comma.
    \tOptions:
    \t\t- scrapper
    \t\t- sentencizer
    \t\t- jsonlifier
    \t\t- patternifier
    \t\t- all
    \tExample:
    \t\tpython run.py --apps sentencizer,jsonlifier
	"""
    parser.add_argument("-a", "--apps", help=help_msg)
    args = parser.parse_args()

    if (not args.apps):
        print(help_msg)
    else:
        all = False
        if (args.apps == "all"):
            all = True
        args_lst = args.apps.split(",")
        if (not args_lst):
            print(help_msg)
        if (all or "scrapper" in args_lst):
            scrape_n_save(SCRAPPER_INPUT_FILENAME, SCRAPPER_OUTPUT_FILENAME)
        if (all or "sentencizer" in args_lst):
            sentencize_n_save(SENTENCIZER_INPUT_DIR, SENTENCIZER_OUTPUT_FILENAME)
        if (all or "jsonlifier" in args_lst):
            jsonlify_n_save(JSONLIFIER_INPUT_DIR, JSONLIFIER_OUTPUT_FILENAME)
        if (all or "patternifier" in args_lst):
            patternify_n_save(PATTERNIFIER_INPUT_DIR, PATTERNIFIER_OUTPUT_FILENAME)
