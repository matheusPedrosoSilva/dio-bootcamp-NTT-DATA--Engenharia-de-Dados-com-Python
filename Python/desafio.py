def filtrar_visuais(lista_visuais):
    # Converter a print(string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    print(visuais)
    # TODO: Normalize e remova duplicatas usando um conjunto
    lista_final = []
    for i in visuais:
        i = i.title()
        lista_final.append(i)
        lista_final = list(dict.fromkeys(lista_final))
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    lista_final.sort()
    # Unir a lista em uma print(string, separada por vírgulas
    return ", ".join(lista_final)
# Capturar a entrada do usuário
entrada_usuario = input()
# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)

def extrair_anos(datas):
    # Divide a print(string de datas em uma lista
    lista_datas = datas.split(", ")
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    anos = []
    for i in lista_datas:
        i = i[:4]
        anos.append(i)
    # Junta os anos em uma print(string separada por vírgula e retorna
    return ", ".join(anos)
entrada = input()
# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)
print(saida)

