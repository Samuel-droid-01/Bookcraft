from ....main.bookcraft.bd.domain.solicitud import Solicitud
from ....main.bookcraft.bd.mappers.solicitud.solicitud_map import SolicitudMapper

test_solicitud = Solicitud(
    1,
    1,
    1,
    'prestamo1',
    '2027-10-10'
)

solicitud_mapper = SolicitudMapper()
solicitud_mapper.delete(2)
print(solicitud_mapper.get_by_id(1).get_fecha())
print(solicitud_mapper.get_all())