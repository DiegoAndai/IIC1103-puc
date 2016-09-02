class Kuromasu:

    def __init__(self,archivo_tablero):
        self.tablero=[]
        for linea in archivo_tablero:
            self.tablero.append(linea.split())
        self.celdas_blancas=[]
        self.celdas_numeradas=[]
        self.celdas_negras=[]
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if celda_ocupada(self.tablero,i,j) and self.tablero[i][j]!='X':
                    self.celdas_numeradas.append([i,j])
                elif self.tablero[i][j]=='X':
                    self.celdas_negras.append([i,j])

    def dibujarTablero(self):
        print('\n')
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if [i,j] in self.celdas_negras:
                    print(' ',chr(9679),' ',end='')
                elif [i,j] in self.celdas_numeradas:
                    print(' ',chr(9311+int(self.tablero[i][j])),' ',end='')
                else:
                    print(' ',chr(9675),' ',end='')
            print('\n')
        print('\n')

    def agregarNegra(self,i,j):
        if [int(i),int(j)] in self.celdas_numeradas:
            print('esa celda no puede pintarse de negro pues contiene un numero')
            sleep(2.3)
        elif not validar_celda_tablero(self.tablero,int(i),int(j)):
            print('esa posicion no pertenece al tablero(fuera de limites)')
            sleep(2.3)
        elif negras_adyacentes(self.celdas_negras,int(i),int(j)):
            print('dos negras no pueden estar juntas ni horizontal ni verticalmente')
            sleep(2.3)
        elif [int(i),int(j)] in self.celdas_negras:
            print('esa celda ya fue pintada')
            sleep(2.3)
        else:
            self.celdas_negras.append([int(i),int(j)])

    def revisarSolucion_regla1(self):
        for i in range(len(self.tablero)):
                for j in range(len(self.tablero)):
                    if self.tablero[i][j]!='0' and self.tablero[i][j]!='X':
                        celda_solucionada=False
                        soluciones_celda=traducir_combinaciones_posibles(combinaciones_posibles(self.tablero,int(self.tablero[i][j])-1,generar_decisiones(self.tablero,i,j)))
                        soluciones_inviables_segun_negros=[]
                        for solucion in soluciones_celda:
                            for celda in solucion:
                                if celda in self.celdas_negras:
                                    soluciones_inviables_segun_negros.append(solucion)
                                    break
                        if soluciones_inviables_segun_negros==soluciones_celda:
                            return False
                        lista_posibles_negras=solucion_celda(self.tablero,i,j)
                        for posible_combinacion in lista_posibles_negras:
                            for negra in posible_combinacion:
                                if negra not in self.celdas_negras:
                                    break
                                celda_solucionada=True
                        if not celda_solucionada:
                            return False
        return True

    def revisarSolucion_regla4(self,posicion=[0,0],blancas=[],i=0):
        vectores=[[1,0],[0,1],[-1,0],[0,-1]]
        if i==0:
            self.blancas_simulacion_regla4=[]
            for i in range(len(self.tablero)):
                for j in range(len(self.tablero)):
                    if [i,j] not in self.celdas_negras:
                        self.blancas_simulacion_regla4.append([i,j])
            if len(self.blancas_simulacion_regla4)==1 or len(self.blancas_simulacion_regla4)==0:
                return True
            celda_comienzo=self.blancas_simulacion_regla4[0]
            for vector in vectores:
                if [celda_comienzo[0]+vector[0],celda_comienzo[1]+vector[1]] in self.blancas_simulacion_regla4:
                    if self.revisarSolucion_regla4([celda_comienzo[0]+vector[0],celda_comienzo[1]+vector[1]],self.blancas_simulacion_regla4,i+1):
                        return True
        else:
            if posicion in blancas:
                eliminar_de_lista(blancas,posicion)
            if blancas==[]:
                return True
            for vector in vectores:
                if [posicion[0]+vector[0],posicion[1]+vector[1]] in self.blancas_simulacion_regla4:
                    if self.revisarSolucion_regla4([posicion[0]+vector[0],posicion[1]+vector[1]],self.blancas_simulacion_regla4,i+1):
                        return True
        return False

    def resolver(self,celdas_numeradas=[],solucion=[],blancas=(),i=0):
        if i==0:
            celdas_numeradas=self.celdas_numeradas
            #print(celdas_numeradas)
            solucion=[[]]*len(celdas_numeradas)
        if celdas_numeradas==[]:
            #print('caso baso solucion:',solucion)
            return True
        #print(solucion_celda(self.tablero,celdas_numeradas[0][0],celdas_numeradas[0][1]))
        for combinacion in solucion_celda(self.tablero,celdas_numeradas[0][0],celdas_numeradas[0][1]):
            legal=True
            for celda in combinacion:
                #print('celda:',celda)
                if celda in blancas:
                    legal=False
                else:
                    for negras in solucion[:i]:
                        #print('sol:',solucion)
                        #print(negras)
                        if negras_adyacentes(negras,celda[0],celda[1]):
                            legal=False
                            #print('ad')
            for negras in solucion[:i]:
                for negra in negras:
                    #print ('negra:',negra)
                    #print('comb:',combinacion)
                    #print(blancas_segun_solucion(self.tablero,celdas_numeradas[0][0],celdas_numeradas[0][1],combinacion))
                    if negra in blancas_segun_solucion(self.tablero,celdas_numeradas[0][0],celdas_numeradas[0][1],combinacion):
                        #print('in')
                        legal=False
            #print('\n')
            if legal:
                #print('comb:',combinacion)
                #print('legal')
                #print(celdas_numeradas[1:])
                #print(i)
                #print('\n')
                blancas_lista=list(blancas)
                #print('comb:',combinacion)
                #print('blancas:',blancas)
                #print('sol:',solucion)
                #print(i,'\n')
                blancas_lista+=(blancas_segun_solucion(self.tablero,celdas_numeradas[0][0],celdas_numeradas[0][1],combinacion))
                solucion[i]=combinacion
                if self.resolver(celdas_numeradas[1:],solucion,tuple(blancas_lista),i+1):
                    return solucion
        #print('fail')
        #return []

    def traducirSolucion(self,solucion):
        traduccion=[]
        for combinacion in solucion:
            for negra in combinacion:
                if negra not in traduccion:
                    traduccion.append(negra)
        return traduccion

    def volverEstado_inicial(self):
        self.celdas_blancas=[]
        self.celdas_numeradas=[]
        self.celdas_negras=[]
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                if celda_ocupada(self.tablero,i,j) and self.tablero[i][j]!='X':
                    self.celdas_numeradas.append([i,j])
                elif self.tablero[i][j]=='X':
                    self.celdas_negras.append([i,j])

    def limpiarTablero(self):
        self.celdas_negras=[]

