from ..administrador.administradorDAO import AdministradorDAO
from ...bd.domain.solicitud import Solicitud
from ...bd.mappers.solicitud.solicitud_map import SolicitudMapper
from typing import List

class BibliotecarioDAO(AdministradorDAO):
    def __init__(self):
        self.__solicitudes_prestamo: List[Solicitud] = []
        self.__solicitudes_reservacion: List[Solicitud] = []
        self.__solicitudes_renovacion: List[Solicitud] = []
        self.__solicitudes_devolucion: List[Solicitud] = []
    
    def recibir_solicitudes_prestamo(self):
        mapper = SolicitudMapper()
        self.__solicitudes_prestamo = mapper.select_by_tipo('prestamo')

    def recibir_solicitudes_reservacion(self):
        mapper = SolicitudMapper()
        self.__solicitudes_reservacion = mapper.select_by_tipo('reservacion')

    def recibir_solicitudes_renovacion(self):
        mapper = SolicitudMapper()
        self.__solicitudes_renovacion = mapper.select_by_tipo('renovacion')
    
    def recibir_solicitudes_devolucion(self):
        mapper = SolicitudMapper()
        self.__solicitudes_devolucion = mapper.select_by_tipo('devolucion')
    
    def get_solicitudes_prestamo(self):
        return self.__solicitudes_prestamo
    
    def get_solicitudes_reservacion(self):
        return self.__solicitudes_reservacion
    
    def get_solicitudes_renovacion(self):
        return self.__solicitudes_renovacion
    
    def get_solicitudes_devolucion(self):
        return self.__solicitudes_devolucion
