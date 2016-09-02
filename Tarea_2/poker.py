# -*- coding: utf-8 -*-

import os
import sys
import math
import random
import time

# drawings
if 'cp850' in sys.stdin.encoding or 'windows-1252' in sys.stdin.encoding:
    if 'cp850' in sys.stdout.encoding:
        drC = chr(3)
        drD = chr(4)
        drT = chr(5)
        drP = chr(6)
    else:
        drC = 'C'
        drD = 'T'
        drT = 'D'
        drP = 'P'
    ltc = '+'
    rtc = '+'
    lbc = '+'
    rbc = '+'
    lr = '|'
    td = '-'
    dSy = 'D'
    hiddenc = chr(16)
else:
    drC = '\u2665'
    drD = '\u2666'
    drT = '\u2663'
    drP = '\u2660'
    ltc = '\u250C'
    rtc = '\u2510'
    lbc = '\u2514'
    rbc = '\u2518'
    lr = '\u2502'
    td = '\u2500'
    dSy = '\u24B9'
    hiddenc = '\u2573'

# manejo basico de excepciones para errores de datos de entrada
class PokerError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return repr(self.__value)

# La clase Carta controla las operaciones de una carta, en setear su valor y dibujarla.
# Tambien entrega su estado mediante un numero (carta entre 0 y 52)
#
# palos (string):
#   C -> corazon
#   P -> pica
#   T -> trebol
#   D -> diamante
#
# valores (string) {'2','3',...,'10','J','Q','K','A'}

class Carta:
    # tamaño de la carta en 'espacios de caracter'
    __height = 7
    __width = 8
    __hiddenchar = hiddenc

    # Constructor
    def __init__(self):
        #card_canvas es donde se dibuja la carta
        self.__card_canvas = ['']*self.__height
        for i in range(self.__height):
            self.__card_canvas[i] = [' ']*self.__width
        # crear el borde de la carta
        self.__draw_border()

        # palos (suits)
        self.__draws = {'C':drC, 'P':drP, 'T':drT, 'D':drD}

        self.__suitvec = ['C','P','T','D']
        self.__valuevec = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

        # valores predeterminados
        self.__idcard = 0
        self.__suit = 'C'
        self.__value = '2'

        # estado del dorso de la carta: 'oculto', 'visible'
        self.__statuslist = ['oculto','visible']
        self.__status = 'visible'

    def obtenerPalo(self):
        return self.__suit
    def obtenerValor(self):
        return self.__value
    def obtenerDimensiones(self):
        return self.__width, self.__height
    def definirEstado(self,status):
        if status not in self.__statuslist:
            raise PokerError('\'status\' debe ser uno de ' + str(self.__statuslist))
        self.__status = status
    def obtenerEstado(self):
        return self.__status

    def val_index(self):
        return self.__valuevec.index(self.obtenerValor())

    def suit_index(self):
        return self.__suitvec.index(self.obtenerPalo())

    # setea el valor de la carta por id
    def set_by_id(self, id, status='visible'):
        # check value
        try:
            val = int(id)
            if val < 0 or val > 51:
                raise ValueError()
        except ValueError:
            raise PokerError('id debe ser un numero entre 0 y 51')

        idsuit = val // 13
        idvalue = val % 13

        self.__set_by_suit_value(self.__suitvec[idsuit],self.__valuevec[idvalue], status)
    
    # setea el valor de la carta por palo y valor
    def __set_by_suit_value(self,suit='C',value='A', status='visible'):

        #check values
        if suit not in self.__suitvec:
            raise PokerError('\'suit\' debe ser \'C\', \'P\', \'T\' o \'D\'')
        if value.isdigit() == False and (len(value) > 1 or value not in self.__valuevec):
            raise PokerError('\'value\' debe ser \'A\', \'J\', \'Q\' o \'K\' si no es numero')
        if value.isdigit() and (int(value)>10 or int(value)<2):
            raise PokerError('\'value\' debe ser un entero entre 2 y 10 cuando es numerico')

        # cambio palo y valor en la carta
        self.__suit = suit
        self.__value = value
        self.__idcard = self.__suitvec.index(suit)*13 + self.__valuevec.index(value)
        self.definirEstado(status)
        
    def __draw_show(self):
        for x in range(1,self.__width-1):
            for y in range(1,self.__height-1):
                self.__card_canvas[y][x] = ' '

        # centro de la carta en (wc, hc)
        wc = (self.__width-1) // 2
        hc = (self.__height-1) // 2

        # dibujo figura central
        self.__card_canvas[hc][wc] = self.__draws[self.__suit]

        #dibujo valor de la carta en dos esquinas
        if len(self.__value) == 1:
            value1 = self.__value + ' '
            value2 = ' ' + self.__value
        else:
            value1 = self.__value
            value2 = self.__value
        self.__card_canvas[1][1] = value1[0]
        self.__card_canvas[1][2] = value1[1]
        self.__card_canvas[self.__height-2][self.__width-3] = value2[0]
        self.__card_canvas[self.__height-2][self.__width-2] = value2[1]

    def __draw_hide(self):
        for x in range(1,self.__width-1):
            for y in range(1,self.__height-1):
                self.__card_canvas[y][x] = self.__hiddenchar

    def __draw_border(self):
        self.__card_canvas[0][0] = ltc
        self.__card_canvas[self.__height-1][0] = lbc
        self.__card_canvas[0][self.__width-1] = rtc
        self.__card_canvas[self.__height-1][self.__width-1] = rbc
        for x in range(1,self.__width-1):
            self.__card_canvas[0][x] = td
            self.__card_canvas[self.__height-1][x] = td
        for y in range(1,self.__height-1):
            self.__card_canvas[y][0] = lr
            self.__card_canvas[y][self.__width-1] = lr

    def draw(self, canvas, place):
        if self.__status == 'oculto':
            self.__draw_hide()
        elif self.__status == 'visible':
            self.__draw_show()
        for y in range(self.__height):
            for x in range(self.__width):
                canvas[place[1]+y][place[0]+x] = self.__card_canvas[y][x]


