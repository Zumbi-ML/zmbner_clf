#!/usr/bin/env zsh

prodigy ner.correct zmbner_train_db pt_core_news_lg ./data/stp04-inputs-4-annotation/sentences_4_training.jsonl --label PER,ORG,PUBLIC,EDUCATIONAL,CITY,STATE,COUNTRY,WORK,MOVEMENT,POLICE,LAW,MEDIA
