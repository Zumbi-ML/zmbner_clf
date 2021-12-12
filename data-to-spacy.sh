#!/usr/bin/env zsh

prodigy data-to-spacy data/stp05-ready-4-training/annotated-dataset-v1.0.jsonl --ner zmbner_train_db --eval-split 0.3 --lang "pt"

# python -m spacy train data/stp05-ready-4-training/config.cfg --paths.train data/stp05-ready-4-training/train.spacy --paths.dev data/stp05-ready-4-training/dev.spacy
