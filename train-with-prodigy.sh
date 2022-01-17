#!/usr/bin/env zsh

prodigy train --ner zmbner_clf_train_db_v1 --eval-split 0.3 --verbose --lang pt --label-stats models/model-v1.0/
