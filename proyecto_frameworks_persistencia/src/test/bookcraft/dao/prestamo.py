from ....main.bookcraft.bd.domain.prestamo import Prestamo
from ....main.bookcraft.bd.mappers.prestamo.prestamo_map import PrestamoMapper
test_prestamo = Prestamo(
    2,
    1,
    1,
    '2024-10-10',
    '2026-10-10',
    1,
    1
)
prestamo_mapper = PrestamoMapper()
#prestamo_mapper.insert(test_prestamo)
prestamo_mapper.delete(test_prestamo)
print(prestamo_mapper.get_by_id(2))