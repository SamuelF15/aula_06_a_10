import csv


def ler_csv(caminho_arquivo: str) -> list[dict]:
    lista = []
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_vendas_maior_1000(lista: list[dict]) -> list[dict]:
    lista_filtrada = []
    for venda in lista:
        if float(venda.get("Venda")) > 1000:
            lista_filtrada.append(venda)
    return lista_filtrada


def somar_valores_venda(lista_com_vendas_filtradas: list[dict]) -> int:
    total = 0
    for valor in lista_com_vendas_filtradas:
        total += float(valor.get("Venda"))
    return total
