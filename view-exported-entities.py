import json

def read_file(filename, sep='\n'):
    with open(filename, 'r') as f:
        return f.read().split(sep)

def write(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def write_lst(filename, lst):
    content = ""
    for line in lst:
        content += line + "\n"
    write(filename, content)

def main():
    ENTITY = "ORG"
    filename = 'data/exported-db-annotations/zmbner_clf_train_db_v1_2022-01-16.jsonl'
    json_sentences = read_file(filename)
    laws_sents = []
    k = 1
    for js in json_sentences:
        if (not js):
            continue
        marker = f"""\"label\":\"{ENTITY}\""""
        if (marker in js):
            laws_sents.append(js)

    for jsonl in laws_sents:
        a_json = json.loads(jsonl)
        text = a_json['text']
        input_hash = a_json["_input_hash"]
        for json_sp in a_json['spans']:
            if (json_sp and json_sp['label'] == f"{ENTITY}"):
                print(k, end="\t")
                start = json_sp['start']
                end = json_sp['end']
                k += 1
                print(f"{input_hash}\t{text[start:end]}", end="")
                print("")

    #write_lst('data/sentences-with-laws.jsonl', laws_sents)

main()
