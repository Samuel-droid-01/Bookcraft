from abc import ABCMeta, abstractmethod
from ...domain.usuario import Usuario

class UsuarioMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, usuario: Usuario):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass
    @abstractmethod
    def get_all(self)->list[Usuario]:
        pass    

    @abstractmethod
    def update(self, usuario: Usuario):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def validar_credenciales(self, correo: str, contrasena: str):
        pass
    
    @abstractmethod
    def validar_correo(self, correo: str):
        pass
