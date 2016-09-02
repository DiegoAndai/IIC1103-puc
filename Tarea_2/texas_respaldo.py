from poker import Carta, Tablero, Baraja
from poker import obtenerApuestaRobot, compararJugadas
from time import sleep
from random import randint

Mesa=Tablero()  #tablero de todo el juego

def anm1(lista,x,largo_goma,tablero):  #animacion inicial 1
    for i in range (0,7):
        tablero.escribirMensaje(lista[i],x,i+3)
    print (tablero)
    sleep(0.6)
    for i in range (0,7):
        tablero.borrarZona(x,i+3,largo_goma,1)
    print(tablero)
    sleep(0.4)

def anm2(lista,x,largo_goma,tablero): #animacion inicial 2
    for i in range(0,7):
        tablero.escribirMensaje(lista[i],x,i+3)
        sleep(0.09)
        print (tablero)
    for i in range (0,7):
        tablero.borrarZona(x,i+3,largo_goma,1)
        sleep(0.09)
        print(tablero)

def all_in_anm(juego):  #animacion all in!
    juego.tablero.borrarZona(32,13,16,5)
    print(Mesa)
    sleep(0.3)
    juego.tablero.escribirMensaje('***** *    *    ',33,13)
    juego.tablero.escribirMensaje('*   * *    *    ',33,14)
    juego.tablero.escribirMensaje('***** *    *    ',33,15)
    juego.tablero.escribirMensaje('*   * *    *    ',33,16)
    juego.tablero.escribirMensaje('*   * **** **** ',33,17)
    print(juego.tablero)
    sleep(0.6)
    juego.tablero.borrarZona(32,13,16,5)
    print(juego.tablero)
    sleep(0.3)
    juego.tablero.escribirMensaje('*** *   *  |',34,13)
    juego.tablero.escribirMensaje(' *  **  *  |',34,14)
    juego.tablero.escribirMensaje(' *  * * *  |',34,15)
    juego.tablero.escribirMensaje(' *  *  **   ',34,16)
    juego.tablero.escribirMensaje('*** *   *  *',34,17)
    print(juego.tablero)
    sleep(0.6)
    juego.tablero.borrarZona(32,13,16,5)
    print(juego.tablero)
    sleep(0.3)

