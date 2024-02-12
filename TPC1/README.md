## Problema
Criar um programa capaz de apresentar o número de ocurrências de cada palavra num ficheiro.
Utilize as bibliotecas *collections* e *jjcli*.

O programa deve ser capaz de:
- -m <numero inteiro> : Mostrar as <numero inteiro> palavras mais comuns.
    - <numero de ocurrências -> palavra>
* -n : Mostrar todas as palavras de forma alfabética, e o seu numero de ocorrêncis.
    * <palavra -> numero de ocurrências>

## Solução
- Criação da função **tokenize** que agrupa e captura palavras individuais, através de uma função regular.

- Criação da função **imprimeN** que recebe e imprime uma lista de tuplos, um tuplo por linha, constituido por uma palavra e o numero de vezes que ocorre, com a palvara primeiro e o número de ocorrências em seguida.

- Criação da função **imprimeM** que recebe e imprime uma lista de tuplos, um tuplo por linha, constituido por uma palavra e o numero de vezes que ocorre, com o número de ocorrências primeiro e a palavra.

> *Counter(lista)* conta o numero de ocurrências de cada objeto na lista e coloca-os num dicionário.
> *abc.most_common(n)* retorna uma lista das n palavras mais comuns em abc.
> *abc.items()* transforma o dicionário *abc* numa lista de pares.

## Comando para apresentar as palavras em ordem alfabética

    python3 word_freq.py -n <file name>

## Comando para apresentar as m palavras mais comuns

    python3 word_freq.py -m <numero de palavras a mostrar> <file name>
