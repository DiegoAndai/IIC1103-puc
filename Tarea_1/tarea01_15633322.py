def rodillo(r,s,t,u,v,w,x,y,z):
    print ('\nEl estado actual de la maquina es: ')
    print ('   |-----|-----|-----|')
    print ('   |',t,'|',w,'|',z,'|')
    print ('-->|',s,'|',v,'|',y,'|')
    print ('   |',r,'|',u,'|',x,'|')
    print ('   |-----|-----|-----|')
    print ('')
def asignador_valores (x):
    if x%2==0:
        x=' '+str(int(x/2))+' '
    else:
        x='- -'
    if x==' 10 ':
        x=' * '
    if x==' 11 ':
        x=' '+str(1)+' '
    return x
def giro_rodillo(x):
    import random
    x=random.randint(1,20)
    y=x+1
    z=x+2
    x=asignador_valores(x)
    y=asignador_valores(y)
    z=asignador_valores(z)
    return x,y,z
def comprobar_int(x,y):
    try:
        x=int(x)
        y=True
    except ValueError:
        x=input('Ese valor no es correcto, ingreselo nuevamente $:')
        try:
            x=int(x)
            y=True
        except ValueError:
            x=0
            y=False
    return x,y


print ('\n*'+'*'*55)
print ('*'*3+' '*50+'*'*3)
print ('*'*3+' '*12+'Bienvenido al Tragamonedas'+' '*12+'*'*3)
print ('*'*3+' '*50+'*'*3)
print ('*'*56)

print ('\nEn este juego de azar apuestas al giro de tres rodillos,')
print ('los que toman valores de 1 a 9, o el comodin "*".')
print ('\nPara comenzar, ingresa dinero a tu "bolsillo" (tiene que')
print ('ser al menos $500), desde este pozo realizaras apuestas:')
print ('la apuesta maxima es de $500 y la minima de $10. La fle-')
print ('cha que aparecera al lado izquierdo señaliza la linea de')
print ('pago de las combinaciones, que son:')
print ('\nTres comodines: 100x')
print ('Tres numeros iguales: 50x')
print ('Dos comodines y un numero: 25x')
print ('Dos numeros iguales y un comodin: 10x')
print ('Dos comodines: 5x')
print ('Dos numeros iguales: 3x')
print ('Un comodin: 1x')


bolsillo=input('\n¿Cuanto dinero quieres jugar hoy?: $')
seguir=True
bolsillo,seguir=comprobar_int(bolsillo,seguir)
if bolsillo < 500 and seguir:
    print ('\nRecuerda, no puedes partir con menos de $500 en tu bol-\nsillo (has ingresado $'+str(bolsillo)+'), ingresa una nueva cantidad', end='')
    bolsillo=int(input(': \n$'))
if bolsillo < 500:
    print ('\nEl juego se ha detenido pues has ingresado una cantidad \nincorrecta para tu bolsillo dos veces \n')
    bolsillo=0
else:
    print ('Excelente, comencemos, tu bolsillo actual es $'+str(bolsillo))
    print ('')
    a,b,c=giro_rodillo(1)
    d,e,f=giro_rodillo(2)
    g,h,i=giro_rodillo(3)
    rodillo (a,b,c,d,e,f,g,h,i)
while bolsillo>=10:
    apuesta=input('\nDinero que apostaras esta ronda: $')
    apuesta,seguir=comprobar_int(apuesta,seguir)
    if not seguir:
        print ('\nEl juego se ha detenido pues has ingresado una cantidad \nincorrecta en la apuesta dos veces\n')
        break
    if apuesta<10 or apuesta>500 or apuesta>bolsillo and seguir:
        print ('\nLa apuesta no puede ser menor a $10 mayor a $500, ni ser \nmayor a tu bolsillo ($'+str(bolsillo)+'), ingresa una nueva apuesta: \n', end='')
        apuesta=int(input('$'))
    if apuesta<10 or apuesta>500 or apuesta>bolsillo:
        print ('\nEl juego se ha detenido pues has ingresado una cantidad \nincorrecta en la apuesta dos veces\n')
        break
    bolsillo=bolsillo-apuesta
    print ('Bolsillo actual: $'+str(bolsillo))
    a,b,c=giro_rodillo(1)
    d,e,f=giro_rodillo(2)
    g,h,i=giro_rodillo(3)
    rodillo (a,b,c,d,e,f,g,h,i)
    if b==e==h and h==' * ':
        ganancia=apuesta*100
        print ('Wow!, es tu dia de suerte, has sacado la combinacion \nganadora, tu ganancia es de $'+str(ganancia)+'.')
    elif b==e==h and h!='- -':
        ganancia=apuesta*50
        print ('Excelente tiro, un trio perfecto, tu ganancia es de $'+str(ganancia)+'.')
    elif (b==h==' * ' and e!='- -') or (b==e==' * ' and h!='- -') or (e==h==' * ' and b!='- -'):
        ganancia=apuesta*25
        print ('Gran tiro, dos comodines y sin caer entre numeros, tu ga-\nnancia es de $'+str(ganancia)+'.')
    elif (b==h and h!='- -' and e==' * ') or (b==e and e!='- -' and h==' * ') or (e==h and h!='- -' and b==' * '):
        ganancia=apuesta*10
        print ('Un par y un comodin! que suerte, tu ganancia es de $'+str(ganancia)+'.')
    elif b==h==' * ' or b==e==' * ' or e==h==' * ':
        ganancia=apuesta*5
        print ('Par de comodines!, no es una combinacion que se repita \nmucho, tu ganancia es de $'+str(ganancia)+'.')
    elif b==h!='- -' or b==e!='- -' or e==h!='- -':
        ganancia=apuesta*3
        print ('Sigue asi!, ha salido un par, tu ganancia es de $'+str(ganancia)+'.')
    elif b==' * ' or e==' * ' or h==' * ':
        ganancia=apuesta
        print ('Has sacado el comodin, no has ganado nada pero mantienes \ntu dinero: $'+str(ganancia)+'.')
    else:
        ganancia=0
        print ('Lo siento, no has ganado nada.')
    bolsillo=bolsillo+ganancia
    if bolsillo<10:
        print ('\nLo siento, tu bolsillo tiene menos de $10, se ha acabado \nel juego cuando tenias: $'+str(bolsillo)+'. \nRetira tu dinero, muchas gracias por jugar\n')

        break
    print ('Tu bolsillo actual es: $'+str(bolsillo)+'.')
    continuar=input('\nQuieres seguir jugando?: ')
    while continuar!='si' and continuar!='Si' and continuar!='s' and continuar!='S' and continuar!='No' and continuar!='no' and continuar!='n' and continuar!='N':
        print ('Lo siento, no entiendo lo que quieres decir con "'+str(continuar)+'".\nPorfavor ingresa si o no', end='')
        continuar=input(': ')
    if continuar=='no' or continuar=='No' or continuar=='n' or continuar=='N':
        print ('\nHas terminado el juego cuando tu bolsillo era: $'+str(bolsillo)+'. \nRetira tu dinero, muchas gracias por jugar\n')
        break
