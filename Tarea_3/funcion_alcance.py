def celdas_inalcanzables(tablero):
    inalcanzables=[]
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            inalcanzables.append([i,j])
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j]!='0':
                eliminar_de_lista(inalcanzables,[i,j])
                for l in range(-(int(tablero[i][j])),int(tablero[i][j])+1):
                    eliminar_de_lista(inalcanzables,[i+l,j])
                    eliminar_de_lista(inalcanzables,[i,j+l])
    print(inalcanzables)

def eliminar_de_lista(lista,elemento):
    if elemento in lista:
        lista.pop(lista.index(elemento))

def validar_celda_tablero(tablero,i,j):
    if i<0 or j<0 or i>len(tablero)-1 or j>len(tablero[0])-1:
        return False
    return True

def generar_decisiones(tablero,i,j):
    decisiones=[[],[],[],[]]
    if tablero[i][j]!='0':
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i+l,j):
                decisiones[0].append([i+l,j])
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i-l,j):
                decisiones[1].append([i-l,j])
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i,j+l):
                decisiones[2].append([i,j+l])
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i,j-l):
                decisiones[3].append([i,j-l])
    decisiones=limpiar_lista_sublistas_vacias(decisiones)
    return decisiones

def eliminar_celda_de_decision(celda_eliminar,decisiones):
    for camino in decisiones:
        for celda in camino:
            if celda==celda_eliminar:
                indice_camino=decisiones.index(camino)
                decisiones[0],decisiones[indice_camino]=decisiones[indice_camino],decisiones[0]
                if len(decisiones)==1:
                    return [decisiones[0][1:]]
                return [decisiones[0][1:]]+decisiones[1:]


def limpiar_lista_sublistas_vacias(lista):
    while [] in lista:
        lista.pop(lista.index([]))
    return lista

def combinaciones_posibles(tablero,numero,lista_decisiones,combinacion_solucion=None,i=0):
    if i==0 and combinacion_solucion is None:
        combinacion_solucion=[0]*(numero)
    if numero==0:
        print('-------->',combinacion_solucion)
        return
    for decision in lista_decisiones:
        #print(decision)
        #print(lista_decisiones)
        #print(decision[0])
        combinacion_solucion[i]=decision[0]
        #print(limpiar_lista_sublistas_vacias(eliminar_celda_de_decision(decision[0],lista_decisiones)))
        (combinaciones_posibles(tablero,numero-1,limpiar_lista_sublistas_vacias(eliminar_celda_de_decision(decision[0],lista_decisiones)),combinacion_solucion,i+1))
        #print(lista_decisiones)
        lista_decisiones=lista_decisiones[1:]
        #print(lista_decisiones,'\n')

#archivo=input('nombre del archivo (nombre.txt): ')
archivo_tablero=open('tablero_dificil.txt','r')
tablero=[]
for linea in archivo_tablero:
    tablero.append(linea.split())

#celdas_inalcanzables(tablero)
#print(generar_decisiones(tablero,4,2))
#print(eliminar_celda_de_decision([1,2],generar_decisiones(tablero,0,2)))
#print(limpiar_lista_sublistas_vacias(eliminar_celda_de_decision([1,2],generar_decisiones(tablero,0,2))))
#combinaciones_posibles(tablero,2,generar_decisiones(tablero,2,3))
#combinaciones_posibles(tablero,1,generar_decisiones(tablero,0,0))
#combinaciones_posibles(tablero,2,generar_decisiones(tablero,4,0))
#combinaciones_posibles(tablero,4,generar_decisiones(tablero,2,1))
#combinaciones_posibles(tablero,5,generar_decisiones(tablero,3,3))
#combinaciones_posibles(tablero,4,generar_decisiones(tablero,4,4))

for i in range(len(tablero)):
    for j in range(len(tablero)):
        if tablero[i][j]!='0':
            combinaciones_posibles(tablero,int(tablero[i][j])-1,generar_decisiones(tablero,i,j))