#clases
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#funciones


def eliminar_de_lista(lista,elemento): #elimina elemento de la lista, util para evitar errores si el elemento no esta
    if elemento in lista:
        #print('s')
        lista.pop(lista.index(elemento))

def celda_ocupada(tablero,i,j): #valida que la celda no este ocupada (True=ocupada, False=desocupada)
    if validar_celda_tablero(tablero,i,j):
        if tablero[i][j]!='0':
            return True
    return False

def validar_celda_tablero(tablero,i,j): #valida que la celda se encuentre dentro del tablero (True=dentro, False=fuera)
    if i<0 or j<0 or i>len(tablero)-1 or j>len(tablero[0])-1:
        return False
    return True

def negras_adyacentes(negras_actuales,i,j): #comprueba si las celdas adyacentes a [i,j] estan pintadas de negro
    if ([i+1,j] in negras_actuales) or ([i-1,j] in negras_actuales) or ([i,j+1] in negras_actuales) or ([i,j-1] in negras_actuales):
        return True
    return False

def generar_decisiones(tablero,i,j):                            #retorna todas las celdas que son "alcanzables" por la celda en la posicion i,j  segun su numero.
    decisiones=[[],[],[],[]]                                    #El formato son 4 listas para las 4 direcciones posibles, donde las celdas estan ordenadas segun cercania,
    if tablero[i][j]!='0':                                      #siendo la primera la más cerca en tal direccion, y la ultima la mas lejana en dicha direccion
        for l in range(1,int(tablero[i][j])):                   #Debe ocuparse la funcion limpiar_lista_sublistas_vacias para eliminar las listas de direcciones
            if validar_celda_tablero(tablero,i+l,j):            #en las que no haya posibilidades de movimiento
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

def eliminar_celda_de_decision(celda_eliminar,decisiones): #elimina celda elegida de la lista de caminos, funcion necesaria por el formato de las decisiones
    for camino in decisiones:
        for celda in camino:
            if celda==celda_eliminar:
                indice_camino=decisiones.index(camino)
                decisiones[0],decisiones[indice_camino]=decisiones[indice_camino],decisiones[0]
                if len(decisiones)==1:
                    return [decisiones[0][1:]]
                return [decisiones[0][1:]]+decisiones[1:]

