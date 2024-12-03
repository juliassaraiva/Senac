import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

#CLASSE LOCKER
class Locker:
    def __init__(self, locker_id, locker_ocupado=False, locker_usuario=None, locker_tipo=None):
        self.__locker_id = locker_id
        self.__is_ocupado = locker_ocupado
        self.__usuario_id = locker_usuario
        self.__tipo_usuario = locker_tipo

    def associar_usuario(self, usuario_id, usuario_tipo):
        if not self.__is_ocupado:
            self.__is_ocupado = True
            self.__usuario_id = usuario_id
            self.__tipo_usuario = usuario_tipo
            return True
        return False

    def liberar_usuario(self):
        if self.__is_ocupado:
            self.__is_ocupado = False
            self.__usuario_id = None
            self.__tipo_usuario = None
            return True
        return False

    def get_id_locker(self):
        return self.__locker_id

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def get_ocupado(self):
        return self.__is_ocupado
    
#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def get_id_usuario(self):
        return self.__usuario_id

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def get_tipo_usuario(self):
        return self.__tipo_usuario

    def get_status(self):
        return self.__is_ocupado, self.__usuario_id, self.__tipo_usuario

#CLASSE USUÁRIO
class Usuario:
    def __init__(self, usuario_id, nome):
        self.__usuario_id = usuario_id
        self.__nome = nome
        self.__tipo = "Usuario"

    def get_id_usuario(self):
        return self.__usuario_id

    def get_nome(self):
        return self.__nome
    
    def get_tipo(self):
        return self.__tipo

    def get_status(self):
        return self.__usuario_id, self.__nome, self.__tipo

#CLASSE SISTEMA LOCKER
class SistemaLocker:
    def __init__(self):
        self.__lockers = {}
        self.__usuarios = {}
        self.__moradores = {}
        self.__entregadores = {}
        self.__locker_arquivo = 'lockers.txt'
        self.carregar_lockers()

#AJUSTEI CONFORME CÓDIGO ORIGINAL
    def adicionar_locker(self, locker_id):
        if locker_id not in self.__lockers:
            self.__lockers[locker_id] = Locker(locker_id)
            self.salvar_locker(self.__lockers[locker_id])
            return True
        return False

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def get_lockers(self):
        return self.__lockers

    def libera_locker(self, locker_id):
        if locker_id in self.__lockers:
            return self.__lockers[locker_id].liberar_usuario()
        return False

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def excluir_locker(self, locker_id):
        if locker_id in self.__lockers:
            del self.__lockers[locker_id]
            self.salvar_dados(self.__locker_arquivo)
            return True
        return False

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def existe_locker(self, id_locker):
        return id_locker in self.__lockers

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def is_locker_livre(self, locker_id):
        return locker_id in self.__lockers and not self.__lockers[locker_id].get_ocupado()

    def associar_locker_ao_usuario(self, locker_id, usuario_id, usuario_tipo):
        if locker_id in self.__lockers:
            if (usuario_id in self.__usuarios or self.__moradores or self.__entregadores):
                return self.__lockers[locker_id].associar_usuario(usuario_id, usuario_tipo)
        return False

#INCLUI PARA FICAR COMO O CÓDIGO ORIGINAL A OPÇÃO ACIMA ESTAVA NO CÓDIGO DA INTERFACE E FUNCIONA. DECIDIR QUAL MANTER
    def get_locker_status(self, locker_id):
        if locker_id in self.__lockers:
            return self.__lockers[locker_id].get_status()
        return None, None, None

#NÃO ESTÁ EXATAMENTE ASSIM NO CÓDIGO ORIGINAL, MAS COMO ESTÁ MAIS COMPLETO, MANTIVE
    def salvar_locker(self, locker):
        with open(self.__locker_arquivo, 'a') as arquivo:
            arquivo.write(
                f'{locker.get_id_locker()},{locker.get_ocupado()},{locker.get_id_usuario()},{locker.get_tipo_usuario()}\n'
            )

