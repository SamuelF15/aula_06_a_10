import glob
import os

import pandas as pd


def extrair_dados_e_consolidar(pasta_parametro: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta_parametro, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


def carregar_dados(df: pd.DataFrame, format_saida: list):
    save_path = "./dados_gerados"
    os.makedirs(save_path, exist_ok=True)
    for formato in format_saida:
        if formato == "csv":
            df.to_csv(f"{save_path}/dados.csv")
        if formato == "parquet":
            df.to_parquet(f"{save_path}/dados.parquet")


def pipeline_calcular_kpi_de_venda_consolidada(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    dataframe_calculado = calcular_kpi_total_de_vendas(data_frame)
    carregar_dados(dataframe_calculado, formato_de_saida)
