import pandas as pd
import os

# 1. Exportar informações
# 2. Criar um menu interativo para exibir as informações tratadas de forma simplificada ao usuario.
# 3. Exportar estas informações após usuario conferir para TSSR.
# 4. Criar interface no windows e executar como .exe

# ------------------------------------------------------
# MAURO:
# 1. Criar sistema que verifica liçensa online.
# Para atribuir a ferramenta apenas para assinantes.
# Criar uma maneira simplificada para renovar o pacote, sera vendido mensal.

# ------------------------------------------------------
# Definição de Funções e Classes:
# ------------------------------------------------------
class Menu:
    def __init__(self, titulo_padrao):
        self.titulo = titulo_padrao

    def exibir_cabecalho(self, novo_titulo=None):
        # Limpa o terminal e exibe o título estilizado
        os.system('cls' if os.name == 'nt' else 'clear')
        texto = novo_titulo if novo_titulo else self.titulo
        borda = "*" * (len(texto) + 4)
        print(f"{borda}")
        print(f"* {texto} *")
        print(f"{borda}\n")

    def mostrar_opcoes(self, lista, titulo_tela=None):
        self.exibir_cabecalho(titulo_tela)
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")
        print("0 - Sair")

class Spazio:
    def __init__(self,df_spazio):
        # Passar df da spazio para manter salvo na memoria
        self.df_spazio = df_spazio

        # Lista das colunas da SPAZIO.
        # Ajustar aqui se precisar mudar as colunas exibidas.
        self.colunas = [
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

    def spazio_info(self, site_name):
        # 1. Filtra a linha
        df_filtro = self.df_spazio[self.df_spazio['SITE_ID'].astype(str) == str(site_name)]

        # 2. Se não encontrou nada, retorna o df vazio direto para evitar erros
        if df_filtro.empty:
            return df_filtro

        # 3. Retorna apenas as colunas da sua lista que NÃO estão vazias
        return df_filtro[self.colunas].dropna(axis=1, how='all')


# ------------------------------------------------------
# Configurações de Dados:
# ------------------------------------------------------
# Define o caminho relativo ao arquivo .py
caminho_file = os.path.dirname(os.path.abspath(__file__))

# Carrega o DataFrame (ajuste o caminho se necessário)
try:
    # Carregar arquivo com python calamine, mais rapido para carregar.
    df_spazio = pd.read_excel(os.path.join(caminho_file, "database", "SPAZIO_NOKIA.xlsx"),engine="calamine") # Carregar data frame Spazio NOKIA, indica o caminho relativo ao main.py
except Exception as e:
    print(f"ERRO REAL: {type(e).__name__} - {e}") # Isso vai imprimir o nome do erro (ex: FileNotFoundError)
    df_spazio = pd.DataFrame()

# ------------------------------------------------------
# Instanciação e Loop Principal:
# ------------------------------------------------------
main_menu = Menu("MENU PRINCIPAL")
app_spazio = Spazio(df_spazio)

while True:
    opcoes = ['Buscar Site ID', 'Teste de Conexão']
    main_menu.mostrar_opcoes(opcoes) 
    
    selecao = input("\nEscolha uma opção: ").strip()

    match selecao:
        case "1":
            site_id_pesquisa = input('\nInserir o SITE ID a pesquisar: ').strip()
            
            try:
                # Realiza a busca através da classe
                df_info_site = app_spazio.spazio_info(site_id_pesquisa)
                 
                main_menu.exibir_cabecalho("RESULTADO DA BUSCA")
                
                if not df_info_site.empty:
                    print("Informações encontradas na Spazio:")
                    # Criamos uma lista de nomes: ['SITE 1', 'SITE 2', ...] baseada na quantidade de linhas
                    novos_nomes = [f"SITE {i}" for i in range(1, len(df_info_site) + 1)]

                    df_info_site.index = novos_nomes
                    
                    # O display.to_string() ajuda a não cortar colunas no print
                    #print(df_info_site.to_string(index=False))
                    print(df_info_site.T)

                    # Caso encontre mais de 1 site.
                    if len(novos_nomes)>1:
                        print(f"\nEncontrado: {len(novos_nomes)} sites. \nEscolha qual site devo considerar:")
                        for i,item in enumerate(novos_nomes,start=1):
                            print(f"{i} - {df_info_site.iloc[i-1]['SITE_ID']}")

                        # Adicionar critica de dados para sempre ser INT de 1 ate a quantidade de item.
                        while True:
                            try:
                                escolha = int(input('\nInseri o numero correspondente a opção desejada:'))
                                if 0 < escolha < len(novos_nomes)+1: 
                                    print('Opção Invalida')
                                    break
                            except:
                                print('Escolher uma opção valida.')
                        
                        main_menu.exibir_cabecalho("RESULTADO DA BUSCA")
                        print("Informações encontradas na Spazio:")
                        df_info_site = df_info_site.iloc[escolha-1]
                        print(df_info_site.T)
                    
                    input("\nPressione ENTER para voltar ao menu...")  
                else:
                    print(f'O SITE ID "{site_id_pesquisa}" não foi encontrado na base.')

            except Exception as e:
                print(f'Ocorreu um erro na pesquisa: {e}')
                input("Pressione ENTER para continuar...")

        case "2":
            main_menu.exibir_cabecalho("TESTE DE CONEXÃO")
            print("Funcionalidade em desenvolvimento...")
            input("\nPressione ENTER para voltar...")

        case "0":
            print('Saindo do sistema...')
            break
            
        case _:
            print("\nOpção inválida! Tente novamente.")
            input("Pressione ENTER...")