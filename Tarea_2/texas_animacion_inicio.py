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

#linea1='******* ****** *     * ****** ******' #para este x=22 y=3,4,5,6,7,8,9
#linea2='   *    *       *   *  *    * *     '
#linea3='   *    *        * *   *    * *     '
#linea4='   *    ******    *    ****** ******'
#linea5='   *    *        * *   *    *      *'
#linea6='   *    *       *   *  *    *      *'
#linea7='   *    ****** *     * *    * ******'

#linea1_1='*    * ****** *     ****    * ****** *     *'  #para este x=18
#linea1_2='*    * *    * *     *   *   * *      **   **'
#linea1_3='*    * *    * *     *    *  * *      * * * *'
#linea1_4='****** *    * *     *    *    ****** *  *  *'
#linea1_5='*    * *    * *     *    *    *      *     *'
#linea1_6='*    * *    * *     *   *     *      *     *'
#linea1_7='*    * ****** ***** ****      ****** *     *'

texas=['******* ****** *     * ****** ******','   *    *       *   *  *    * *     ','   *    *        * *   *    * *     ',   \
       '   *    ******    *    ****** ******','   *    *        * *   *    *      *','   *    *       *   *  *    *      *',   \
       '   *    ****** *     * *    * ******']

holdem=['*    * ****** *     ****    * ****** *     *','*    * *    * *     *   *   * *      **   **','*    * *    * *     *    *  * *      * * * *',\
        '****** *    * *     *    *    ****** *  *  *','*    * *    * *     *    *    *      *     *','*    * *    * *     *   *     *      *     *',\
        '*    * ****** ***** ****      ****** *     *']

def anm1(lista,x,largo_goma,tablero):
    for i in range (0,7):
        tablero.escribirMensaje(lista[i],x,i+3)
    print (tablero)
    sleep(0.6)
    for i in range (0,7):
        tablero.borrarZona(x,i+3,largo_goma,1)
    print(tablero)
    sleep(0.4)

def anm2(lista,x,largo_goma,tablero):
    for i in range(0,7):
        tablero.escribirMensaje(lista[i],x,i+3)
        sleep(0.09)
        print (tablero)
    for i in range (0,7):
        tablero.borrarZona(x,i+3,largo_goma,1)
        sleep(0.09)
        print(tablero)

anm1(texas,22,36,Mesa)
anm1(holdem,18,45,Mesa)
anm2(texas,22,36,Mesa)
anm2(holdem,18,45,Mesa)
