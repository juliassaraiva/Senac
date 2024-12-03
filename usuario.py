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
