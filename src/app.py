import customtkinter as ctk
import sys
from tkinter import messagebox,filedialog
from database import BancoDeDados

# ============
# Cores usadas
# ============
# cor_adaptavel = ("#EBEBEB", "#1A1C1E") 

# Light: Cinza Gelo (suave) | Dark: Azul Profundo (Nokia/TIM)
cor_adaptavel = ("#DDE1E7", "#111827")
cor_nokia = ("#124191",'#9FA2A7') # Azul oficial Nokia para detalhes
hover_nokia = ("#a4a6aa","#164aa5")
cor_texto_botao = ("white", "#111827")
fonte_h1 = ('Roboto',16,"bold")
fonte_page = ('Roboto',12,"bold")

# ----------------
# Variaveis globais do customtkinter
# ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ----------------
# Funções da Tela
# ----------------

def sair_app():
    """Sair do app finalizando tudo."""
    sys.exit()

# ----------------
# Controle de Paginas do AppRF
# ----------------
class Pag_pesquisa(ctk.CTkFrame):
    """ Pagina de pesquisa conforme caracteristicas de container principal. de AppRF."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ctk.CTkLabel(
            self,
            width=50,
            height=25,
            text="Site ID:",
            font=fonte_h1,
        ).grid(row=0,column=0,padx=5,sticky='ns')
        
        self.entrada_id = ctk.CTkEntry(
            self,
            placeholder_text="-- SITE ID/END ID --",
            width=125,
            height=25,
            border_color=cor_nokia
        )
        self.entrada_id.grid(row=0,column=1,pady=5)

        self.bt_pesquisar = ctk.CTkButton(self,
                        width=100,
                        height=25,
                        font=fonte_page,
                        text="Pesquisar",
                        fg_color=cor_nokia,
                        # command=funcao,
                        hover_color=hover_nokia,
                        text_color=cor_texto_botao)
        self.bt_pesquisar.grid(row=0,column=2,padx=5,sticky='ew')

class Pag_update(ctk.CTkFrame):
    """ Gestão dos itens para criar banco de dados."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        ctk.CTkLabel(self,
            width=50,
            height=25,
            text="Atualizar Banco de dados do App.",
            font=fonte_h1,
        ).pack(pady=10)

        # Container para linhar botoes
        container_botoes = ctk.CTkFrame(self,fg_color="transparent")
        container_botoes.pack(pady=5)
        
        self.bt_att_spazio = ctk.CTkButton(container_botoes,
                        width=100,
                        height=25,
                        font=fonte_page,
                        text="SPAZIO",
                        fg_color=cor_nokia,
                        command=lambda: BancoDeDados('spazio'),
                        hover_color=hover_nokia,
                        text_color=cor_texto_botao)
        self.bt_att_spazio.pack(side='left',padx=5)

        self.bt_att_spazio = ctk.CTkButton(container_botoes,
                        width=100,
                        height=25,
                        font=fonte_page,
                        text="Rollout",
                        fg_color=cor_nokia,
                        # command=funcao,
                        hover_color=hover_nokia,
                        text_color=cor_texto_botao)
        self.bt_att_spazio.pack(side='left',padx=5)

        self.bt_att_spazio = ctk.CTkButton(container_botoes,
                        width=100,
                        height=25,
                        font=fonte_page,
                        text="Nominal",
                        fg_color=cor_nokia,
                        # command=funcao,
                        hover_color=hover_nokia,
                        text_color=cor_texto_botao)
        self.bt_att_spazio.pack(side='left',padx=5)

        self.bt_att_spazio = ctk.CTkButton(container_botoes,
                        width=100,
                        height=25,
                        font=fonte_page,
                        text="MAE",
                        fg_color=cor_nokia,
                        # command=funcao,
                        hover_color=hover_nokia,
                        text_color=cor_texto_botao)
        self.bt_att_spazio.pack(side='left',padx=5)

        ctk.CTkLabel(self,
            width=50,
            height=25,
            text="""Para atualizar o banco de dados.
            Basta clicar no botão com o nome da planilha a ser atualizada.""",
            font=fonte_h1,
        ).pack(pady=10,side='bottom')