def limpiar_lista_sublistas_vacias(lista): #elimina sublistas que sean vacias ([]) si estas existen
    while [] in lista:
        lista.pop(lista.index([]))
    return lista

def combinaciones_posibles(tablero,numero,lista_decisiones,combinacion_solucion=None,i=0,lista_combinaciones=[]): #retorna lista con tuplas que contienen las celdas que resuelven el numero,
    if i==0 and combinacion_solucion is None:                                                                     #recibe:
        combinacion_solucion=[0]*(numero)                                                                         #--->numero del que se buscan las combinaciones, restado en
        lista_combinaciones=[]                                                                                        # uno, pues numero-1 es la cantidad de celdas blancas
    if numero==0:                                                                                                     #necesarias aparte de la que contiene al numero
        lista_combinaciones.append(tuple(combinacion_solucion))                                                   #--->resultado de la funcion generar_decisiones en la posicion
        return                                                                                                        #del numero
    for decision in lista_decisiones:
        combinacion_solucion[i]=decision[0]
        (combinaciones_posibles(tablero,numero-1,limpiar_lista_sublistas_vacias(eliminar_celda_de_decision(decision[0],lista_decisiones)),combinacion_solucion,i+1,lista_combinaciones))
        lista_decisiones=lista_decisiones[1:]
    return lista_combinaciones

def traducir_combinaciones_posibles(resultado_combinaciones_posibles): #retorna lista con listas que contienen las celdas que resuelven cada numero,
    comb=[]                                                            #o sea todas las posibilidades de casillas blancas para satisfacer la regla 1 del juego, recibe el resultado
    for tupla in resultado_combinaciones_posibles:                     #de la funcion combinaciones_posibles.
        l=list(tupla)
        comb.append(l)
    return comb

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

def blancas_segun_solucion(tablero,i,j,solucion): #retorna que celdas deben ser blancas para una determinada solucion a una celda numerada
    blancas=[]
    blancas.append([i,j])
    for l in range(1,int(tablero[i][j])):
        if [i+l,j] not in solucion and validar_celda_tablero(tablero,i+l,j):
            blancas.append([i+l,j])
        else:
            break
    for l in range(1,int(tablero[i][j])):
        if [i-l,j] not in solucion and validar_celda_tablero(tablero,i-l,j):
            blancas.append([i-l,j])
        else:
            break
    for l in range(1,int(tablero[i][j])):
        if [i,j+l] not in solucion and validar_celda_tablero(tablero,i,j+l):
            blancas.append([i,j+l])
        else:
            break
    for l in range(1,int(tablero[i][j])):
        if [i,j-l] not in solucion and validar_celda_tablero(tablero,i,j-l):
            blancas.append([i,j-l])
        else:
            break
    return blancas


#funciones
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#flujo

from time import sleep
import os

archivo_tablero=open('tablero_facil.txt','r')
juego=Kuromasu(archivo_tablero)
#print(juego.celdas_numeradas)

#agregar_celda=(input('pintar celda: '))
#juego.agregarNegra(agregar_celda.split(',')[0],agregar_celda.split(',')[1])
#print(juego.tablero)
#print(juego.celdas_negras)
#print(juego.celdas_blancas)

#print(combinaciones_posibles(juego.tablero,2,generar_decisiones(juego.tablero,1,0)))
#print(solucion_celda(juego.tablero,1,0))

#juego.dibujarTablero()
#if juego.revisarSolucion_regla1():
#    print('Solucion correcta!')
#else:
#    print('Solucion incorrecta')

#if juego.revisarSolucion_regla4():
#    print('si')
#else:
#    print('no')

#juego.resolver()

#juego.dibujarTablero()
#print(juego.resolver())
#solucion=(juego.traducirSolucion(juego.resolver()))

#for negra in solucion:
#    juego.agregarNegra(negra[0],negra[1])

#juego.dibujarTablero()
#
#juego.revisarSolucion_regla1()
#juego.revisarSolucion_regla4()
#sistema_operativo=input('¿cual es su sistema operativo? (ingrese W para windows, OS para OS X(apple) o L para Linux)')
#while sistema_operativo!='W' and sistema_operativo!='OS' and sistema_operativo!='L':
#    sistema_operativo=input('¿cual es su sistema operativo? (ingrese W para windows, OS para OS X(apple) o L para Linux)')
#if sistema_operativo=='W':
#    os.system('cls')
#else:
#    os.system('clear')

