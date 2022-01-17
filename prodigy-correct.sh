#!/usr/bin/env zsh

prodigy ner.correct zmbner_clf_train_db_v1 pt_core_news_lg ./data/stp04-inputs-4-annotation/sentences_4_training.jsonl --label PER,ORG,CITY,STATE,COUNTRY,WORK,LAW,MEDIA
