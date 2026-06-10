# Script para gerenciar dados !
# Classe para buscar informações Spazio.db
# Classe para buscar informaçoes MAE.db
# Classe para buscar informaçoes Rollout.db
# Classe para buscar informaçoes Nominal.db

# ---------------
# Classe Spazio
# ---------------

# Salvar colunas a pegar informaçoes da Spazio
# nomes = [
#             'SITE_ID',
#             'TIPO_DE_LOGRADOURO',
#             'LOGRADOURO',
#             'NUMERO',
#             'COMPLEMENTO',
#             'BAIRRO',
#             'ESTADO',
#             'CEP',
#             'REGIONAL',
#             'LATITUDE',
#             'LONGITUDE',
#             'TIPO_DA_TORRE',
#             'STATION_ID',
#             'FORNECEDOR_DE_EV',
#             'OBSERVACAO_THQ',
#             'SITUACAO'
#         ]

import sqlite3
from sqlite3 import Error
import os
class Locate_db:
    """Exportar dados de banco de dados em formato de dicionario.
    [Coluna:Item]"""
    @staticmethod
    def locate_spazio(site_id: str):
        caminho_db = os.path.dirname(__file__)
        caminho_db = os.path.dirname(caminho_db)
        caminho_db = os.path.join(caminho_db,'data','Data.db')

        # Colunas a buscar 
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

        query_names = ",".join(nomes)

        try:
            with sqlite3.connect(caminho_db) as conn:
                query = f"SELECT {query_names} FROM spazio WHERE SITE_ID=?"
                cursor = conn.execute(query,(site_id,))
                sql_result = cursor.fetchall()
                if sql_result:
                    dados_brutos = dict(zip(nomes, sql_result[0]))
                    # Retornar apenas dados não nulos
                    dados_limpos = {k: v for k, v in dados_brutos.items() if v is not None}
                    return dados_limpos
                else:
                    print(f"Aviso: SiteID: {site_id} não localizado.")
                    return None

        except Error as e:
            print(f'Erro ao conectar: {e}')
            return None
if __name__ == '__main__':
    # Chamando e salvando o resultado
    dados = Locate_db.locate_spazio(input("SITE ID:"))

    # Se o resultado existir, você já pode acessar as informações
    if dados:
        print(f"Localizado:")
        for chave,item in dados.items():
            print(f"{chave}: {item}")
