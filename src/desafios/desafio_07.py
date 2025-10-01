import csv

caminho_arquivo = "./data/vendas.csv"


def ler_csv(caminho_arquivo: str) -> list[dict]:
    lista = []
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for produto in leitor:
            lista.append(produto)
    return lista


def processar_dados(lista: list[dict]) -> dict[str, list[dict]]:
    lista_filtrada = {}
    for item in lista:
        lista_filtrada[item.get("Categoria")] = lista_filtrada.get(
            item.get("Categoria"), []
        ) + [item]
    return lista_filtrada


def calcular_vendas_categoria(
    lista_filtrada: dict[str, list[dict]]
) -> dict[str, float]:
    totais_por_categoria = {}
    for categoria, vendas in lista_filtrada.items():
        total_categoria = 0
        for venda in vendas:
            total_categoria += float(venda.get("Venda")) * int(venda.get("Quantidade"))
        totais_por_categoria[categoria] = round(total_categoria, 2)
    return totais_por_categoria


venda_por_categoria = calcular_vendas_categoria(
    processar_dados(ler_csv(caminho_arquivo))
)
print(venda_por_categoria)
