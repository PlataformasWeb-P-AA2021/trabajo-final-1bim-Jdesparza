archivo = open('data/Listado-Instituciones-Educativas.csv', 'r', encoding='utf-8')
copyArchivo = archivo
linea1 = next(copyArchivo)
linea1 = linea1.split('\n')
copyLinea1 = linea1

for linea in archivo:
    #linea = linea.replace('\n', '')
    if (linea != linea1):
        copyLinea = copyLinea1[0].split('|')
        token = linea.split('|')
        for i in range(len(token)):
            print("%2d - %50s: %s" % (i, copyLinea[i], token[i]))
        print()

archivo.close()