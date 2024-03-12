file = open("Linguakit.txt","r")
data = file.readlines()

informacoes = {}

for linha in data[8:]:
    partes = linha.split()
    if len(partes) >= 3:
        palavra = partes[0].replace('_',' ')
        polaridade = partes[1]
        valor = float(partes[2])
        if palavra in informacoes:
            if informacoes[palavra][1] < valor:
                informacoes[palavra] = (polaridade,valor)
        else:
            informacoes[palavra] = (polaridade,valor)

for info in informacoes:
    if informacoes[info][1] < 0.002:
        informacoes[info] = ("NEUTRAL", informacoes[info][1])
        
categoria = open("Linguakit_categoria.txt", "w")
for palavra, (polaridade, valor) in informacoes.items():
    categoria.write(f"{palavra}:{polaridade}\n")

# Criar e escrever no arquivo de saída para valores
valores = open("Linguakit_number.txt", "w")
for palavra, (polaridade, valor) in informacoes.items():
    valores.write(f"{palavra}:{valor}\n")


