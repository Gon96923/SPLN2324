# Problema

1)Procurar uma tabela de frequências de portugues
2)Limpeza (das palavras menos frequentes,numeros,palavras sem numeros, letras sozinhas)
3)Formula capaz de comparar casos(numero de ocurrencias por milhão)

# Solução

word_freq [options] input_files
options: 
- m 20 : Show 20 most common
- n : Order alfabetically
- o : Clean the table, oder it by frequency and put in "tests/clean_table.txt" (word_freq -o tests/toralpt.txt)
- p : Oder by frequency and put in "tests/ocorr.txt" (word_freq -p tests/Camilo-Amor_de_Perdicao.md)
- c : Compare the frequency with the table previously created and put the difference in "tests/final.txt" (word_freq -c tests/Camilo-Amor_de_Perdicao.md)