def ronda(juego,carta):  #control mensajes y apuestas por ronda, parametros juego y carta siguiente a mostrar
    juego.pedir_apuestas(carta)
    if juego.robot.retirarse:
        juego.tablero.borrarZona(32,13,16,5)
        juego.tablero.escribirMensaje('Tu contrincante',33,13)
        juego.tablero.escribirMensaje('se retira!',36,14)
        juego.tablero.escribirMensaje('Te llevas:',36,16)
        juego.tablero.escribirMensaje('$'+str(juego.humano.apuesta+juego.robot.apuesta+juego.apuesta_mano),((16-len('$'+str(juego.humano.apuesta+juego.robot.apuesta+juego.apuesta_mano))//2)+24),17)
        print(juego.tablero)
    elif juego.humano.retirarse:
        juego.tablero.borrarZona(32,13,16,5)
        juego.tablero.escribirMensaje('Te has retirado',33,13)
        juego.tablero.escribirMensaje('Tu oponente',35,15)
        juego.tablero.escribirMensaje('se  lleva:',36,16)
        juego.tablero.escribirMensaje('$'+str(juego.humano.apuesta+juego.robot.apuesta+juego.apuesta_mano),((16-len('$'+str(juego.humano.apuesta+juego.robot.apuesta+juego.apuesta_mano))//2)+24),17)
        print(juego.tablero)
    juego.tablero.borrarZona(0,5,15,1)
    juego.tablero.borrarZona(65,5,14,1)

def seguir(juego):   #pregunta si el usuario quiere continuar jugando
    juego.tablero.borrarZona(32,13,16,5)
    juego.limpiar_tablero()
    seguir=input('Quieres seguir jugando? (si/no): ')
    while seguir!='no' and seguir!='si':
        seguir=input('\nQuieres seguir jugando? (si/no): ')
    if seguir=='no':
        juego.tablero.escribirMensaje('Te llevas $'+str(juego.humano.dinero)+', hasta la proxima',((81-len('Te llevas $'+str(juego.humano.dinero)+', hasta la proxima'))//2),6)
        print(juego.tablero)
        return False
    return True

def suspenso(tiempo,juego):   #animacion suspenso
    juego.tablero.borrarZona(32,13,16,5)
    juego.tablero.escribirMensaje('Suspenso',34,15)
    print(juego.tablero)
    puntitos='.'
    for i in range(0,5):
        sleep(tiempo)
        juego.tablero.escribirMensaje(puntitos,42+i,15)
        print(juego.tablero)
        sleep(tiempo)

class jugador_humano:    #clase controla al usuario como jugador

    def __init__(self,dinero,tablero):
        self.dinero=dinero
        self.cartas=[]
        self.apuesta=0
        self.tablero=tablero
        self.posicioncartas=[[7,12],[16,12]]
        self.tablero.escribirMensaje(str(self.dinero),5,9)
        self.retirarse=False
        self.all_in=False

    def iniciar_mano(self):
        self.cartas=[]
        self.apuesta=0
        self.retirarse=False

    def recibir_dinero(self,ganancia):
        self.dinero += ganancia
        self.tablero.borrarZona(5,9,10,1)
        self.tablero.escribirMensaje(str(self.dinero),5,9)

    def apostar(self,apuesta_superar):
        apuesta=input('Cuanto deseas apostar? ("r":retirarse,"all in":apostar todo,"0":paso): $')
        if apuesta=='r':
            self.retirarse=True
        elif apuesta=='all in':
            self.all_in=True
            return self.apuesta
        else:
            apuesta=int(apuesta)
            while apuesta>self.dinero or apuesta<apuesta_superar:
                print ('la apuesta no es valida, porfavor ingresa una apuesta menor o igual a tu dinero, que supere o iguale la apuesta actual',end='')
                apuesta=int(input(': '))
            self.dinero += -(apuesta)
            self.apuesta += apuesta
            self.tablero.borrarZona(5,9,10,1)
            self.tablero.escribirMensaje(str(self.dinero),5,9)
            self.tablero.escribirMensaje('$'+str(self.apuesta),((7-len('$'+str(self.apuesta))//2)),5)
            return apuesta

    def entregar_cartas(self):
        return self.cartas

class jugador_robot:    #clase controla al robot como jugador

    def __init__(self,dinero,tablero):
        self.dinero=dinero
        self.cartas=[]
        self.apuesta=0
        self.tablero=tablero
        self.posicioncartas=[[57,12],[66,12]]
        self.tablero.escribirMensaje(str(self.dinero),69,9)
        self.retirarse=False

    def iniciar_mano(self):
        self.cartas=[]
        self.apuesta=0
        self.retirarse=False

    def recibir_dinero(self,ganancia):
        self.dinero += ganancia
        self.tablero.borrarZona(69,9,10,1)
        self.tablero.escribirMensaje(str(self.dinero),69,9)

    def apostar(self,cartas_mesa,apuesta_superar):
        apuesta=obtenerApuestaRobot(self.cartas,cartas_mesa,self.dinero,self.apuesta,apuesta_superar)
        if apuesta==0:
            self.tablero.borrarZona(69,9,10,1)
            self.tablero.escribirMensaje(str(self.dinero),69,9)
            self.tablero.escribirMensaje('$'+str(self.apuesta),((72-len('$'+str(self.apuesta))//2)),5)
            return apuesta
        else:
            self.dinero += -(apuesta)
            self.apuesta += apuesta
            self.tablero.borrarZona(69,9,10,1)
            self.tablero.escribirMensaje(str(self.dinero),69,9)
            self.tablero.escribirMensaje('$'+str(self.apuesta),((72-len('$'+str(self.apuesta))//2)),5)
            return apuesta

    def entregar_cartas(self):
        self.cartas[0].definirEstado('visible')
        self.cartas[1].definirEstado('visible')
        self.tablero.dibujarCarta(self.cartas[0],self.posicioncartas[0][0],self.posicioncartas[0][1])
        self.tablero.dibujarCarta(self.cartas[1],self.posicioncartas[1][0],self.posicioncartas[1][1])
        print (self.tablero)

class control_juego:    #clase contiene atributos del juego

    def __init__(self,tablero,jugador_humano,jugador_robot):
        self.tablero=tablero
        self.humano=jugador_humano
        self.robot=jugador_robot
        self.mazo=Baraja()
        self.apuesta_mano=0
        self.cartas_visibles=[]
        self.cartas_mesa_ocultas=[]

    def comenzar_mano(self):
        self.all_in=False
        self.mazo.barajar()
        self.apuesta_mano=0
        self.humano.iniciar_mano()
        self.robot.iniciar_mano()
        self.tablero.escribirMensaje('Apuesta actual:',33,16)
        self.tablero.escribirMensaje('Pozo acumulado:',33,13)
        self.tablero.borrarZona(0,4,15,1)
        self.tablero.borrarZona(65,4,14,1)
        self.cartas_mesa_ocultas=[[18,3],[27,3],[36,3],[45,3],[54,3]]
        self.cartas_visibles=[]
        self.humano.cartas.append(self.mazo.obtenerCarta())
        self.robot.cartas.append(self.mazo.obtenerCarta())
        self.humano.cartas.append(self.mazo.obtenerCarta())
        self.robot.cartas.append(self.mazo.obtenerCarta())
        for carta in self.robot.cartas:
            carta.definirEstado('oculto')
        for posicion in self.cartas_mesa_ocultas:
            posicion.insert(0,self.mazo.obtenerCarta())
            posicion[0].definirEstado('oculto')

    def repartir_animado(self,retardo):
        self.cartas_iniciales=[[self.humano.cartas[0],self.humano.posicioncartas[0][0],self.humano.posicioncartas[0][1]], \
                            [self.robot.cartas[0],self.robot.posicioncartas[0][0],self.robot.posicioncartas[0][1]], \
                            [self.humano.cartas[1],self.humano.posicioncartas[1][0],self.humano.posicioncartas[1][1]],  \
                            [self.robot.cartas[1],self.robot.posicioncartas[1][0],self.robot.posicioncartas[1][1]], \
                            self.cartas_mesa_ocultas[0], self.cartas_mesa_ocultas[1],self.cartas_mesa_ocultas[2],   \
                            self.cartas_mesa_ocultas[3],self.cartas_mesa_ocultas[4]]
        self.limpiar_tablero()
        print(self.tablero)
        for carta in self.cartas_iniciales:
            sleep(retardo)
            self.tablero.dibujarCarta(carta[0],carta[1],carta[2])
            print (self.tablero)
            sleep(retardo)

    def mostrar_mesa_animado(self,carta_inicio,carta_fin,retardo_prog): #se que no habia que entregar todas las cartas de una, pero lo hice asi en honor a que con mis abuelos
        if carta_inicio>carta_fin:                                      #jugabamos de esta forma, de todas formas las "cartas visibles" se van entregando de la manera que se pide
            return                                                      #esto esta implementado en este metodo, cambiando el rango de las cartas a "mostrar" de 1,3, a 4,4, y
        for i in range (carta_inicio-1,carta_fin):                      #finalmente 5,5, haciendo visibles 3, 1 y 1 cartas respectivamente.
            self.cartas_mesa_ocultas[i][0].definirEstado('visible')
            self.cartas_visibles.append(self.cartas_mesa_ocultas[i][0])
            self.tablero.dibujarCarta(self.cartas_visibles[i],self.cartas_mesa_ocultas[i][1],self.cartas_mesa_ocultas[i][2])
            sleep(retardo_prog+i/7)
            print(self.tablero)

    def limpiar_tablero(self):
        self.tablero.borrarZona(16,3,48,7)
        self.tablero.borrarZona(6,12,19,7)
        self.tablero.borrarZona(56,12,19,7)
        self.tablero.borrarZona(38,14,11,1)

    def pedir_apuestas(self,carta):
        self.humano.apuesta=0
        self.robot.apuesta=0
        if self.humano.dinero==0:
            print('No tienes mas dinero, la apuesta queda hasta aqui.')
            input('presiona Enter para continuar')
            self.all_in=True
            self.humano.apuesta=self.humano.dinero
            self.robot.dinero += (self.robot.apuesta-self.humano.apuesta)
            self.robot.apuesta=self.humano.apuesta
            self.tablero.escribirMensaje(str(self.robot.dinero),69,9)
            print(self.tablero)
            self.mostrar_mesa_animado(carta,5,0.2)
            return
        self.tablero.escribirMensaje('Tu apuesta:',2,4)
        self.tablero.escribirMensaje('Su apuesta:',67,4)
        self.humano.apostar(0)
        if self.humano.all_in:
            if self.robot.dinero<self.humano.dinero:
                self.humano.all_in=False
                print('No puedes hacer un all in si tu contrincante tiene menos dinero.')
                self.humano.apostar(0)
            else:
                if self.robot.apuesta==0:
                    self.tablero.borrarZona(5,9,10,1)
                    self.tablero.borrarZona(69,9,10,1)
                    self.tablero.escribirMensaje(str(self.robot.dinero),69,9)
                    self.tablero.escribirMensaje(str(self.humano.dinero),5,9)
                    self.robot.retirarse=True
                else:
                    all_in_anm(self)
                    self.all_in=True
                    self.humano.apuesta+=self.humano.dinero
                    self.humano.dinero=0
                    self.robot.dinero += (self.robot.apuesta-self.humano.apuesta)
                    self.robot.apuesta=self.humano.apuesta
                    self.apuesta_mano += (self.humano.apuesta+self.robot.apuesta)
                    self.tablero.borrarZona(0,5,15,1)
                    self.tablero.borrarZona(65,5,14,1)
                    self.tablero.borrarZona(5,9,10,1)
                    self.tablero.borrarZona(69,9,10,1)
                    self.tablero.escribirMensaje(str(self.robot.dinero),69,9)
                    self.tablero.escribirMensaje(str(self.humano.dinero),5,9)
                    self.tablero.escribirMensaje('$'+str(self.humano.apuesta),((7-len('$'+str(self.humano.apuesta))//2)),5)
                    self.tablero.escribirMensaje('$'+str(self.robot.apuesta),((72-len('$'+str(self.robot.apuesta))//2)),5)
                    print(self.tablero)
                    self.mostrar_mesa_animado(carta,5,0.2)
                    return
        self.tablero.escribirMensaje('$'+str(self.humano.apuesta),38,17)
        print(self.tablero)
        while not self.humano.retirarse and not self.robot.retirarse:
            if self.robot.dinero<self.humano.apuesta and randint(0,50)<5: #implementado para que a veces el robot decida hacer all in
                all_in_anm(self)
                self.tablero.borrarZona(32,13,16,5)
                self.tablero.escribirMensaje('Tu contrincante',33,14)
                self.tablero.escribirMensaje('limita la',36,15)
                self.tablero.escribirMensaje('apuesta, no',35,16)
                self.tablero.escribirMensaje('tiene mas dinero',32,17)
                self.all_in=True
                self.robot.apuesta+=self.robot.dinero
                self.robot.dinero=0
                self.humano.dinero += (self.humano.apuesta-self.robot.apuesta)
                self.humano.apuesta=self.robot.apuesta
                self.apuesta_mano += (self.humano.apuesta+self.robot.apuesta)
                self.tablero.borrarZona(0,5,15,1)
                self.tablero.borrarZona(65,5,14,1)
                self.tablero.borrarZona(5,9,10,1)
                self.tablero.borrarZona(69,9,10,1)
                self.tablero.escribirMensaje(str(self.robot.dinero),69,9)
                self.tablero.escribirMensaje(str(self.humano.dinero),5,9)
                self.tablero.escribirMensaje('$'+str(self.humano.apuesta),((7-len('$'+str(self.humano.apuesta))//2)),5)
                self.tablero.escribirMensaje('$'+str(self.robot.apuesta),((72-len('$'+str(self.robot.apuesta))//2)),5)
                print(self.tablero)
                input('presiona Enter para continuar')
                self.mostrar_mesa_animado(carta,5,0.2)
                return
            self.robot.apostar(self.cartas_visibles,self.humano.apuesta)
            if self.robot.apuesta==0 and not self.humano.apuesta==0:
                self.tablero.borrarZona(5,9,10,1)
                self.tablero.borrarZona(69,9,10,1)
                self.tablero.escribirMensaje(str(self.robot.dinero),69,9)
                self.tablero.escribirMensaje(str(self.humano.dinero),5,9)
                self.robot.retirarse=True
            self.tablero.escribirMensaje('$'+str(self.robot.apuesta),38,17)
            print(self.tablero)
            if self.robot.apuesta==self.humano.apuesta:
                self.tablero.borrarZona(32,13,16,5)
                self.tablero.escribirMensaje('Tu contrincante',33,14)
                self.tablero.escribirMensaje('ha igualado la',34,15)
                self.tablero.escribirMensaje('apuesta',37,16)
                print(self.tablero)
                sleep(1.5)
                self.tablero.borrarZona(32,13,16,5)
                self.tablero.escribirMensaje('Apuesta actual:',33,16)
                self.tablero.escribirMensaje('Pozo acumulado:',33,13)
                self.tablero.escribirMensaje('$'+str(self.robot.apuesta),38,17)
                if self.apuesta_mano!=0:
                    self.tablero.escribirMensaje('$'+str(self.apuesta_mano),38,14)
                print(self.tablero)
                break
            elif self.robot.retirarse:
                break
            else:
                self.tablero.borrarZona(32,13,16,5)
                self.tablero.escribirMensaje('Tu contrincante',33,14)
                self.tablero.escribirMensaje('ha subido la',35,15)
                self.tablero.escribirMensaje('apuesta',37,16)
                print(self.tablero)
                sleep(1.5)
                self.tablero.borrarZona(32,13,16,5)
                self.tablero.escribirMensaje('Apuesta actual:',33,16)
                self.tablero.escribirMensaje('Pozo acumulado:',33,13)
                self.tablero.escribirMensaje('$'+str(self.robot.apuesta),38,17)
                if self.apuesta_mano!=0:
                    self.tablero.escribirMensaje('$'+str(self.apuesta_mano),38,14)
                print(self.tablero)
            if self.humano.dinero<=self.robot.apuesta-self.humano.apuesta:
                apostar_todo=input('Decide: hacer un all in para limitar la apuesta y jugar la mano, o retirarte.\n(all in/retirarse): ')
                while apostar_todo!='all in' and apostar_todo!='retirarse':
                    apostar_todo=input('Decide: hacer un all in para limitar la apuesta y jugar la mano, o retirarte.\n(all in/retirarse): ')
                if apostar_todo=='all in':
                    all_in_anm(self)
                    self.all_in=True
                    self.humano.apuesta+=self.humano.dinero
                    self.humano.dinero=0
                    self.robot.dinero += (self.robot.apuesta-self.humano.apuesta)
                    self.robot.apuesta=self.humano.apuesta
                    self.tablero.borrarZona(0,5,15,1)
                    self.tablero.borrarZona(65,5,14,1)
                    self.tablero.borrarZona(5,9,10,1)
                    self.tablero.borrarZona(69,9,10,1)
                    self.tablero.escribirMensaje(str(self.robot.dinero),69,9)
                    self.tablero.escribirMensaje(str(self.humano.dinero),5,9)
                    self.tablero.escribirMensaje('$'+str(self.humano.apuesta),((7-len('$'+str(self.humano.apuesta))//2)),5)
                    self.tablero.escribirMensaje('$'+str(self.robot.apuesta),((72-len('$'+str(self.robot.apuesta))//2)),5)
                    print(self.tablero)
                    self.mostrar_mesa_animado(carta,5,0.2)
                if apostar_todo=='retirarse':
                    self.humano.retirarse=True
            else:
                print('(En tu apuesta, ingresa $'+str(self.robot.apuesta-self.humano.apuesta)+' para igualar)')
                self.humano.apostar(self.robot.apuesta-self.humano.apuesta)
                self.tablero.escribirMensaje('$'+str(self.humano.apuesta),38,17)
            if self.robot.apuesta==self.humano.apuesta or self.humano.retirarse:
                break
        if self.robot.retirarse:
            self.humano.recibir_dinero(self.humano.apuesta+self.robot.apuesta+self.apuesta_mano)
        elif self.humano.retirarse:
            self.robot.recibir_dinero(self.humano.apuesta+self.robot.apuesta+self.apuesta_mano)
        else:
            self.apuesta_mano += (self.humano.apuesta+self.robot.apuesta)
            self.tablero.escribirMensaje('$'+str(self.apuesta_mano),38,14)
            self.tablero.borrarZona(38,17,11,1)
        print(self.tablero)

    def repartija(self,respuesta_compararjugadas):
        if respuesta_compararjugadas=='gana_humano':
            self.humano.recibir_dinero(self.apuesta_mano)
            self.tablero.borrarZona(32,13,16,5)
            self.tablero.escribirMensaje('Ganaste!',37,14)
            self.tablero.escribirMensaje('Te llevas:',36,15)
            self.tablero.escribirMensaje('$'+str(self.apuesta_mano),((16-len('$'+str(self.apuesta_mano))//2)+24),16)
            print(self.tablero)
        elif respuesta_compararjugadas=='gana_robot':
            self.robot.recibir_dinero(self.apuesta_mano)
            self.tablero.borrarZona(32,13,16,5)
            self.tablero.escribirMensaje('Has perdido',35,14)
            self.tablero.escribirMensaje('Tu oponente',35,15)
            self.tablero.escribirMensaje('se  lleva:',36,16)
            self.tablero.escribirMensaje('$'+str(self.apuesta_mano),((16-len('$'+str(self.apuesta_mano))//2)+24),17)
            print(self.tablero)

        elif respuesta_compararjugadas=='empate':
            self.robot.recibir_dinero(self.apuesta_mano//2)
            self.humano.recibir_dinero(self.apuesta_mano//2)
            self.tablero.borrarZona(32,13,16,5)
            self.tablero.escribirMensaje('Empate!',37,14)
            self.tablero.escribirMensaje('Cada  uno',36,15)
            self.tablero.escribirMensaje('se lleva:',36,16)
            self.tablero.escribirMensaje('$'+str(self.apuesta_mano//2),((16-len('$'+str(self.apuesta_mano//2))//2)+24),17)
            print(self.tablero)

def setear_mesa_y_juego(Mesa):   #setea los graficos iniciales y crea los objetos jugador humano y jugador robot

    bordes=[[30,0,19,2],[15,2,49,8],[5,11,20,8],[55,11,20,8],[31,12,18,6]]
    for borde in bordes:
        Mesa.dibujarBorde(borde[0],borde[1],borde[2],borde[3])
    mensajes_iniciales=[["  Texas  Hold'em  ",31,1],[' Cartas en mesa ',32,10],[' Tus cartas ',5,19],[' Contrincante ',62,19],['$:',3,9],['$:',67,9],\
                        ["Bienvenido a Texas Hold'em, en este juego de",18,3],["cartas debes formar la mejor combinacion posible",16,4],['ocupando tus cartas y las de la mesa.',21,5],\
                        ["En cada ronda se da vuelta un numero de cartas",17,6],["y se debe apostar, ten en cuenta que cuando se",17,7],["pida igualar la apuesta del contrincante,  debes",16,8],\
                        ["ingresar lo que te falta y no la apuesta total.",17,9]]
    for mensaje in mensajes_iniciales:
        Mesa.escribirMensaje(mensaje[0],mensaje[1],mensaje[2])
    print (Mesa)

    texas=['******* ****** *     * ****** ******','   *    *       *   *  *    * *     ','   *    *        * *   *    * *     ',   \
           '   *    ******    *    ****** ******','   *    *        * *   *    *      *','   *    *       *   *  *    *      *',   \
           '   *    ****** *     * *    * ******']

    holdem=['*    * ****** *     ****    * ****** *     *','*    * *    * *     *   *   * *      **   **','*    * *    * *     *    *  * *      * * * *',\
            '****** *    * *     *    *    ****** *  *  *','*    * *    * *     *    *    *      *     *','*    * *    * *     *   *     *      *     *',\
            '*    * ****** ***** ****      ****** *     *']

    input('Comandos especiales: en la apuesta, ingresar "all in" despues del signo $\nsignifica apostar todo tu dinero, en el mismo lugar, si ingresas 0, significa\nque no aumentas la apuesta. Enter para continuar')
    Mesa.borrarZona(16,3,48,7)

    Instruccion1=[['Este juego contiene simples y modestas',21,3],['animaciones, que estan probadas en la Terminal',17,4],['del sistema operativo Ubuntu.',26,5],\
                    ['Si esta corriendo este programa en otra interfaz',16,6],['como IDLE, porfavor ajuste la ventana con',20,7],['respecto a este tablero.',29,8]]
    for mensaje in Instruccion1:
        Mesa.escribirMensaje(mensaje[0],mensaje[1],mensaje[2])
    print (Mesa)
    Mesa.borrarZona(16,3,48,7)

    guia=input('Quieres una guia para ajustar el tablero? (recomendado), aparecera un borde\npara que puedas ajustar mas facilmente (si/no): ')
    while guia!='si' and guia!='no':
        guia=input('Quieres una guia para ajustar el tablero? (recomendado), aparecera un borde\npara que puedas ajustar mas facilmente (si/no): ')
    if guia=='si':    #muestra el borde para ajustar pantalla si el usuario lo requiere
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
        print('Este pedazo se ocupara para que ingreses tus apuestas, asique procura que\neste mensaje tambien se vea correctamente hasta la siguiente linea\n(Enter para continuar)',end='')
        input('')
        bordes=[[30,0,19,2],[15,2,49,8],[5,11,20,8],[55,11,20,8],[31,12,18,6]]
        for borde in bordes:
            Mesa.dibujarBorde(borde[0],borde[1],borde[2],borde[3])
        mensajes_iniciales=[["  Texas  Hold'em  ",31,1],[' Cartas en mesa ',32,10],[' Tus cartas ',5,19],[' Contrincante ',62,19],['$:',3,9],['$:',67,9]]
        for mensaje in mensajes_iniciales:
            Mesa.escribirMensaje(mensaje[0],mensaje[1],mensaje[2])
        print(Mesa)


    anm1(texas,22,36,Mesa)
    anm1(holdem,18,45,Mesa)
    anm2(texas,22,36,Mesa)
    anm2(holdem,18,45,Mesa)

    josesita=jugador_humano(1000,Mesa)
    dieguits=jugador_robot(1000,Mesa)
    juego=control_juego(Mesa,josesita,dieguits)

sleep(0.5)
while juego.humano.dinero>10:
    juego.comenzar_mano()
    juego.repartir_animado(0.2)
    ronda(juego,1)
    if juego.all_in:
        suspenso(0.3,juego)
        juego.robot.entregar_cartas()
        juego.repartija(compararJugadas(juego.humano.cartas,juego.robot.cartas,juego.cartas_visibles))
        input('presiona Enter para continuar')
        if juego.humano.dinero==0 or juego.robot.dinero==0 or not seguir(juego):
            break
        continue
    if juego.robot.retirarse or juego.humano.retirarse:
        if juego.robot.dinero==0 or juego.humano.dinero==0 or not seguir(juego):
            break
        continue
    juego.mostrar_mesa_animado(1,3,0.7)
    ronda(juego,4)
    if juego.all_in:
        suspenso(0.3,juego)
        juego.robot.entregar_cartas()
        juego.repartija(compararJugadas(juego.humano.cartas,juego.robot.cartas,juego.cartas_visibles))
        input('presiona Enter para continuar')
        if juego.humano.dinero==0 or juego.robot.dinero==0 or not seguir(juego):
            break
        continue
    if juego.robot.retirarse or juego.humano.retirarse:
        if juego.robot.dinero==0 or juego.humano.dinero==0 or not seguir(juego):
            break
        continue
    juego.mostrar_mesa_animado(4,4,0.7)
    ronda(juego,5)
    if juego.all_in:
        suspenso(0.3,juego)
        juego.robot.entregar_cartas()
        juego.repartija(compararJugadas(juego.humano.cartas,juego.robot.cartas,juego.cartas_visibles))
        input('presiona Enter para continuar')
        if juego.humano.dinero==0 or juego.robot.dinero==0 or not seguir(juego):
            break
        continue
    if juego.robot.retirarse or juego.humano.retirarse:
        if not juego.all_in and (juego.robot.dinero==0 or juego.humano.dinero==0 or not seguir(juego)):
            break
        continue
    juego.mostrar_mesa_animado(5,5,0.8)
    ronda(juego,6)
    if juego.all_in:
        suspenso(0.3,juego)
        juego.robot.entregar_cartas()
        juego.repartija(compararJugadas(juego.humano.cartas,juego.robot.cartas,juego.cartas_visibles))
        if juego.humano.dinero==0 or juego.robot.dinero==0 or not seguir(juego):
            break
        continue
    if juego.robot.retirarse or juego.humano.retirarse:
        if not juego.all_in and (juego.robot.dinero==0 or juego.humano.dinero==0 or not seguir(juego)):
            break
        continue
    else:
        suspenso(0.3,juego)
        juego.robot.entregar_cartas()
        juego.repartija(compararJugadas(juego.humano.cartas,juego.robot.cartas,juego.cartas_visibles))
        if not juego.all_in and (juego.robot.dinero==0 or juego.humano.dinero==0 or not seguir(juego)):
            break
    juego.limpiar_tablero()
    print(juego.tablero)

if juego.robot.dinero==0:
    juego.tablero.borrarZona(0,4,15,1)
    juego.tablero.borrarZona(65,4,14,1)
    juego.tablero.borrarZona(32,13,16,5)
    juego.limpiar_tablero()
    juego.tablero.escribirMensaje('Tu oponente se ha quedado sin dinero asique',20,5)
    juego.tablero.escribirMensaje('el juego ha acabado.',30,6)
    juego.tablero.escribirMensaje('Te llevas $'+str(juego.humano.dinero)+', hasta la proxima',((81-len('Te llevas $'+str(juego.humano.dinero)+', hasta la proxima'))//2),7)
    print(juego.tablero)

if juego.humano.dinero==0:
    juego.tablero.borrarZona(0,4,15,1)
    juego.tablero.borrarZona(65,4,14,1)
    juego.tablero.borrarZona(32,13,16,5)
    juego.limpiar_tablero()
    juego.tablero.escribirMensaje('Te has quedado sin dinero, el juego ha acabado.',17,6)
    print(juego.tablero)

if juego.humano.dinero<10 and not juego.humano.dinero==0:
    juego.tablero.borrarZona(0,4,15,1)
    juego.tablero.borrarZona(65,4,14,1)
    juego.tablero.borrarZona(32,13,16,5)
    juego.limpiar_tablero()
    juego.tablero.escribirMensaje('Te has quedado con menos de $10,',25,5)
    juego.tablero.escribirMensaje('el juego ha acabado.',31,6)
    juego.tablero.escribirMensaje('Te llevas $'+str(juego.humano.dinero)+', hasta la proxima',((81-len('Te llevas $'+str(juego.humano.dinero)+', hasta la proxima'))//2),7)
    print(juego.tablero)
