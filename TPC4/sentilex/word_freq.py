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
import sys
import re


#bonitos,bonito.PoS=Adj;FLEX=mp;TG=HUM:N0;POL:N0=1;ANOT=MAN
#engoliste em seco,engolir em seco.PoS=IDIOM;Flex=J2p|J2s;TG=HUM:N0;POL:N0=-1;ANOT=MAN
#engolistes em seco,engolir em seco.PoS=IDIOM;Flex=J2p;TG=HUM:N0;POL:N0=-1;ANOT=MAN


def tokenize(texto):
    er = re.compile(r'POL:.+=(-?\d+)') #expressão regular para encontrar a polaridade
    with open('result.txt', 'w') as f:

        file = open(texto, 'r')
        lines = file.readlines()
        for line in lines:
            pp = line.split(".")
            words = pp[0].split(",")
            pol = er.search(pp[1]).group(1)
            for word in words:
                if pol == "1":
                    f.write(f"{word}:POSITIVE\n")
                elif pol == "-1":
                    f.write(f"{word}:NEGATIVE\n")
                elif pol == "0":
                    f.write(f"{word}:NEUTRAL\n")
                else:
                    f.write(f"{word}:UNKNOWN\n")
    f.close()
    

tokenize('files/SentiLex-flex-PT02.txt')


    

