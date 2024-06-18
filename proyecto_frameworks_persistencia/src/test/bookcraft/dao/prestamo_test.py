import unittest

from ....main.bookcraft.dao.prestamo.prestamoDAO import PrestamoDAO
from ....main.bookcraft.bd.mappers.prestamo.prestamo_map import PrestamoMapper

class Test_prestamo(unittest.TestCase):
    print("Test de Prestamo")
    def test_set_prestamo(self):
        
        mappers= PrestamoMapper()
        registro=mappers.get_all()
        tamaño=len(registro)
        prestamo = PrestamoDAO(0, 0, '2021-10-10', '2021-10-10', 0, 0)
        try:
            prestamo.set_prestamo()
            self.assertEqual(len(mappers.get_all()), tamaño+1)
            print("\tprestamo insertado correctamente")
        except Exception as e:
            self.fail(f"\tError al insertar el prestamo: {e}")

    def test_get_prestamo(self):

        prestamo=PrestamoDAO(id=9)
        try:
            info_prestamo=prestamo.get_prestamo()
            #print("\tprestamo{",info_prestamo,"}")
            print("\tprestamo obtenido correctamente")
        except Exception as e:
            self.fail(f"\tError al obtener el prestamo: {e}")
    @unittest.skip("funcionando con un id existente")
    def test_sancionar(self):

        prestamo=PrestamoDAO(id=9)
        try:
            prestamo.sancionar("Sancion por retraso")
        except Exception as e:
            self.fail(f"\tError al sancionar el prestamo: {e}")
    #@unittest.skip("no se puede eliminar un prestamo que no existe")
    @unittest.skip("funcionando con un id existente")
    def test_delete_prestamo(self):
        mappers= PrestamoMapper()
        tamaño=len(mappers.get_all())
        print(tamaño)
        prestamo=PrestamoDAO(id=13)#------>asignar un id existente
        try:
            prestamo.delete_prestamo()
            print("\tprestamo eliminado correctamente")
            tamaño1=len(mappers.get_all())
            print(tamaño1)
            
            if tamaño1 != tamaño-1:
                self.fail("Puede que el id usado no exista, verifique y vuelva a intentarlo")
            self.assertEqual(tamaño1,tamaño-1)
            print("\tprestamo eliminado correctamente")
        except Exception as e:
                self.fail(f"\tError al eliminar el prestamo: {e}")
                
    @unittest.skip("funcionando con un id existente")
    def test_update_prestamo(self):
        id=10
        mappers=PrestamoMapper
        try:
            data=mappers.get_by_id(id)
        except:
            self.fail("dato inexiste, imposible actualizar")

        prestamo=PrestamoDAO(id=10 )
        prestamo.get_prestamo().set_fecha_devolucion('1500-10-10')
        try:
            prestamo.update_prestamo()
            print("\tprestamo actualizado correctamente")
        except Exception as e:
            self.fail(f"\tError al actualizar el prestamo: {e}")


