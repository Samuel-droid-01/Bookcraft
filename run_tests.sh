python3 -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.Registro_test #correr test individual de registro insertar solo este codigo en la terminal
python3 -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.prestamo_test
python3 -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.libro_test
python3 -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.catalogo_test
python3 -m unittest proyecto_frameworks_persistencia.src.test.bookcraft.dao.administrador_test


#chmod +x run_tests.sh  ->>>>  para darle permisos de ejecucion y crear el archivo ejecutable
#./run_tests.sh     ->>>>  para correr los tests