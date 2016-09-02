from poker import Carta, Tablero, Baraja
from poker import obtenerApuestaRobot, compararJugadas
from time import sleep

Mesa=Tablero()

bordes=[[30,0,19,2],[15,2,49,8],[5,11,20,8],[55,11,20,8],[31,12,18,6]]
for borde in bordes:
    Mesa.dibujarBorde(borde[0],borde[1],borde[2],borde[3])
mensajes_iniciales=[["  Texas  Hold'em  ",31,1],[' Cartas en mesa ',32,10],[' Tus cartas ',5,19],[' Contrincante ',62,19],['Pozo acumulado:',33,13],['Apuesta actual:',33,16],['$:',3,9],['$:',67,9]]
for mensaje in mensajes_iniciales:
    Mesa.escribirMensaje(mensaje[0],mensaje[1],mensaje[2])
print (Mesa)


#Mesa.borrarZona(32,13,16,5)
#Mesa.escribirMensaje('Tu contrincante',33,13)
#Mesa.escribirMensaje('se retira!',36,14)
#Mesa.escribirMensaje('Te llevas:',36,16)
#Mesa.escribirMensaje('$1000',((16-len('$1000')//2)+24),17)

#Mesa.borrarZona(32,13,16,5)
#Mesa.escribirMensaje('Te has retirado',35,14)
#Mesa.escribirMensaje('Tu oponente',35,15)
#Mesa.escribirMensaje('se lleva:',36,16)

#Mesa.borrarZona(32,13,16,5)
#Mesa.escribirMensaje('Has perdido',35,14)
#Mesa.escribirMensaje('Tu oponente',35,15)
#Mesa.escribirMensaje('se  lleva:',36,16)
#Mesa.escribirMensaje('$1000',((16-len('$1000')//2)+24),17)

#Mesa.escribirMensaje('Contrincante sube la apuesta!',26,11)

#Mesa.borrarZona(32,13,16,5)
#Mesa.escribirMensaje('Tu contrincante',33,14)
#Mesa.escribirMensaje('ha subido la',35,15)
#Mesa.escribirMensaje('apuesta',37,16)

#Mesa.escribirMensaje('Tu apuesta:',2,4)
#Mesa.escribirMensaje('$10000',((8-len('$10000')//2)),5)

#Mesa.borrarZona(32,13,16,5)
#Mesa.escribirMensaje('Empate!',37,14)
#Mesa.escribirMensaje('Cada  uno',36,15)
#Mesa.escribirMensaje('se lleva:',36,16)

#Mesa.escribirMensaje('Te llevas 100000000, hasta la proxima',((81-len('Te llevas 100000000, hasta la proxima'))//2),6)

#def suspenso(tiempo):
#    Mesa.borrarZona(32,13,16,5)
#    Mesa.escribirMensaje('Suspenso',33,15)
#    print(Mesa)
#    puntitos='.'
#    for i in range(0,7):
#        sleep(tiempo)
#        Mesa.escribirMensaje(puntitos,41+i,15)
#        print(Mesa)
#        sleep(tiempo)

#suspenso(0.15)

#Bienvenida="Bienvenido a Texas Hold'em, en este juego de"
#Bienvenida2="cartas debes formar la mejor combinacion posible"
#Bienvenida3='ocupando tus cartas y las de la mesa.'

#Bienvenida4="En cada ronda se da vuelta un numero de cartas"
#Bienvenida5="y se debe apostar, ten en cuenta que cuando se"
#Bienvenida6="pida igualar la apuesta del contrincante,  debes"
#Bienvenida7="ingresar lo que te falta y no la apuesta total."

#Bienvenida='Este juego contiene simples y modestas'
#Bienvenida2='animaciones, que estan probadas en la Terminal'
#Bienvenida3='del sistema operativo Ubuntu.'
#Bienvenida4='Si esta corriendo este programa en otra interfaz'
#Bienvenida5='como IDLE, porfavor ajuste la ventana con'
#Bienvenida6='respecto a este tablero.'

#Instruccion1=[['Este juego contiene simples y modestas',21,3],['animaciones, que estan probadas en la Terminal',17,4],['del sistema operativo Ubuntu.',26,5],\
#                ['Si esta corriendo este programa en otra interfaz',16,6],['como IDLE, porfavor ajuste la ventana con',20,7],['respecto a este tablero.',29,8]]





#Mesa.escribirMensaje(Bienvenida,21,3)
#Mesa.escribirMensaje(Bienvenida2,17,4)
#Mesa.escribirMensaje(Bienvenida3,26,5)
#Mesa.escribirMensaje(Bienvenida4,16,6)
#Mesa.escribirMensaje(Bienvenida5,20,7)
#Mesa.escribirMensaje(Bienvenida6,29,8)
#Mesa.escribirMensaje(Bienvenida7,17,9)




#Mesa.borrarZona(0,0,79,19)
#Mesa.dibujarBorde(0,0,79,19)
#def all_in_anm():
#    Mesa.borrarZona(32,13,16,5)
#    print(Mesa)
#    sleep(0.3)
#    Mesa.escribirMensaje('***** *    *    ',33,13)
#    Mesa.escribirMensaje('*   * *    *    ',33,14)
#    Mesa.escribirMensaje('***** *    *    ',33,15)
#    Mesa.escribirMensaje('*   * *    *    ',33,16)
#    Mesa.escribirMensaje('*   * **** **** ',33,17)
#    print(Mesa)
#    sleep(0.6)
#    Mesa.borrarZona(32,13,16,5)
#    print(Mesa)
#    sleep(0.3)
#    Mesa.escribirMensaje('*** *   *  |',34,13)
#    Mesa.escribirMensaje(' *  **  *  |',34,14)
#    Mesa.escribirMensaje(' *  * * *  |',34,15)
#    Mesa.escribirMensaje(' *  *  **   ',34,16)
#    Mesa.escribirMensaje('*** *   *  *',34,17)
#    print(Mesa)
#    sleep(0.6)
#    Mesa.borrarZona(32,13,16,5)
#    print(Mesa)


#all_in_anm()



#print(Mesa)
Mesaguia=Tablero()
mazo=Baraja()
Mesaguia.dibujarBorde(0,0,79,19)
cartita=mazo.obtenerCarta()
cartita.definirEstado('oculto')
Mesaguia.dibujarCarta(cartita,32,8)
cartita.definirEstado('visible')
Mesaguia.dibujarCarta(cartita,35,10)

Mesaguia.escribirMensaje('Procura que este rectangulo se vea completo,',17,4)
Mesaguia.escribirMensaje('los bordes laterales y superior deben calzar con los del modulo de ejecucion',2,5)
print(Mesaguia)
