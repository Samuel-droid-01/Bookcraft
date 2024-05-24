# Por el momento solo se probaran las operaciones definidas en mappers

from ....main.bookcraft.bd.domain.libro import Libro
from ....main.bookcraft.bd.mappers.libro.libro_map import LibroMapper

test_libro = Libro(
    1,
    'No manches Frida',
    978,
    'Miguel de Cervantes',
    'Espasa',
    '1605-01-16',
    1,
    'Primera',
    1345,
    10,
    10
)

test_libro_mapper = LibroMapper()
#test_libro_mapper.insert(test_libro)
l = test_libro_mapper.get_all()
#for i in l:
#    print(i.get_titulo())
l = test_libro_mapper.get_by_category("Accion")
print(l[0].get_titulo())