# Baraja controla las acciones de barajar y entregar una carta a la vez.
class Baraja():
    def __init__(self):
        self.barajar()

    def barajar(self):
        self.num_picked = 0
        self.__picked = [0]*52

    def obtenerCarta(self):
        # obtiene el indice de la siguiente carta si es que la baraja
        # tiene aun cartas; si no, retorna None
        unpicked_idx = [i for i in range(len(self.__picked)) if self.__picked[i] == 0]
        if len(unpicked_idx) == 0:
            print("WARNING: la baraja se ha vaciado")
            return None
        pick = unpicked_idx[random.randint(0,len(unpicked_idx)-1)]
        self.__picked[pick] = 1
        self.num_picked += 1
        new_card = Carta()
        new_card.set_by_id(pick)
        return new_card

# Tablero es solo para manejar la prehistorica "grafica"
class Tablero():
    
    def __init__(self, num_players=2,width=80, height=20):

        # ancho y altura de zona de dibujo
        self.__width= width
        self.__height = height

        # mensajes que serán desplegados en la zona de mensajes
        self.messages = []
        self.__table_canvas = []*9

        # table_canvas es donde se dibuja el tablero
        self.__table_canvas = []
        # inicializo el tablero
        self.borrarTablero()

    def __str__(self):
        # if using IDLE, do not erase window
        if 'idlelib.run' not in sys.modules: 
            if 'win' in sys.platform.lower() and 'dar' not in sys.platform.lower():
                a = os.system('cls')
            else:
                a = os.system('clear')
        
        retstr = ''
        for y in range(self.__height):
            for x in range(self.__width):
                retstr += self.__table_canvas[y][x]
                #print(self.__table_canvas[y][x],end='')
            retstr += '\n'
            #print('')
        return retstr
    
    def dibujarCarta(self, carta, x, y):
        self.__assert_place([x,y])
        self.__draw_card(carta,[x,y])
        
    def dibujarBorde(self,x,y,ancho,alto):
        self.__draw_border([x,y],[ancho,alto])
    
    def escribirMensaje(self,mensaje,x,y):
        for i,px in zip(mensaje,[x+j for j in range(len(mensaje))]):
            self.__assert_place([px,y])
            self.__table_canvas[y][px] = i
    
    def borrarZona(self,x,y,ancho,alto):
        x0 = x
        y0 = y
        x1 = x+ancho
        y1 = y+alto
        self.__assert_place([x0,y0])
        self.__assert_place([x1,y1])
        for v in range(x0,x1):
            for u in range(y0,y1):
                self.__table_canvas[u][v] = ' '
        
    def borrarTablero(self):
        self.__table_canvas = ['']*self.__height
        for y in range(self.__height):
            self.__table_canvas[y] = [' ']*self.__width

    def __assert_place(self, place):
        if not (place[0] >= 0 and place[0] < self.__width and place[1] >= 0 and place[1] < self.__height):
            if place[0] < 0:
                raise PokerError("Posicion x negativa")
            if place[0] >= self.__width:
                raise PokerError("Posicion x mayor que ancho tablero")
            if place[1] < 0:
                raise PokerError("Posicion y negativa")
            if place[1] >= self.__height:
                raise PokerError("Posicion y mayor que altura tablero")
    
    def __draw_border(self, place, size):
        x0 = place[0]
        y0 = place[1]
        x1 = place[0] + size[0]
        y1 = place[1] + size[1]
        
        self.__assert_place([x0,y0])
        self.__assert_place([x1,y1])

        self.__table_canvas[y0][x0] = ltc
        self.__table_canvas[y1][x0] = lbc
        self.__table_canvas[y0][x1] = rtc
        self.__table_canvas[y1][x1] = rbc
        for x in range(x0+1,x1):
            self.__table_canvas[y0][x] = td
            self.__table_canvas[y1][x] = td
        for y in range(y0+1,y1):
            self.__table_canvas[y][x0] = lr
            self.__table_canvas[y][x1] = lr

    def __draw_card(self, card, place):
        card.draw(self.__table_canvas, place)

