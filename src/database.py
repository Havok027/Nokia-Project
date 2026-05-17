import os
import sqlite3
from tkinter import filedialog, messagebox
import pandas as pd

# Script para gerenciamento de bancos de dados.
# Estrutura das pastas:
# .
# ├── Projeto/
# ├── Base/
# ├── data/
# │   └── Data.db
# ├── models/
# ├── output/
# └── src/
#     ├── app.py
#     ├── database.py
#     └── localizador.py

class BancoDeDados:
    def __init__(self, opcao):
        """Passar os parametros: nominal / spazio / rollout / mae
        Conforme o nome, será atualizada a tabela respectiva no Data.db."""
        self.opcao = str(opcao).lower()
        self.gerenciar_pasta_data()
        self.path_planilha = None

        # Define a extensão esperada baseado no tipo de arquivo informado
        file_types = [("Arquivo CSV", "*.csv")] if self.opcao == 'mae' else [("Arquivo Excel", "*.xlsx")]

        if self.opcao:
            self.path_planilha = filedialog.askopenfilename(
                title=f'Selecionar o arquivo para {self.opcao.upper()}:',
                filetypes=file_types
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
        """Filtrar colunas por função para SPAZIO."""
        nomes = [
            'SITE_ID', 'TIPO_DE_LOGRADOURO', 'LOGRADOURO', 'NUMERO', 
            'COMPLEMENTO', 'BAIRRO', 'ESTADO', 'CEP', 'REGIONAL', 
            'LATITUDE', 'LONGITUDE', 'TIPO_DA_TORRE', 'STATION_ID', 
            'FORNECEDOR_DE_EV', 'OBSERVACAO_THQ', 'SITUACAO'
        ]
        # Carrega apenas as colunas necessárias
        self.df = pd.read_excel(self.path_planilha, usecols=nomes)
        
        # Criar/Salvar na tabela SPAZIO
        self.salvar_no_banco(nome_tabela='SPAZIO')

    def criar_db_rollout(self):
        """Carrega a planilha TIM_ROLLOUT.xlsx (Ajuste o usecols se necessário)"""
        # Se quiser filtrar colunas específicas depois, basta criar a lista 'nomes' igual no spazio
        self.df = pd.read_excel(self.path_planilha)
        
        # Criar/Salvar na tabela ROLLOUT
        self.salvar_no_banco(nome_tabela='ROLLOUT')

    def criar_db_nominal(self):
        """Carrega a planilha NMOMINAL_PLAN.xlsx (Ajuste o usecols se necessário)"""
        self.df = pd.read_excel(self.path_planilha)
        
        # Criar/Salvar na tabela PLANO_NOMINAL
        self.salvar_no_banco(nome_tabela='PLANO_NOMINAL')

    def criar_db_mae(self):
            """Carrega o arquivo CSV MAE_NOKIA.csv testando encodings comuns."""
            # Lista de encodings comuns para arquivos gerados no Windows/Excel brasileiro
            encodings_para_testar = ['iso-8859-1', 'cp1252', 'utf-8']
            
            for enc in encodings_para_testar:
                try:
                    print(f"Tentando ler o CSV com o encoding: {enc}...")
                    self.df = pd.read_csv(self.path_planilha, sep=';', encoding=enc)
                    print(f"Sucesso ao ler com {enc}!")
                    break  # Se funcionou, sai do loop
                except UnicodeDecodeError:
                    continue  # Se deu erro, tenta o próximo da lista
            else:
                # Se sair do loop sem dar 'break', significa que nenhum funcionou
                raise Exception("Não foi possível ler o arquivo CSV com nenhum dos encodings conhecidos.")

            # Criar/Salvar na tabela MAE
            self.salvar_no_banco(nome_tabela='MAE')

    def salvar_no_banco(self, nome_tabela):
        """Salva o DataFrame na tabela correspondente dentro do arquivo Data.db"""
        try:
            # Centralizado no banco único Data.db dentro da pasta data
            caminho_final_db = os.path.join(self.caminho_db, 'Data.db')
            
            with sqlite3.connect(caminho_final_db) as conn:
                self.df.to_sql(name=nome_tabela, con=conn, if_exists='replace', index=False)
                messagebox.showinfo(
                    title="ATENÇÃO:",
                    message=f'Tabela "{nome_tabela}" criada/atualizada com sucesso no Data.db!'
                )
        except Exception as e:
            messagebox.showerror(title="Erro", message=f'Erro ao salvar no banco: {e}')

    def gerenciar_pasta_data(self):
        """Verifica/Cria a pasta data para salvar os bancos de dados."""
        caminho_database = os.path.dirname(__file__)
        caminho_database = os.path.dirname(caminho_database) # Sobe uma pasta
        caminho_database = os.path.join(caminho_database, 'data') # Procura pasta data

        print('Caminho do banco de dados:', caminho_database, sep='\n')
        # Verificar se a pasta existe e criar a pasta.
        if not os.path.exists(caminho_database): 
            os.makedirs(caminho_database)
        self.caminho_db = caminho_database

# ---------------
if __name__ == '__main__':
    # Modifique o parâmetro para testar cada um: 'spazio', 'nominal', 'rollout' ou 'mae'
    data = BancoDeDados('spazio')