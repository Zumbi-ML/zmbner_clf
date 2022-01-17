# Zumbi NER Classifier

## Creating the gold-standard dataset

### Using the manual recipe

```bash
prodigy ner.manual zmbner_clf_train_db_v1 pt_core_news_lg data/stp04-inputs-4-annotation/sentences_4_training.jsonl  --label PER,ORG,CITY,STATE,COUNTRY,WORK,LAW,MEDIA --patterns data/stp04-inputs-4-annotation/pt_ner_patterns.jsonl
```

### Using active learning

```bash
prodigy ner.correct zmbner_clf_train_db_v1 pt_core_news_lg ./data/stp04-inputs-4-annotation/sentences_4_training.jsonl --label PER,ORG,CITY,STATE,COUNTRY,WORK,LAW,MEDIA
```

## Training (pt_BR)

```bash
prodigy train --ner zmbner_clf_train_db_v1 --eval-split 0.3 --gpu-id 0 --verbose --lang pt --label-stats models/model-v0.0.1/
```

## Packaging (pt_BR)

```bash
python -m spacy package models/model-v0.0.1/model-best packages --name zmbner_clf --version 0.0.0 --force
```

## Installation

```bash
pip install packages/pt_zmbner_clf-0.0.0/dist/pt_zmbner_clf-0.0.0.tar.gz
```
