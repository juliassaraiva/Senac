from usuario import Usuario
#Herança
#CLASSE ENTREGADOR
class Entregador(Usuario):
    def __init__(self, usuario_id, nome, empresa):
        super().__init__(usuario_id, nome)
        self.__empresa = empresa
        self.__tipo = "Entregador"

    def get_empresa(self):
        return self.__empresa

    def get_status(self):
        return self.usuario_id(), self.nome(), self.__empresa, self.__tipo
