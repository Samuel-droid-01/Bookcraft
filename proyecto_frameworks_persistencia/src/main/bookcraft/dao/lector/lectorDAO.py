from ..usuario.usuarioDAO import UsuarioDAO
from ...bd.domain.solicitud import Solicitud
from ...bd.mappers.solicitud.solicitud_map import SolicitudMapper
from datetime import datetime

class LectorDAO(UsuarioDAO):
    def __init__(self):
        super().__init__()
    
    def solicitar_prestamo(self, id_libro):
        solicitud = Solicitud(None, self.get_usuario().get_id(), id_libro, 'prestamo', datetime.now().strftime('%Y-%m-%d'))
        mapper = SolicitudMapper()
        mapper.insert(solicitud)

    def solicitar_reservacion(self, id_libro):
        solicitud = Solicitud(None, self.get_usuario().get_id(), id_libro, 'reservacion', datetime.now().strftime('%Y-%m-%d'))
        mapper = SolicitudMapper()
        mapper.insert(solicitud)

    def solicitar_renovacion(self, id_libro):
        solicitud = Solicitud(None, self.get_usuario().get_id(), id_libro, 'renovacion', datetime.now().strftime('%Y-%m-%d'))
        mapper = SolicitudMapper()
        mapper.insert(solicitud)

    def solicitar_devolucion(self, id_libro):
        solicitud = Solicitud(None, self.get_usuario().get_id(), id_libro, 'devolucion', datetime.now().strftime('%Y-%m-%d'))
        mapper = SolicitudMapper()
        mapper.insert(solicitud)
    
    