# importo el modulo de poker
# cargo las funciones de poker
from poker import Carta, Baraja, Tablero
from poker import obtenerApuestaRobot, compararJugadas

# creo la baraja
deck = Baraja()

# reparto cartas
cartasHumano = []
cartasRobot = []
cartasMesa = []

# 2 cartas para cada jugador
for i in range(2):
    cartasHumano.append(deck.obtenerCarta())
    cartasRobot.append(deck.obtenerCarta())

# 5 cartas en la mesa
for i in range(5):
    cartasMesa.append(deck.obtenerCarta())

# Hago un dibujo dibujo simple en el tablero
table = Tablero()

# dibujo cartas de la mesa
xi = 10
yi = 2
x = xi
for carta in cartasMesa:
    table.dibujarCarta(carta, x, yi)
    x += 10

# dibujo un borde en las cartas de la mesa y un mensaje
table.dibujarBorde(xi-2,yi-1,10*5+1,8)
table.escribirMensaje('Mesa',xi+20,yi-1)

# dibujo cartas jugador humano
xi = 10
yi = 11
x = xi
for carta in cartasHumano:
    table.dibujarCarta(carta, x, yi)
    x += 10
table.dibujarBorde(xi-2,yi-1,10*2+1,8)
table.escribirMensaje('Humano',xi+2,yi-1)

# dibujo cartas jugador robot
xi = 35
yi = 11
x = xi
for carta in cartasRobot:
    table.dibujarCarta(carta, x, yi)
    x += 10
table.dibujarBorde(xi-2,yi-1,10*2+1,8)
table.escribirMensaje('Robot',xi+2,yi-1)

# imprimo el tablero en pantalla 
print(table)

# simular una apuesta de robot
apuesta_actual_robot = 10   # lo que lleva apostado hasta ahora
dinero_robot = 100          # el dinero ue le queda al robot 
apuesta_a_superar = 40      # la apuesta a superar

# obtengo la nueva apuesta del robot
apuesta_robot = obtenerApuestaRobot(cartasRobot, cartasMesa, dinero_robot, apuesta_actual_robot, apuesta_a_superar)

if apuesta_robot == 0:
    print("Robot se retira")
elif apuesta_robot == apuesta_a_superar:
    print("Robot iguala a apuesta de $"+str(apuesta_a_superar))
else:
    print("Robot paga la apuesta de $"+str(apuesta_a_superar)+" y la sube en $"+str(apuesta_robot-apuesta_a_superar))

# independiente de la apuesta, veo quién ganaría
print("Resultado: ",compararJugadas(cartasHumano, cartasRobot, cartasMesa))
print()
