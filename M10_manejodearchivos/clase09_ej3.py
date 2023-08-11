import sys
if len(sys.argv) == 4:
    print("El primer parametro es:", sys.argv[1])
    print("El segundo parametro es:",sys.argv[2])
    print("El tercer parametro es:",sys.argv[3])
else:
    print("ERROR: Introdujo un cantidad de argumentos distinta de tres (3)")
    print("Ejemplo: clase09_ej4.py 1 2 3")