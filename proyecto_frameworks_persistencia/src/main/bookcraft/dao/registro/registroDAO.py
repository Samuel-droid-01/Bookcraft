from ...dao.prestamo.prestamoDAO import PrestamoDAO
from ...bd.mappers.prestamo.prestamo_map import PrestamoMapper
from ...bd.mappers.reservacion.reservacion_map import ReservacionMapper
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.domain.reservacion import Reservacion
from datetime import datetime, timedelta

class RegistroDAO:
    def __init__(self):
        pass
    
    def finalizar_prestamo(self, id_prestamo):
        prestamoaf = PrestamoDAO(id=id_prestamo)
        prestamoaf.get_prestamo().set_activo(0)
        
        fecha_actual = datetime.now()
        fecha_actual_entero = int(fecha_actual.strftime('%Y%m%d'))
        
        fecha_fin = prestamoaf.get_prestamo().get_fecha_devolucion()
        
        if isinstance(fecha_fin, str):
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        fecha_fin_entero = int(fecha_fin.strftime('%Y%m%d'))
    
        
        if fecha_actual_entero > fecha_fin_entero:
            prestamoaf.sancionar("sancion")
        else:
            prestamoaf.update_prestamo()
            
    def extender_prestamo(self, id_usuario,id_libro,fecha_prestamo,fecha_devolucion):
        try:
            prestamoaf = PrestamoDAO(id_usuario, id_libro, fecha_prestamo, fecha_devolucion, 0, 1)
            prestamoaf.set_prestamo()
        except:
            print("datos incorrectos")
    
    def realizar_prestamo(self, id_usuario,id_libro,fecha_prestamo,fecha_devolucion):
        try:
            prestamoaf = PrestamoDAO(id_usuario, id_libro, fecha_prestamo, fecha_devolucion, 0, 1)
            prestamoaf.set_prestamo()
        except:
            print("datos incorrectos")
    
    def reservar_prestamo(self,id_usuario,id_libro,fecha_reservacion):
        try:
            mapper = ReservacionMapper()
            reserva = Reservacion(id_usuario, id_libro,fecha_reservacion)
            mapper.insert(reserva)
        except:
            print("datos incorrectos")

