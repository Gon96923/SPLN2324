import spacy

nlp = spacy.load('pt_core_news_lg')

ex = "O gato e o cão 1 foram de bicicleta para Ponte de Lima. O gato caiu e o cão riu."
doc = nlp(ex)

tokens = []
for token in doc.ents:
    tokens.append((token.text,token.label_, token.lemma_))

i=0
f_list = []
for token in doc:
    if token.ent_iob_ == 'B':
        f_list.append(tokens[i])
        i = i+1
    if token.ent_iob_ == 'O':
        f_list.append((token.text, token.pos_, token.lemma_))

print("Palavra______POS______Lema")
for token in f_list:
    print(f"|{token[0]}|         |{token[1]}|         |{token[2]}|")
