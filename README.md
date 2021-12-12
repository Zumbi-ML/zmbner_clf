# Zumbi Annotator


## Training (pt_BR)

```bash
prodigy ner.manual zmbner_train_db pt_core_news_lg ./data/stp04-inputs-4-annotatation/sentences_4_training.jsonl --label PER,ORG,PUBLIC,EDUCATIONAL,CITY,STATE,COUNTRY,WORK,MOVEMENT,POLICE,LAW,MEDIA --patterns ./data/stp04-inputs-4-annotatation/pt_ner_patterns.jsonl
```
