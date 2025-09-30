# Adicionamos o parâmetro 'nivel' para ajudar na visualização
def buscar_caminho(grafo, vertice_atual, caminho, num_total_vertices, nivel):
    indent = "  " * nivel
    print(
        f"{indent}🔎 Tentando a partir de '{vertice_atual}', caminho atual: {caminho}"
    )

    if len(caminho) == num_total_vertices:
        print(f"{indent}✅ SOLUÇÃO ENCONTRADA: {caminho}")
        return caminho

    for vizinho in grafo[vertice_atual]:
        if vizinho not in caminho:
            print(f"{indent}  -> Explorando vizinho '{vizinho}'...")
            resultado = buscar_caminho(
                grafo,
                vizinho,
                caminho + [vizinho],
                num_total_vertices,
                nivel + 1,
            )

            if resultado is not None:
                return resultado

    print(f"{indent}❌ Beco sem saída em '{vertice_atual}'. Retrocedendo...")
    return None


def encontrar_caminho_hamiltoniano(grafo):
    num_vertices = len(grafo)
    """Usar o loop for facilita e tira o trabalho
    de você mesmo escolher o vértice inicial.
    Porém, para tornar a apresentação mais interativa,
    vamos pedir para o usuário escolher o vértice inicial."""
    # for vertice_inicial in grafo:
    # print(f"\n{'='*20}\nINICIANDO BUSCA A PARTIR DE '{vertice_inicial}'\n{'='*20}")
    # solucao = buscar_caminho(grafo, vertice_inicial, caminho_inicial, num_vertices, 0)
    # if solucao:
    # return solucao
    vertice_inicial = input(
        f"Escolha o vertice que você deseja explorar: {list(grafo.keys())}: "
    )
    caminho_inicial = [vertice_inicial]
    solucao = buscar_caminho(grafo, vertice_inicial, caminho_inicial, num_vertices, 0)
    if solucao:
        return solucao
    return None


# Grafo usado no exemplo
grafo_com_caminho = {
    "A": ["B", "C"],
    "B": ["A", "D", "C"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"],
}

resultado = encontrar_caminho_hamiltoniano(grafo_com_caminho)

if resultado:
    print(f"\n🎉 Resultado final: {' -> '.join(resultado)}")
else:
    print("\n🤷‍ Resultado final: Nenhum caminho encontrado.")
