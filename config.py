# Common
# ==============================================================================

BASE_DIR = "data/"

ARTICLES_DIR = "news_articles/"

# Scrapper
# ==============================================================================

SCRAPPER_FILE_INPUT_DIR = BASE_DIR + ARTICLES_DIR + "stp00_scrapper/"

SCRAPPER_FILE_OUTPUT_DIR = BASE_DIR + ARTICLES_DIR + "stp01_raw/"

SCRAPPER_INPUT_FILENAME = SCRAPPER_FILE_INPUT_DIR + "URLs.tsv"

SCRAPPER_OUTPUT_FILENAME = SCRAPPER_FILE_OUTPUT_DIR + "raw_articles_content.txt"

# Sentencizer
# ==============================================================================

SENTENCIZER_INPUT_DIR = SCRAPPER_FILE_OUTPUT_DIR

SENTENCIZER_OUTPUT_DIR = BASE_DIR + ARTICLES_DIR + "stp02_sentencized/"

SENTENCIZER_OUTPUT_FILENAME = SENTENCIZER_OUTPUT_DIR + "sentencized_text.txt"

# Patternifier
# ==============================================================================

PATTERNIFIER_INPUT_DIR = BASE_DIR + ARTICLES_DIR + "stp03_patterns/"

PATTERNIFIER_OUTPUT_DIR = BASE_DIR + "stp04-inputs-4-annotation/"

PATTERNIFIER_OUTPUT_FILENAME = PATTERNIFIER_OUTPUT_DIR + "pt_ner_patterns.jsonl"

# JSONlifier
# ==============================================================================

JSONLIFIER_INPUT_DIR = SENTENCIZER_OUTPUT_DIR

JSONLIFIER_OUTPUT_DIR = BASE_DIR + "stp04-inputs-4-annotation/"

JSONLIFIER_OUTPUT_FILENAME = JSONLIFIER_OUTPUT_DIR + "sentences_4_training.jsonl"
