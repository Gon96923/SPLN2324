from jjcli import *
import sys
import re



def tokenize(files):
    dicionario = {}
    er = re.compile(r'(.+):(\w+)') #expressão regular para encontrar a polaridade
    with open('combined.txt', 'w') as f:
        for file in files:

            ccc = open(file, 'r')
            lines = ccc.readlines()
            for line in lines:
                pal = er.search(line).group(1)
                pol = er.search(line).group(2)
                if pal in dicionario and not pol in dicionario[pal]:
                    dicionario[pal].append(pol)
                else:
                    dicionario[pal] = [pol]
        for key in dicionario:
            f.write(key + ':' + str(dicionario[key]) + '\n')

 
    f.close()
    

files = ['sentilex/result.txt','LEIA/tratamento/lexicon_category.txt','LinguaKIT/Linguakit_categoria.txt']
tokenize(files)

