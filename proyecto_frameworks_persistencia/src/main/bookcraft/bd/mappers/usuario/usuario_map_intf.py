from abc import ABCMeta, abstractmethod
from ...domain.usuario import Usuario

class UsuarioMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def get_usuario_by_id(self, id: int) -> Usuario:
        pass

    @abstractmethod
    def update_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def delete_usuario(self, id: int):
        pass
