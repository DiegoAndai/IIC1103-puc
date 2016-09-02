
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

def celda_ocupada(tablero,i,j):
    if validar_celda_tablero(tablero,i,j):
        if tablero[i][j]!='0':
            return True
    return False

def generar_decisiones(tablero,i,j):
    decisiones=[[],[],[],[]]
    if tablero[i][j]!='0':
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i+l,j):
                if tablero[i+l][j]!='X':
                    decisiones[0].append([i+l,j])
                else:
                    break
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i-l,j):
                if tablero[i-l][j]!='X':
                    decisiones[1].append([i-l,j])
                else:
                    break
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i,j+l):
                if tablero[i][j+l]!='X':
                    decisiones[2].append([i,j+l])
                else:
                    break
        for l in range(1,int(tablero[i][j])):
            if validar_celda_tablero(tablero,i,j-l):
                if tablero[i][j-l]!='X':
                    decisiones[3].append([i,j-l])
                else:
                    break
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

def combinaciones_posibles(tablero,numero,lista_decisiones,combinacion_solucion=None,i=0,lista_combinaciones=[]):
    if i==0 and combinacion_solucion is None:
        combinacion_solucion=[0]*(numero)
        lista_combinaciones=[]
    if numero==0:
        #print('-------->',combinacion_solucion)
        lista_combinaciones.append(tuple(combinacion_solucion))
        return # (combinacion_solucion)
    for decision in lista_decisiones:
        #print(decision)
        #print(lista_decisiones)
        #print(decision[0])
        combinacion_solucion[i]=decision[0]
        #print(limpiar_lista_sublistas_vacias(eliminar_celda_de_decision(decision[0],lista_decisiones)))
        (combinaciones_posibles(tablero,numero-1,limpiar_lista_sublistas_vacias(eliminar_celda_de_decision(decision[0],lista_decisiones)),combinacion_solucion,i+1,lista_combinaciones))
        #print(lista_decisiones)
        lista_decisiones=lista_decisiones[1:]
        #print(lista_decisiones,'\n')
    return lista_combinaciones

def traducir_combinaciones_posibles(resultado_combinaciones_posibles):
    comb=[]
    for tupla in resultado_combinaciones_posibles:
        l=list(tupla)
        comb.append(l)
    return comb



#archivo=input('nombre del archivo (nombre.txt): ')
archivo_tablero=open('tablero_facil.txt','r')
tablero=[]
for linea in archivo_tablero:
    tablero.append(linea.split())

#celdas_inalcanzables(tablero)
#print(generar_decisiones(tablero,4,2))
#print(eliminar_celda_de_decision([1,2],generar_decisiones(tablero,0,2)))
#print(limpiar_lista_sublistas_vacias(eliminar_celda_de_decision([1,2],generar_decisiones(tablero,0,2))))
#combinaciones_posibles(tablero,2,generar_decisiones(tablero,2,3))
#print(combinaciones_posibles(tablero,1,generar_decisiones(tablero,0,0)))
#combinaciones_posibles(tablero,2,generar_decisiones(tablero,4,0))
#combinaciones_posibles(tablero,4,generar_decisiones(tablero,2,1))
#combinaciones_posibles(tablero,5,generar_decisiones(tablero,3,3))
#combinaciones_posibles(tablero,4,generar_decisiones(tablero,4,4))

#for i in range(len(tablero)):
#    for j in range(len(tablero)):
#        if tablero[i][j]!='0':
#            combinaciones_posibles(tablero,int(tablero[i][j])-1,generar_decisiones(tablero,i,j))


#print(combinaciones_posibles(tablero,1,generar_decisiones(tablero,0,0)))
#print(traducir_combinaciones_posibles(combinaciones_posibles(tablero,2,generar_decisiones(tablero,2,3))))

def solucion_celda(tablero,i,j):  #retorna la combinacion de celdas negras que necesita una posicion para ser resuelta (lista con todas las combinaciones posibles)
    celdas_negras_cada_solucion=[]
    soluciones=(traducir_combinaciones_posibles(combinaciones_posibles(tablero,int(tablero[i][j])-1,generar_decisiones(tablero,i,j))))
    for solucion in soluciones:
        celdas_negras=[]
        i_min=min(solucion[n][0] for n in range(len(solucion)))
        if i_min>i:
            i_min=i
        if validar_celda_tablero(tablero,i_min-1,j):
            celdas_negras.append([i_min-1,j])
            if tablero[i_min-1][j]!='0' and tablero[i_min-1][j]!='X':
                continue
        i_max=max(solucion[n][0] for n in range(len(solucion)))
        if i_max<i:
            i_max=i
        if validar_celda_tablero(tablero,i_max+1,j):
            celdas_negras.append([i_max+1,j])
            if tablero[i_max+1][j]!='0' and tablero[i_max+1][j]!='X':
                continue
        j_min=min(solucion[n][1] for n in range(len(solucion)))
        if j_min>j:
            j_min=j
        if validar_celda_tablero(tablero,i,j_min-1):
            celdas_negras.append([i,j_min-1])
            if tablero[i][j_min-1]!='0' and tablero[i][j_min-1]!='X':
                continue
        j_max=max(solucion[n][1] for n in range(len(solucion)))
        if j_max<j:
            j_max=j
        if validar_celda_tablero(tablero,i,j_max+1):
            celdas_negras.append([i,j_max+1])
            if tablero[i][j_max+1]!='0' and tablero[i][j_max+1]!='X':
                continue
        celdas_negras_cada_solucion.append(celdas_negras)
    return celdas_negras_cada_solucion


print(solucion_celda(tablero,4,4))

#for aolucion in (solucion_celda(tablero,0,2)):
#    for celda in aolucion:
#        tablero[celda[0]][celda[1]]='X'
#    for linea in tablero:
#        for celda in linea:
#            print(celda,'  ',end='')
#        print('\n')
#    print('\n')
#    for celda in aolucion:
#        tablero[celda[0]][celda[1]]='0'
