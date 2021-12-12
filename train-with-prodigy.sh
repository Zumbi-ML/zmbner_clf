#!/usr/bin/env zsh

prodigy train --ner zmbner_train_db --eval-split 0.3 --gpu-id 0 --verbose --lang pt --label-stats models/model-v1.0/