############################################################################
############################################################################

def obtenerApuestaRobot(cartasRobot, cartasMesa, dinero_robot, apuesta_robot, apuesta_a_superar):
    # TODO: logica de apuesta de robot

    if random.randint(0,20) > 3: # iguala o sube, si es que tiene dinero, si n se retira.
        if apuesta_a_superar - apuesta_robot > dinero_robot:
            return 0
        if random.randint(0,10) > 2:
            return apuesta_a_superar
        else:
            return apuesta_a_superar + min(random.randint(1,100),dinero_robot-(apuesta_a_superar - apuesta_robot))
    else:
        return 0

def compararJugadas(cartasHumano, cartasRobot, cartasMesa):
    
    def get_score(cards):
        # asigno puntajes
        # *0: nada (carta mas alta)
        # *1: par
        # *2: doble par
        # *3: trio
        # *4: escalera
        # *5: color
        # *6: full
        # *7: poker
        # *8: escalera_color
        #
        # ademas retorno la lista de los valores de carta para comparar cuando hay empate.

        if len(cards) > 5:
            best_score = -1
            cards_inv = []
            for i in range(len(cards)):
                cards_red = cards[:i]+cards[i+1:]
                pp = get_score(cards_red)
                if pp[0] > best_score:
                    best_score = pp[0]
                    cards_inv = pp[1]
                elif pp[0] == best_score:
                    for i in range(min(len(cards_inv),len(pp[1]))):
                        if cards_inv[i] > pp[1][i]:
                            break
                        elif cards_inv[i] < pp[1][i]:
                            cards_inv = pp[1]
                            break
            return [best_score, cards_inv]
        else:
            row = [0]*13
            mat = [list(row) for i in range(4)]
            for card in cards:
                #print(card.suit_index(), card.val_index())
                mat[card.suit_index()][card.val_index()] += 1

            #print(mat)

            hist_vals = [0]*13
            hist_suit = [0]*4

            for j in range(4):
                for i in range(13):
                    if mat[j][i]:
                        hist_vals[i] += 1
                        hist_suit[j] += 1


            hist_sort_val = sorted(((e,i) for i,e in enumerate(hist_vals)), reverse=True)
            hist_sort_suit = sorted(((e,i) for i,e in enumerate(hist_suit)), reverse=True)

            max_score = 0
            cards_involved = []

            if (hist_sort_val[0][1] - hist_sort_val[4][1] == 4) and hist_sort_suit[0][0] == 5:
                max_score = 8
                cards_involved = [hist_sort_val[0][1]]
            elif hist_sort_val[0][0] == 4:
                max_score = 7
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1]]
            elif hist_sort_val[0][0] == 3 and hist_sort_val[1][0] == 2:
                max_score = 6
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1]]
            elif hist_sort_suit[0][0] == 5 and not (hist_sort_val[0][1] - hist_sort_val[4][1] == 4):
                max_score = 5
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1],hist_sort_val[2][1],hist_sort_val[3][1],hist_sort_val[4][1]]
            elif not (hist_sort_suit[0][0] == 5) and hist_sort_val[0][1] - hist_sort_val[4][1] == 4:
                max_score = 4
                cards_involved = [hist_sort_val[0][1]]
            elif hist_sort_val[0][0] == 3 and hist_sort_val[1][0] == 1:
                max_score = 3
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1],hist_sort_val[2][1]]
            elif hist_sort_val[0][0] == 2 and hist_sort_val[1][0] == 2:
                max_score = 2
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1],hist_sort_val[2][1]]
            elif hist_sort_val[0][0] == 2 and hist_sort_val[1][0] == 1:
                max_score = 1
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1],hist_sort_val[2][1],hist_sort_val[3][1]]
            else:
                max_score = 0
                cards_involved = [hist_sort_val[0][1],hist_sort_val[1][1],hist_sort_val[2][1],hist_sort_val[3][1],hist_sort_val[4][1]]

            return [max_score, cards_involved]
            
    if not ( type(cartasHumano) is list and type(cartasRobot) is list and type(cartasMesa) is list):
        raise PokerError("compararJugadas recibe solo argumentos de tipo lista")
    
    assert(len(cartasHumano) == 2 and len(cartasRobot) == 2 and len(cartasMesa) == 5)
    
    cardsA = cartasHumano + cartasMesa
    cardsB = cartasRobot + cartasMesa

    scA = get_score(cardsA)
    scB = get_score(cardsB)

    if scA[0] > scB[0]:
        return "gana_humano"
    elif scA[0] < scB[0]:
        return "gana_robot"
    else:
        for i in range(min(len(scA[1]),len(scB[1]))):
            if scA[1][i] > scB[1][i]:
                return "gana_humano"
            elif scA[1][i] < scB[1][i]:
                return "gana_robot"
        return "empate"
    
    

