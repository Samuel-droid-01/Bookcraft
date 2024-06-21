from ..usuario.usuarioDAO import UsuarioDAO
from ...bd.domain.solicitud import Solicitud
from ...bd.domain.prestamo import Prestamo
from ...bd.mappers.prestamo.prestamo_map import PrestamoMapper
from ...bd.mappers.solicitud.solicitud_map import SolicitudMapper
from datetime import datetime

class LectorDAO(UsuarioDAO):
    def __init__(self):
        super().__init__()
    
    def solicitar_prestamo(self, id_libro,fecha_devolucion,id_sancion,activo):#Se cambio de que insertaba en solicitudes a que inserta en prestamos
        prestamo = Prestamo(None, self.get_usuario().get_id(), id_libro, datetime.now().strftime('%Y-%m-%d'),fecha_devolucion,id_sancion,activo )
        mapper = PrestamoMapper()
        return mapper.insert(prestamo)


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
    
    