import os
import sqlite3
from tkinter import filedialog,messagebox
import pandas as pd
# Script para gerenciamento de bancos de dados.
# Cada classe deve criar os bancos com base no input ['Spazio','Nominal','MAE','Rollout']

# Nomes dos bancos:
# Spazio.db
# Nominal.db
# MAE.db
# Rollout.db

# Estrutura das pastas:
# .
# ├── Projeto/
# ├── Base/
# ├── data/
# │   ├── Nominal.db
# │   ├── MAE.db
# │   ├── Rollout.db
# │   └── Spazio.db
# ├── models/
# ├── output/
# └── src/
#     ├── app.py
#     ├── database.py
#     └── localizador.py

class BancoDeDados:
    def __init__(self,opcao):
        """Passar os parametros: nominal / spazio / rollout / mae
        Conforme o nome, será criado o banco de dados."""
        self.opcao = str(opcao)
        self.gerenciar_pasta_data()

        if self.opcao:
            self.path_planilha = filedialog.askopenfilename(
                title=f'Selecionar a planilha {self.opcao} para atualizar:',
                filetypes=[("Arquivo Excel", "*.xlsx")]
                )
            
        if self.path_planilha:
            match self.opcao:
                case "nominal":
                    self.criar_db_nominal()
                case 'spazio':
                    self.criar_db_spazio()
                case 'rollout':
                    self.criar_db_rollout()            
                case 'mae':
                    self.criar_db_mae()

    def criar_db_spazio(self):
        """Filtrar colunas por função."""
        nomes = [
                    'SITE_ID',
                    'TIPO_DE_LOGRADOURO',
                    'LOGRADOURO',
                    'NUMERO',
                    'COMPLEMENTO',
                    'BAIRRO',
                    'ESTADO',
                    'CEP',
                    'REGIONAL',
                    'LATITUDE',
                    'LONGITUDE',
                    'TIPO_DA_TORRE',
                    'STATION_ID',
                    'FORNECEDOR_DE_EV',
                    'OBSERVACAO_THQ',
                    'SITUACAO'
                ]
        self.df = pd.read_excel(self.path_planilha,usecols=nomes)
        
        # Criar banco de dados.
        self.criar_db()

    def criar_db_rollout(self):
        pass

    def criar_db_nominal(self):
        pass

    def criar_db_mae(self):
        pass

    def criar_db(self):
        try:
            with sqlite3.connect(f'{self.caminho_db}/{self.opcao}.db') as conn:
                self.df.to_sql(name=self.opcao,con=conn,if_exists='replace',index=False)
                messagebox.showinfo(f'Banco de dados {self.opcao} criado com sucesso !')
        except Exception as e:
            messagebox.showerror(f'Erro ao criar o banco: {e}')

    def gerenciar_pasta_data(self):
        """Verifica/Cria a pasta data para salvar os bancos de dados."""
        caminho_database = os.path.dirname(__file__)
        caminho_database = os.path.dirname(caminho_database) # Sobe uma pasta
        caminho_database = os.path.join(caminho_database,'data') # Procura pasta data

        print( 'caminho:',caminho_database,sep='\n')
        # Verificar se a pasta existe e criar a pasta.
        if not os.path.exists(caminho_database): os.mkdir(caminho_database)
        self.caminho_db = caminho_database
# ---------------
if __name__ == '__main__':
    data = BancoDeDados('spazio')