#NÃO ESTÁ EXATAMENTE ASSIM NO CÓDIGO ORIGINAL, MAS COMO ESTÁ MAIS COMPLETO, MANTIVE
    def carregar_lockers(self):
        try:
            with open(self.__locker_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    locker_id, locker_ocupado, locker_usuario, locker_tipo = linha.strip().split(',')
                    self.__lockers[locker_id] = Locker(locker_id, locker_ocupado == 'True', locker_usuario, locker_tipo)
        except FileNotFoundError:
            pass

    def adicionar_usuario(self, usuario_id, nome):
        if usuario_id not in self.__usuarios:
            self.__usuarios[usuario_id] = Usuario(usuario_id, nome)
            return True
        return False

#INCLUSÃO DEVIDO HERANÇA
    def adicionar_morador(self, usuario_id, nome, apartamento):
        if usuario_id not in self.__moradores:
            self.__moradores[usuario_id] = Morador(usuario_id, nome, apartamento)
            return True
        return False

#INCLUSÃO DEVIDO HERANÇA
    def adicionar_entregador(self, usuario_id, nome, empresa):
        if usuario_id not in self.__entregadores:
            self.__entregadores[usuario_id] = Entregador(usuario_id, nome, empresa)
            return True
        return False    

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def excluir_usuario(self, usuario_id):
        if usuario_id in self.__usuarios:
            del self.__usuarios[usuario_id]
            return True
        return False

#INCLUSÃO DEVIDO HERANÇA
    def excluir_morador(self, usuario_id):
        if usuario_id in self.__moradores:
            del self.__moradores[usuario_id]
            return True
        return False

#INCLUSÃO DEVIDO HERANÇA
    def excluir_entregador(self, usuario_id):
        if usuario_id in self.__entregadores:
            del self.__entregadores[usuario_id]
            return True
        return False    

#NÃO ESTAVA NO CÓDIGO ORIGINAL
    def get_usuarios(self):
        return self.__usuarios

#INCLUSÃO DEVIDO HERANÇA
    def get_moradores(self):
        return self.__moradores

#INCLUSÃO DEVIDO HERANÇA
    def get_entregadores(self):
        return self.__entregadores

#INCLUI PARA FICAR COMO O CÓDIGO ORIGINAL A OPÇÃO ACIMA ESTAVA NO CÓDIGO DA INTERFACE E FUNCIONA. DECIDIR QUAL MANTER
    def salvar_dados(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for locker_id, locker in self.__lockers.items():
                is_ocupado, usuario_id, usuario_tipo = locker.get_status()
                arquivo.write(f'{locker_id},{is_ocupado},{usuario_id},{usuario_tipo} \n')

    def carregar_dados(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    locker_id, is_ocupado, usuario_id, usuario_tipo = linha.strip().split(',')
                    self.adicionar_locker(locker_id)
                    if is_ocupado == 'True':
                        self.associar_locker_ao_usuario(locker_id, usuario_id, usuario_tipo)
        except FileNotFoundError:
            pass

#NÃO ESTAVA NO CÓDIGO ORIGINAL >> posteriormente inclui os 'ORs'
    def usuario_cadastrado(self, usuario_id):
        return usuario_id in self.__usuarios or self.__moradores or self.__entregadores

#NÃO ESTAVA NO CÓDIGO ORIGINAL >> posteriormente inclui os 'ORs'
    def get_usuario(self, usuario_id, usuario_tipo):
        if usuario_tipo == "Usuario":
            usuario = self.__usuarios[usuario_id].get_nome()
        if usuario_tipo == "Morador":
            usuario = self.__moradores[usuario_id].get_nome()
        if usuario_tipo == "Entregador":
            usuario = self.__entregadores[usuario_id].get_nome()
        return usuario

#INCLUSÃO DEVIDO HERANÇA
    def morador_cadastrado(self, usuario_id):
        return usuario_id in self.__moradores

#INCLUSÃO DEVIDO HERANÇA
    def get_morador_unico(self, usuario_id):
        return self.__moradores[usuario_id].get_nome()

#INCLUSÃO DEVIDO HERANÇA
    def entregador_cadastrado(self, usuario_id):
        return usuario_id in self.__entregadores

#INCLUSÃO DEVIDO HERANÇA
    def get_entregador_unico(self, usuario_id):
        return self.__entregadores[usuario_id].get_nome()

#CLASSE APP
class App:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Lockers")
        self.sistema = SistemaLocker()

        # Menu
        menubar = tk.Menu(janela)
        janela.config(menu=menubar)

        # Menu de Opções
        menu_opcoes = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opções", menu=menu_opcoes)
        menu_opcoes.add_command(label="Adicionar Locker", command=self.adicionar_lock)
        menu_opcoes.add_command(label="Excluir Locker", command=self.excluir_lock)
        menu_opcoes.add_command(label="Adicionar Usuário", command=self.adicionar_usuario)
        menu_opcoes.add_command(label="Excluir Usuário", command=self.excluir_usuario)
        menu_opcoes.add_command(label="Adicionar Morador", command=self.adicionar_morador)
        menu_opcoes.add_command(label="Excluir Morador", command=self.excluir_morador)
        menu_opcoes.add_command(label="Adicionar Entregador", command=self.adicionar_entregador)
        menu_opcoes.add_command(label="Excluir Entregador", command=self.excluir_entregador)
        menu_opcoes.add_command(label="Atribuir Locker a Usuário", command=self.atribuir_locker_usuario)
        menu_opcoes.add_command(label="Liberar Locker", command=self.liberar_locker)
        menu_opcoes.add_command(label="Verificar Status do Locker", command=self.verificar_status_locker)
        menu_opcoes.add_command(label="Salvar Dados", command=self.salvar_dados)
        menu_opcoes.add_command(label="Carregar Dados", command=self.carregar_dados)
        menu_opcoes.add_separator()
        menu_opcoes.add_command(label="Sair", command=janela.quit)

        # Frame para exibir lockers
        self.frame_lockers = tk.Frame(janela, highlightbackground="orange", highlightthickness=2)
        self.frame_lockers.pack(fill=tk.BOTH, expand=True)

        # Treeview para exibir os lockers
        self.tree_lockers = ttk.Treeview(self.frame_lockers, columns=("ID", "Status", "Usuário"), show="headings")
        self.tree_lockers.heading("ID", text="ID")
        self.tree_lockers.heading("Status", text="Status")
        self.tree_lockers.heading("Usuário", text="Usuário")
        self.tree_lockers.pack(fill=tk.BOTH, expand=True)

        # Frame para exibir usuarios
        self.frame_usuarios = tk.Frame(janela, highlightbackground="blue", highlightthickness=2)
        # self.frame_usuarios.pack(fill=tk.BOTH, expand=True)

        #INCLUSÃO DEVIDO HERANÇA
        # Frame para exibir moradores
        self.frame_moradores = tk.Frame(janela, highlightbackground="pink", highlightthickness=2)
        # self.frame_moradores.pack(fill=tk.BOTH, expand=True)

        #INCLUSÃO DEVIDO HERANÇA
        # Frame para exibir entregadores
        self.frame_entregadores = tk.Frame(janela, highlightbackground="green", highlightthickness=2)
        # self.frame_entregadores.pack(fill=tk.BOTH, expand=True)

        # Treeview para exibir os usuarios
        self.treeusuarios = ttk.Treeview(self.frame_usuarios, columns=("ID", "Nome"), show="headings")
        self.treeusuarios.heading("ID", text="ID")
        self.treeusuarios.heading("Nome", text="Nome")
        self.treeusuarios.pack(fill=tk.BOTH, expand=True)
        self.atualizar_lockers()

        #INCLUSÃO DEVIDO HERANÇA
        # Treeview para exibir os moradores
        self.treemoradores = ttk.Treeview(self.frame_moradores, columns=("ID", "Nome", "Apartamento"), show="headings")
        self.treemoradores.heading("ID", text="ID")
        self.treemoradores.heading("Nome", text="Nome")
        self.treemoradores.heading("Apartamento", text="Apartamento")
        self.treemoradores.pack(fill=tk.BOTH, expand=True)
        self.atualizar_lockers()

        #INCLUSÃO DEVIDO HERANÇA
        # Treeview para exibir os entregadores
        self.treeentregadores = ttk.Treeview(self.frame_entregadores, columns=("ID", "Nome", "Empresa"), show="headings")
        self.treeentregadores.heading("ID", text="ID")
        self.treeentregadores.heading("Nome", text="Nome")
        self.treeentregadores.heading("Empresa", text="Empresa")
        self.treeentregadores.pack(fill=tk.BOTH, expand=True)
        self.atualizar_lockers()
        
    def atualizar_lockers(self):
        for row in self.tree_lockers.get_children():
            self.tree_lockers.delete(row)

        lockers = self.sistema.get_lockers()

        # Debug print para verificar os lockers retornados
        #print("Lockers encontrados:", lockers)  # Para diagnóstico
    
        if lockers is not None and len(lockers) > 0:
            for locker_id, locker in lockers.items():
                #print("Inserindo lockers na TreeView:")  # Debug adicional
                status = "Ocupado" if locker.get_ocupado() else "Livre"
                usuario = locker.get_id_usuario() if locker.get_ocupado() else "N/A"
                #print(f"Inserindo locker: ID={locker_id}, Status={status}, Usuario={usuario}")  # Debug adicional
                self.tree_lockers.insert("", "end", values=(locker_id, status, usuario))
        else:
            #print("Nenhum locker encontrado para exibir")  # Debug adicional
            self.tree_lockers.insert("", "end", values=("Nenhum locker cadastrado", "", ""))

    def adicionar_lock(self):
        locker_id = self.get_input("Digite o ID do Locker:")
        if locker_id and not self.sistema.existe_locker(locker_id):
            self.sistema.adicionar_locker(locker_id)
            messagebox.showinfo("Sucesso", f"Locker {locker_id} adicionado com sucesso.")
            self.atualizar_lockers()
        else:
            messagebox.showerror("Erro", "Locker já existe ou ID inválido.")

    def excluir_lock(self):
        locker_id = self.get_input("Digite o ID do Locker a ser excluído:")
        if locker_id and self.sistema.excluir_locker(locker_id):
            messagebox.showinfo("Sucesso", f"Locker {locker_id} excluído com sucesso.")
            self.atualizar_lockers()
        else:
            messagebox.showerror("Erro", "Locker não encontrado ou ID inválido.")

    def adicionar_usuario(self):
        # Mostra o frame
        self.frame_usuarios.pack(fill=tk.BOTH, expand=True)

        # self.atualizar_usuarios()
        usuario_id = self.get_input("Digite o ID do Usuário:")
        nome = self.get_input("Digite o Nome do Usuário:")
        if usuario_id and nome and self.sistema.adicionar_usuario(usuario_id, nome):
            self.atualizar_usuarios()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso.")
        else:
            messagebox.showerror("Erro", "ID já existe ou dados inválidos.")

        ######self.frame_usuarios.pack_forget()  # Esconde o Frame

    def atualizar_usuarios(self):
        for row in self.treeusuarios.get_children():
            self.treeusuarios.delete(row)

        usuarios = self.sistema.get_usuarios()
        for usuario in usuarios.values():
            self.treeusuarios.insert("", "end", values=(usuario.get_id_usuario(), usuario.get_nome()))
       
    def excluir_usuario(self):
        usuario_id = self.get_input("Digite o ID do Usuário a ser excluído:")
        if usuario_id and self.sistema.excluir_usuario(usuario_id):
            self.atualizar_usuarios()
            messagebox.showinfo("Sucesso", f"Usuário {usuario_id} excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado ou ID inválido.")

#INCLUSÃO DEVIDO HERANÇA
    def adicionar_morador(self):
        # Mostra o frame
        self.frame_moradores.pack(fill=tk.BOTH, expand=True)

        # self.atualizar_moradores()
        usuario_id = self.get_input("Digite o ID do Morador:")
        nome = self.get_input("Digite o Nome do Morador:")
        apartamento = self.get_input("Digite o Apartamento do Morador:")
        if usuario_id and nome and apartamento and self.sistema.adicionar_morador(usuario_id, nome, apartamento):
            self.atualizar_moradores()
            messagebox.showinfo("Sucesso", "Morador adicionado com sucesso.")
        else:
            messagebox.showerror("Erro", "ID já existe ou dados inválidos.")

        #####self.frame_moradores.pack_forget()  # Esconde o Frame

    def atualizar_moradores(self):
        for row in self.treemoradores.get_children():
            self.treemoradores.delete(row)

        moradores = self.sistema.get_moradores()
        for morador in moradores.values():
            self.treemoradores.insert("", "end", values=(morador.get_id_usuario(), morador.get_nome(), morador.get_apartamento()))
                                     
    def excluir_morador(self):
        usuario_id = self.get_input("Digite o ID do Morador a ser excluído:")
        if usuario_id and self.sistema.excluir_morador(usuario_id):
            self.atualizar_moradores()
            messagebox.showinfo("Sucesso", f"Morador {usuario_id} excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Morador não encontrado ou ID inválido.")
           
#INCLUSÃO DEVIDO HERANÇA
    def adicionar_entregador(self):
        # Mostra o frame
        self.frame_entregadores.pack(fill=tk.BOTH, expand=True)

        # self.atualizar_entregadores()
        usuario_id = self.get_input("Digite o ID do Entregador:")
        nome = self.get_input("Digite o Nome do Entregador:")
        empresa = self.get_input("Digite a Empresa do Entregador:")
        if usuario_id and nome and empresa and self.sistema.adicionar_entregador(usuario_id, nome, empresa):
            self.atualizar_entregadores()
            messagebox.showinfo("Sucesso", "Entregador adicionado com sucesso.")
        else:
            messagebox.showerror("Erro", "ID já existe ou dados inválidos.")

        #####self.frame_entregadores.pack_forget()  # Esconde o Frame

    def atualizar_entregadores(self):
        for row in self.treeentregadores.get_children():
            self.treeentregadores.delete(row)

        entregadores = self.sistema.get_entregadores()
        for entregador in entregadores.values():
            self.treeentregadores.insert("", "end", values=(entregador.get_id_usuario(), entregador.get_nome(), entregador.get_empresa()))

    def excluir_entregador(self):
        usuario_id = self.get_input("Digite o ID do Entregador a ser excluído:")
        if usuario_id and self.sistema.excluir_entregador(usuario_id):
            self.atualizar_entregadores()
            messagebox.showinfo("Sucesso", f"Entregador {usuario_id} excluído com sucesso.")
        else:
            messagebox.showerror("Erro", "Entregador não encontrado ou ID inválido.")

    def atribuir_locker_usuario(self):
        def on_user_select():
            selected_item = tree_users.selection()
            if selected_item:
                usuario_id = tree_users.item(selected_item, "values")[0]
                usuario_tipo = tree_users.item(selected_item, "values")[2]
                if self.sistema.associar_locker_ao_usuario(locker_id, usuario_id, usuario_tipo):
                    messagebox.showinfo("Sucesso", "Locker atribuído com sucesso.")
                    self.atualizar_lockers()
                    user_window.destroy()
                else:
                    messagebox.showerror("Erro", "Erro ao atribuir locker.")
            else:
                messagebox.showerror("Erro", "Nenhum usuário selecionado.")

        locker_id = self.get_input("Digite o ID do Locker:")

        if locker_id and self.sistema.is_locker_livre(locker_id):
            # Cria uma nova janela para selecionar o usuário
            user_window = tk.Toplevel(self.janela)
            user_window.title("Selecionar Usuário/Morador/Entregador")

            # Treeview para exibir os usuários
            tree_users = ttk.Treeview(user_window, columns=("ID", "Nome", "Tipo"), show="headings")
            tree_users.heading("ID", text="ID")
            tree_users.heading("Nome", text="Nome")
            tree_users.heading("Tipo", text="Tipo")
            tree_users.pack(fill=tk.BOTH, expand=True)

            # Adiciona usuários comuns
            for usuario_id, usuario in self.sistema.get_usuarios().items():
                tree_users.insert("", "end", values=(usuario_id, usuario.get_nome(), "Usuário"))

            # Adiciona moradores
            for usuario_id, morador in self.sistema.get_moradores().items():
                tree_users.insert("", "end", values=(usuario_id, morador.get_nome(), "Morador"))

            # Adiciona entregadores
            for usuario_id, entregador in self.sistema.get_entregadores().items():
                tree_users.insert("", "end", values=(usuario_id, entregador.get_nome(), "Entregador"))

            
            '''# Inserir dados dos usuários na Treeview
            for usuario_id, usuario in self.sistema.get_usuarios().items() or usuario_id, morador in self.sistema.get_moradores().items() or usuario_id, entregador in self.sistema.get_entregadores().items():
                tree_users.insert("", "end", values=(usuario_id, usuario.get_nome()))
                tree_users.insert("", "end", values=(usuario_id, morador.get_nome()))
                tree_users.insert("", "end", values=(usuario_id, entregador.get_nome()))'''

            # Botão para confirmar a seleção do usuário
            btn_select_user = tk.Button(user_window, text="Selecionar", command=on_user_select)
            btn_select_user.pack()

        else:
            messagebox.showerror("Erro", "Locker não disponível.")

    def liberar_locker(self):
        locker_id = self.get_input("Digite o ID do Locker:")
        if locker_id and self.sistema.libera_locker(locker_id):
            messagebox.showinfo("Sucesso", "Locker liberado com sucesso.")
            self.atualizar_lockers()
        else:
            messagebox.showerror("Erro", "Erro ao liberar locker.")

    def verificar_status_locker(self):
        locker_id = self.get_input("Digite o ID do Locker:")
        if locker_id:
            esta_ocupado, usuario_id, usuario_tipo = self.sistema.get_locker_status(locker_id)
            if esta_ocupado:
                usuario = self.sistema.get_usuario(usuario_id, usuario_tipo)
                messagebox.showinfo("Status do Locker", f"Locker {locker_id} - Ocupado por {usuario_tipo}: {usuario}")
            if esta_ocupado is None:
                messagebox.showerror("Erro", "ID inválido, Locker não encontrado.")
            else:
                messagebox.showinfo("Status do Locker", "Locker disponível.")
            

    def salvar_dados(self):
        nome_arquivo = self.get_input("Digite o nome do arquivo para salvar os dados:")
        if nome_arquivo:
            self.sistema.salvar_dados(nome_arquivo)
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso.")
        else:
            messagebox.showerror("Erro", "Nome de arquivo inválido.")

    def carregar_dados(self):
        nome_arquivo = self.get_input("Digite o nome do arquivo para carregar os dados:")
        if nome_arquivo:
            self.sistema.carregar_dados(nome_arquivo)
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso.")
            self.atualizar_lockers()
        else:
            messagebox.showerror("Erro", "Nome de arquivo inválido.")

    def get_input(self, prompt):
        return simpledialog.askstring("Input", prompt)

if __name__ == "__main__":
    janela = tk.Tk()
    app = App(janela)
    janela.mainloop()
