#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from config import *
import argparse
from app.sentencizer import sentencize_n_save
from app.jsonlifier import jsonlify_n_save
from app.patternifier import patternify_n_save

# Main
# ==============================================================================

def main(input_path, output_path):
    """
    Main function
    """
    #sentencize_n_save(input_path, output_path)
    #jsonlify_n_save(input_path, output_path)
    patternify_n_save(input_path, output_path)

if (__name__ == '__main__'):
	#parser = argparse.ArgumentParser()

	# Sentencizer
	#in_sent_help_msg = \
	#"""
	#Input path containing the `.txt` files with the content to be sentencized
	#"""
	#parser.add_argument("-is", "--input_sent", type=str, help=in_sent_help_msg)

	#out_sent_help_msg = \
	#"""
	#Sentencizer output path
	#"""
	#parser.add_argument("-os", "--output_sent", type=str, help=out_sent_help_msg)

	#args = parser.parse_args()
	#input_sent = args.input_sent if args.input_sent else SENTENCIZER_INPUT_DIR
	#output_sent = args.output_sent if args.output_sent else SENTENCIZER_OUTPUT_DIR

	main(PATTERNIFIER_INPUT_DIR, PATTERNIFIER_OUTPUT_DIR)
