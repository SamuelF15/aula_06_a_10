from etl import filtrar_vendas_maior_1000, ler_csv, somar_valores_venda

path_arquivo = "./DATASETS/vendas.csv"


vendas_itens: list[dict] = ler_csv(path_arquivo)
venda_1000_mais = filtrar_vendas_maior_1000(vendas_itens)
total_venda_1000_mais = somar_valores_venda(venda_1000_mais)
print(f"Valor total: {total_venda_1000_mais}")
