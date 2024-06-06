python -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.Registro_test
if ($?) { python -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.prestamo_test }
if ($?) { python -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.libro_test }
if ($?) { python -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.catalogo_test }
if ($?) { python -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.administrador_test }