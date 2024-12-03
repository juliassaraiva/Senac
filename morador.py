from usuario import Usuario
#Herança
#CLASSE MORADOR
class Morador(Usuario):
    def __init__(self, usuario_id, nome, apartamento):
        super().__init__(usuario_id, nome)
        self.__apartamento = apartamento
        self.__tipo = "Morador"
    
    def get_apartamento(self):
        return self.__apartamento

    def get_status(self):
        return self.usuario_id(), self.nome(), self.__apartamento, self.__tipo
