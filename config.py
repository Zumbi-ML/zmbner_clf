# Common
# ==============================================================================

BASE_DIR = "news_articles/"

RAW_FILE_OUTPUT_DIR = BASE_DIR + "stp01_raw/"

# Sentencizer
# ==============================================================================

SENTENCIZER_INPUT_DIR = RAW_FILE_OUTPUT_DIR

SENTENCIZER_OUTPUT_DIR = BASE_DIR + "stp02_sentencized/"

# JSONlifier
# ==============================================================================

JSONLIFIER_INPUT_DIR = SENTENCIZER_OUTPUT_DIR

JSONLIFIER_OUTPUT_DIR = "train/"

# Patternifier
# ==============================================================================

PATTERNIFIER_INPUT_DIR = BASE_DIR + "stp03_patterns/"

PATTERNIFIER_OUTPUT_DIR = "train/"
