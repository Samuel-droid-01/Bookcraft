from ....main.bookcraft.bd.domain.sancion import Sancion
from ....main.bookcraft.bd.mappers.sancion.sancion_map import SancionMapper
test_sancion = Sancion(
7    ,
    '2027-10-10',
    '2028-10-10',
    'No devolver libro1'
)
sancion_mapper = SancionMapper()
#sancion_mapper.insert(test_sancion)
print(sancion_mapper.get_by_id(1))
print(sancion_mapper.get_by_id(2))
sancion_mapper.update(test_sancion)
print(sancion_mapper.delete(test_sancion))