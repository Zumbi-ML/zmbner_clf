# Zumbi Annotator


## Training (pt_BR)

```bash
prodigy ner.manual zmbner_train_db pt_core_news_lg ./train/sentences_4_training.jsonl --label PER,ORG,PUBLIC,EDUCATIONAL,CITY,STATE,COUNTRY,WORK,MOVEMENT,POLICE,LAW,MEDIA --patterns ./train/pt_ner_patterns.jsonl
```
