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
