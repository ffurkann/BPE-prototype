import regex as re
import json


sentence=input("Enter a sentence:")

word_list=sentence.strip().lower().split()

for i in range(len(word_list)):
    for j in word_list[i]:
        if re.fullmatch(r'\p{L}',j):
            continue
        else:
            word_list[i]=word_list[i].replace(j,"")


try:
    with open ("corpus.json") as f:
        corpus=json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    corpus=[]


try:
    with open ("Merge_history.json") as f:
        Merge_history=json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    Merge_history=[]


try:
    with open ("Vocab.json") as f:
        Vocab=json.load(f)

except (FileNotFoundError, json.JSONDecodeError):
    Vocab={}


for i in word_list:
    corpus.append(list(i))
    corpus[-1].append("</w>")

def pair_count(corpus):
    pair_dict = {}
    for word in corpus:
        for i in range(len(word)-1):
            if word[i+1]!="</w>":
                pair=tuple(word[i:i+2])
                if pair in pair_dict:
                    pair_dict[pair]+=1
                else:
                    pair_dict[pair]=1
    return pair_dict

def merger(pairs,corpus):
    most_frequent=max(pairs, key=pairs.get)
    merged_corpus=[]
    for i in range(len(corpus)):
        merged=list(corpus[i])
        for j in range(len(merged)-1):
            if most_frequent==tuple(merged[j:j+2]):
                merged[j]=most_frequent[0]+most_frequent[1]
                merged.pop(j+1)
        merged_corpus.append(merged)
    merged_pair=most_frequent
    return merged_corpus,merged_pair

def vocab_create(corpus,Vocab):
    id_counter=0
    for i in corpus:
        for j in i:
            if j not in Vocab:
                Vocab[j]=id_counter
                id_counter+=1
    return Vocab


while True:
    pairs=pair_count(corpus)
    if len(pairs)==0:
        break
    else:
        corpus,merged_pair=merger(pairs,corpus)
        Merge_history.append(merged_pair)


Vocab=vocab_create(corpus,Vocab)




with open ("corpus.json","w") as f:
    json.dump(corpus, f, indent=2)



with open ("Merge_history.json","w") as f:
    json.dump(Merge_history, f, indent=2)

with open ("Vocab.json","w") as f:
    json.dump(Vocab, f, indent=2)