# ----------------
# Config. AppRF
# ----------------
class AppRF(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ----------------
        # Config. Janela Principal
        # ----------------

        self.geometry('800x600')
        self.title("NOKIA RF - Tool")

        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        # Variavel de controle de TELA 
        self.frame_atual = None

        # Container principal.
        # As janelas serão exibidas com os parametros dele.
        self.container_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.container_principal.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # ----------------
        # Containers
        # ----------------
        
        # Side Bar
        self.criar_side_bar()
        self.criar_bts_side()

        self.mostrar_pagina()

        # Trocas de temas
        self.criar_tema_switch()

        # criar bototes da 

    # -----------------------
    # Config. Side Bar [FIXO]
    # -----------------------
    def criar_side_bar(self):
        """Criado 2 frames para sobreposição para efeito das bordas apenas no frama inferior."""

        # frame com bordas para adicoinar efeito apenas na parte inferior
        # Para alterar a largura do side BAR
        # Alterar os parametros  "width=" das duas variaveis

        self.sidebar1 = ctk.CTkFrame(self,
                                    width=150,
                                    height=590,
                                    corner_radius=20,
                                    fg_color= cor_adaptavel
                                    )
        self.sidebar1.grid(row=0,column=0,padx=(5,2),sticky="n")

        # Frame principal, onde sera incluido os botoes.
        self.sidebar = ctk.CTkFrame(self,
                                    width=150,
                                    height=570,
                                    corner_radius=0,
                                    fg_color= cor_adaptavel
                                    )
        self.sidebar.grid(row=0,column=0,padx=(5,2),sticky="n")
        self.sidebar.pack_propagate(False) # Impedir o reajuste de tamanho do frame
        
    def mostrar_pagina(self, nome_pagina=None):
            """Troca o conteúdo do container_principal."""
            # Destrir pagina atual.
            if self.frame_atual is not None:
                self.frame_atual.destroy()

            # Decide qual página instanciar
            if nome_pagina == "Pesquisar":
                self.frame_atual = Pag_pesquisa(self.container_principal, fg_color="transparent")
            elif nome_pagina == "Update":
                self.frame_atual = Pag_update(self.container_principal,fg_color="transparent")
            else:
                # Página Home temporária
                self.frame_atual = ctk.CTkFrame(self.container_principal, fg_color="transparent")
                ctk.CTkLabel(self.frame_atual, 
                            text="Bem-vindo à ferramenta RF", 
                            font=fonte_h1).pack(pady=(100, 0), expand=True)
                ctk.CTkLabel(self.frame_atual, 
                            text="Dev.: Mauro Moreira", 
                            font=fonte_page).pack(side='bottom', anchor='e', padx=20, pady=10)

            self.frame_atual.pack(fill="both",padx=2, expand=True)

    def criar_tema_switch(self):
        self.tema_switch = ctk.CTkSwitch(self.sidebar,
                                  width=100,
                                  text="Dark Mode",
                                  progress_color="#124191",
                                  command=self.alterar_tema,
                                  )
        self.tema_switch.pack(pady=1,side="bottom")

        # AppRF iniciado em tema "DARK", iniciar switch setado em dark mode
        self.tema_switch.select()

    def alterar_tema(self):
        """ Ajuste de dark/ligh mode. """
        if self.tema_switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    # Todos os elementos de Side bar aqui
    def criar_bts_side(self):
        """Criar/ajustar todos os elementos de Side Bar atraves desta função."""
        self.menu_label = ctk.CTkLabel(self.sidebar,width=100,height=28,
                            font=fonte_h1,
                            text="MENU"
                            )
        self.menu_label.pack(pady=(5,10))
        
        # Criar botoes dinamicamente com base nos nomes
        mapa_funcoes = {
            "Pesquisar": lambda: self.mostrar_pagina('Pesquisar'),
            "SCI": lambda: self.mostrar_pagina("SCI"),
            "Update" : lambda: self.mostrar_pagina('Update'),
            "Sair": sair_app
        }

        # loop para criar botões com base no mapa_funcoes
        for nome, funcao in mapa_funcoes.items():
            btn = ctk.CTkButton(self.sidebar,
                                        width=100,
                                        height=28,
                                        font=fonte_page,
                                        text=nome,
                                        fg_color=cor_nokia,
                                        command=funcao,
                                        hover_color=hover_nokia,
                                        text_color=cor_texto_botao)
            btn.pack(padx=10, pady=5, fill="x")

 
        pass
app = AppRF()

app.mainloop()