print('\n')
sleep(0.5)
print('Bienvenido a:')
print('\n')
sleep(0.6)
print('                        '+chr(8490)+' '+chr(8487)+' '+chr(7772)+' '+chr(7756)+' '+chr(7743)+'  '+chr(7680)+' '+chr(7778)+' '+chr(8487)+' \n')
sleep(2)
print('En este juego de ingenio, se le presentara un tablero como este:')
tablero_ejemplo=[[2,0,0],[0,0,0],[0,3,0]]
print('\n')
for i in range(len(tablero_ejemplo)):
    for j in range(len(tablero_ejemplo)):
        if tablero_ejemplo[i][j]=='X':
            print(' ',chr(9679),' ',end='')
        elif tablero_ejemplo[i][j]==0:
            print(' ',chr(9675),' ',end='')
        else:
            print(' ',chr(9311+int(tablero_ejemplo[i][j])),' ',end='')
    print('\n')
print('\n')
input('presione enter para continuar')
print('\n')
print('El objetivo del juego es que desde cada celda que contenga un numero\nsean visibles una cantidad de celdas blancas(no pintadas) igual a dicho\nnumero. Una celda es visible cuando esta en linea horizontal o vertical')
print('sin que se interponga una celda negra, además se cuenta como visible\ntambien la celda que contiene al numero, por ejemplo: ')
tablero_ejemplo=[[2,'X',0],[0,0,0],['X',3,0]]
print('\n')
for i in range(len(tablero_ejemplo)):
    for j in range(len(tablero_ejemplo)):
        if tablero_ejemplo[i][j]=='X':
            print(' ',chr(9679),' ',end='')
        elif tablero_ejemplo[i][j]==0:
            print(' ',chr(9675),' ',end='')
        else:
            print(' ',chr(9311+int(tablero_ejemplo[i][j])),' ',end='')
    print('\n')
print('\n')
print('En este caso, la celda que contiene al dos puede ver dos celdas blancas,\nen las posiciones (1,0) y (0,0), que es en la que se encuentra el numero.\n')
print('Como puedes ver, el tablero de arriba esta solucionado, pues la celda\nque tiene un dos ve dos celdas blancas, y la que tiene un tres puede\nver tres.\n')
input('presione enter para continuar')
print('\n')
print('Además, las otras reglas son que dos celdas pintadas no pueden estar\npegadas horizontal ni verticalmente (si estan en diagonal no hay problema),\nno pueden existir islas de celdas blancas, y por ultimo las celdas\ncon numeros no se pueden pintar:\n')
tablero_ejemplo=[[2,'X',0],[0,'X',0],[0,3,'X']]
print('\n')
for i in range(len(tablero_ejemplo)):
    for j in range(len(tablero_ejemplo)):
        if tablero_ejemplo[i][j]=='X':
            print(' ',chr(9679),' ',end='')
        elif tablero_ejemplo[i][j]==0:
            print(' ',chr(9675),' ',end='')
        else:
            print(' ',chr(9311+int(tablero_ejemplo[i][j])),' ',end='')
    print('\n')
print('\n')
print('Esto no es correcto pues las celdas (0,1) y (1,1) son celdas negras\nadyacentes, ademas las celdas (0,2) y (1,2) son una isla de celdas blancas\npues estan incomunicadas')
print('\n')
input('presione enter para continuar')
print('\n')
print('Usted debe ir pintando celdas hasta encontrar la solucion. Por ultimo,\ncomo probablemente ya noto, el primer numero del par coordenado\ncorresponde a la fila y el segundo a la columna:')
tablero_ejemplo=[[2,0,0],[0,0,0],[0,3,0]]
print('\n')
for i in range(len(tablero_ejemplo)):
    for j in range(len(tablero_ejemplo)):
        if tablero_ejemplo[i][j]=='X':
            print(' ',chr(9679),' ',end='')
        elif tablero_ejemplo[i][j]==0:
            print(' ',chr(9675),' ',end='')
        else:
            print(' ',chr(9311+int(tablero_ejemplo[i][j])),' ',end='')
    print('\n')
