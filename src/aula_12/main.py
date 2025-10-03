import pandas as pd


class CsvProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_csv(self):
        if self.df is None:
            self.df = pd.read_csv(self.file_path)
            return self.df

    def filter_column(self, column, value):
        if self.df is not None:
            self.new_df = self.df[self.df[column] == value]
            return self.new_df
        else:
            raise ValueError("DataFrame is not loaded. Please Load the CSV first.")


arquivo_csv = CsvProcessor("./src/aula_12/exemplo.csv")
arquivo_csv.load_csv()

arquivo_csv_SP = arquivo_csv.filter_column("estado", "SP")
print(arquivo_csv_SP)
print(arquivo_csv.df)
