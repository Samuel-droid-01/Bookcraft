from ....main.bookcraft.bd.domain.reservacion import Reservacion
from ....main.bookcraft.bd.mappers.reservacion.reservacion_map import ReservacionMapper


test_reservacion = Reservacion(
    2,
    2,
    1,
    '2024-10-10 10:10:10',
)

reservacion_mapper = ReservacionMapper()
aux=reservacion_mapper.getnombreUsuario(1)
print(aux)
aux2=reservacion_mapper.getnombreLibro(1)
print(aux2)
#reservacion_mapper.delete(3)
#reservacion_mapper.insert(test_reservacion)
#print(reservacion_mapper.find_by_id(4).get_fecha_reservacion())

