from etl import pipeline_calcular_kpi_de_venda_consolidada

pasta_argumento: str = "data"
formato_de_saida: list = ["csv", "parquet"]

pipeline_calcular_kpi_de_venda_consolidada("data", formato_de_saida)
