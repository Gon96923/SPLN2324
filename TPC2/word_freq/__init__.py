#!/usr/bin/env python3
'''
NAME
   word_freq - Calculates word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Show 20 most common
        -n : Order alfabetically
        -o : Clean the table, oder it by frequency and put in "clean_table.txt"
        -p : Oder by frequency and put in "ocorr.txt"
        -c : Compare the frequency with the table and put the difference in "final.txt"
Description'''

from jjcli import *
from collections import Counter
import sys
import re
import os

__version__ = "0.0.1"


def tokenize(texto):
    palavras = re.findall(r'\w\w+(?:\-\w+)?',texto)
    #(?: ...) agrupa mas não captura
    return palavras

def tokenizeX(texto):
    palavras = re.findall(r'\d+\.\d+\s+\w\w+(?:\-\w+)?',texto.read(),re.DOTALL)
    r = re.compile('(\d+\.\d+)\s+(\w\w+(?:\-\w+)?)')
    d = dict()
    for x in palavras:
        c = r.match(x)
        d[c.group(2)] = c.group(1)
    #(?: ...) agrupa mas não captura
    return d


def clean_table(texto): 

    total = 0
    palavras = re.findall('(\d+)\s+(\w\w+(?:\-\w+)?)',texto)
    lista={}

    for line in palavras:
        num = float(line[0])
        pal = line[1]

        total += num
        if pal not in lista:
            lista[pal] = num

    for y in list(lista):
        if y.lower() in lista and y.capitalize() in lista:
            if lista[y.lower()] > lista[y.capitalize()]:
                lista[y.lower()] = lista[y.lower()] + lista[y.capitalize()]
                del lista[y.capitalize()]
            else:
                lista[y.capitalize()] = lista[y.lower()] + lista[y.capitalize()]
                del lista[y.lower()]
        
    for x in lista:
        lista[x] = (lista[x]/total)*1000000
        
    sorted_lista = sorted(lista.items(), key=lambda x:x[1],reverse=True)

    with open("tests/clean_table.txt", 'w') as f:
        for x in sorted_lista:
            f.write("{:.5f}    ".format(round(x[1], 2)))
            f.write(f"{x[0]}" + "\n")

    return 0

def imprimeN(lista):
    for pal,num in lista:
        print(f"{pal}   {num}")

def imprimeM(lista):
    for pal,num in lista:
        print(f"{num}   {pal}")

def compare(ocorr):
    file = open("tests/ocorr.txt", 'r')
    with open("tests/clean_table.txt", 'r') as f:
        d = tokenizeX(f)
        with open("tests/final.txt", 'w') as b:
            sorted_o = sorted(ocorr.items(), key=lambda x:x[1],reverse=True)
            for x in sorted_o:
                if x in d:
                    b.write(f"{x[1] - float(d[x[0]])}   {x[0]}\n")
                else:
                    b.write(f"{x[1]}   {x[0]}\n")



def aux(ocorr):
    for x in list(ocorr):
        if x.lower() in ocorr and x.capitalize() in ocorr:
            if ocorr[x.lower()] > ocorr[x.capitalize()]:
                ocorr[x.lower()] = ocorr[x.lower()] + ocorr[x.capitalize()]
                del ocorr[x.capitalize()]
            else:
                ocorr[x.capitalize()] = ocorr[x.lower()] + ocorr[x.capitalize()]
                del ocorr[x.lower()]
    for x in ocorr:
        ocorr[x] = (ocorr[x]/ocorr.total())*1000000
    return ocorr


def toFile(ocorr):
    with open("tests/ocorr.txt", 'w') as f:
        sorted_o = sorted(ocorr.items(), key=lambda x:x[1],reverse=True)
        for x in sorted_o:
            f.write("{:.5f}    ".format(round(x[1], 2)))
            f.write(f"{x[0]}" + "\n")


def main():
    cl=clfilter("nopchm:",doc = __doc__) #option values in cl.opt dictionary
    for txt in cl.text(): 
        if "-o" in cl.opt: # limpa a tabela e coloca no ficheiro "clean_table.txt" em frequência por milhão
            clean_table(txt)
        else:
            lista_palavras = tokenize(txt)            
            if "-m" in cl.opt:
                ocorr = Counter(lista_palavras)
                imprimeM(ocorr.most_common(int(cl.opt.get("-m"))))
            elif "-n" in cl.opt:
                lista_palavras.sort()
                ocorr = Counter(lista_palavras)
                imprimeN(ocorr.items())
            elif "-p" in cl.opt: # coloca as palavras em percentagem por milhão no ficheiro "tests/ocorr.txt"
                ocorr = Counter(lista_palavras)
                ocorr = aux(ocorr)
                toFile(ocorr)
            elif "-c" in cl.opt: # compara a percentagem das palavras lidas com a tabela padrão e coloca a diferença no ficheiro "final.txt"
                ocorr = Counter(lista_palavras)
                ocorr = aux(ocorr)
                compare(ocorr)
            else:
                ocorr = Counter(lista_palavras)
                imprimeM(ocorr.items())