print('\n')
print('Siguiendo esta logica, la celda con el numero dos es del par coordenado\n(0,0) y la celda con el tres es (2,1). Los numeros de filas y\ncolumnas parten de 0, siendo (0,0) la esquina superior izquierda\n')
input('enter para comenzar!')
print('\n')
print('Debe elegir un archivo que contenga un tablero para jugar')
archivo=input('ingrese el nombre del archivo (nombre.txt): ')
archivo_tablero=open(archivo,'r')
juego=Kuromasu(archivo_tablero)
print('\nSu tablero es:')
juego.dibujarTablero()
pregunta_jugar=input('En cualquier momento puede ingresar al menu para salir del\njuego, revisar si su solucion es correcta o mostrar la solucion\nal tablero.\n¿Desea comenzar? (si/no): ')
while pregunta_jugar!='si' and pregunta_jugar!='no':
    pregunta_jugar=input('¿Desea comenzar? (si/no): ')
if pregunta_jugar=='no':
    pregunta_jugar=input('¿Seguro que quiere salir del juego? (si/no): ')
    if pregunta_jugar=='si':
        jugar=False
    else:
        jugar=True
else:
    jugar=True

while jugar:
    juego.dibujarTablero()
    celda=input('ingrese celda a pintar, o el numero 0 para abrir menu: ')
    if celda=='0':
        print('\nMenu:')
        print('   1. Seguir jugando')
        print('   2. Terminar y validar solucion')
        print('   3. Resolver automaticamente')
        print('   4. Salir del juego')
        print('   5. Volver tablero a estado inicial')
        print('   6. Limpiar tablero')
        print('\n')
        eleccion_menu=input('ingrese el numero (1,2,3 o 4) de la accion a realizar: ')
        while eleccion_menu!='1' and eleccion_menu!='2' and eleccion_menu!='3' and eleccion_menu!='4' and eleccion_menu!='5' and eleccion_menu!='6':
            eleccion_menu=input('ingrese el numero (1,2,3 o 4) de la accion a realizar: ')
        if eleccion_menu=='1':
            jugar=True
        elif eleccion_menu=='2':
            if juego.revisarSolucion_regla1() and juego.revisarSolucion_regla4():
                print('\nSolucion correcta!')
            else:
                print('\nSolucion incorrecta\n')
                juego.volverEstado_inicial()
                continuar=input('¿Desea intentar de nuevo? (si/no): ')
                while continuar!='si' and continuar!='no':
                    continuar=input('¿Desea intentar de nuevo? (si/no): ')
                if continuar=='si':
                    jugar=True
                else:
                    jugar=False
        elif eleccion_menu=='3':
            if len(juego.tablero)>=10:
                print('\nSu tablero es de tamaño',len(juego.tablero),'por lo que la resolucion podría tardarse,\n(ha sido testeado un tablero de 17x17, que se resolvio en aproximadamente\n20 minutos y uno de 11x11 se resolvio en medio minuto aproximadamente) ')
            juego.limpiarTablero()
            solucion=(juego.traducirSolucion(juego.resolver()))
            for negra in solucion:
                juego.agregarNegra(negra[0],negra[1])
            print('\nSolucion:')
            juego.dibujarTablero()
            juego.volverEstado_inicial()
            archivo_guardar=open(archivo,'w')
            for fila in juego.tablero:
                for columna in fila:
                    archivo_guardar.write(columna)
                    archivo_guardar.write(' ')
                archivo_guardar.write('\n')
            print('Se ha guardado el tablero en su estado inicial, ¡vuelve pronto!\n')
            jugar=False
        elif eleccion_menu=='4':
            archivo_guardar=open(archivo,'w')
            for i in range(len(juego.tablero)):
                for j in range(len(juego.tablero)):
                    if [i,j] in juego.celdas_negras:
                        archivo_guardar.write('X')
                        archivo_guardar.write(' ')
                    elif juego.tablero[i][j]!='0' and juego.tablero[i][j]!='X':
                        archivo_guardar.write(juego.tablero[i][j])
                        archivo_guardar.write(' ')
                    else:
                        archivo_guardar.write('0')
                        archivo_guardar.write(' ')
                archivo_guardar.write('\n')
            print('Se han guardado tus respuestas en el archivo. Gracias por jugar.\n¡vuelve pronto!\n')
            jugar=False
        elif eleccion_menu=='5':
            juego.volverEstado_inicial()
        elif eleccion_menu=='6':
            juego.limpiarTablero()
    else:
        juego.agregarNegra(celda.split(',')[0],celda.split(',')[1])
