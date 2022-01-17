# -*- coding: UTF-8 -*-

import re
import glob

def read(full_filename):
	"""
	Read the content of a file
	"""
	with open(full_filename, 'r') as file:
		return file.read()

def write_list_into(filename, lst, end='\n\n'):
	"""
	Write `lst` into `filename`
    Args:
        filename: The filename to be saved
        lst: The list of sentences to be written to the file
	"""
	with open(filename, 'w') as file:
		for text in lst:
			file.write(text + end)

def write(filename, content):
    """
    Write the content to the file
    """
    with open(filename, 'w') as f:
        f.write(content)

def concat_articles_content(dir):
    """
    Concatenate the articles' content into a single string
    """
    content = ""
    for filename in get_filenames(dir):
        content += read(filename)
        content += "\n"
    return content

def get_filenames(dir, file_ext=".txt"):
    """
    Returns a list of filenames in the specified dir
    """
    return glob.glob(dir + "*" + file_ext)

def split(text):
    """
    Splits a text into a list of sentences
    """
    text = re.sub(r'\n+', '\n', text)
    return text.split('\n')
