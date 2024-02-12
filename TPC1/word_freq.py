#!/usr/bin/env python3
'''
NAME
   word_freq - Calculates word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Show 20 most common
        -n : Order alfabetically
Description'''

from jjcli import *
from collections import Counter
import sys
import re

cl=clfilter("nm:",doc = __doc__) #option values in cl.opt dictionary


def tokenize(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[,;.:_—?!]+',texto)
    #(?: ...) agrupa mas não captura
    return palavras

def imprimeN(lista):
    for pal,num in lista:
        print(f"{pal}   {num}")

def imprimeM(lista):
    for pal,num in lista:
        print(f"{num}   {pal}")

for txt in cl.text():
    lista_palavras = tokenize(txt)

    
    if "-m" in cl.opt:
        ocorr = Counter(lista_palavras)
        imprimeM(ocorr.most_common(int(cl.opt.get("-m"))))
    elif "-n" in cl.opt:
        lista_palavras.sort()
        ocorr = Counter(lista_palavras)
        imprimeN(ocorr.items())
    else:
        ocorr = Counter(lista_palavras)
        imprimeN(ocorr.items())
