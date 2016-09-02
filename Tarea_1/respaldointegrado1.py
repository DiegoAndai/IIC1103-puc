def rodillo(r,s,t,u,v,w,x,y,z):
    print ('El estado actual de la maquina es: ')
    print ('   |-----|-----|-----|')
    print ('   |',t,'|',w,'|',z,'|')
    print ('-->|',s,'|',v,'|',y,'|')
    print ('   |',r,'|',u,'|',x,'|')
    print ('   |-----|-----|-----|')
    print ('')
def giro_rodillo(x):
    import random
    x=random.randint(1,20)
    y=x+1
    z=x+2
    x=asignador_valores(x)
    y=asignador_valores(y)
    z=asignador_valores(z)
    return x,y,z
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

bolsillo=int(input('¿Cuanto dinero quieres jugar hoy?: $'))
while bolsillo < 500:
    print ('Recuerda, no puedes comenzar con menos de $500 en tu bolsillo (has ingresado $'+str(bolsillo)+'), ingresa la cantidad que falta:', end='')
    dinero_faltante=int(input('$'))
    bolsillo=bolsillo+dinero_faltante
print ('Excelente, comencemos, tu bolsillo actual es $'+str(bolsillo))
print ('')
a,b,c=giro_rodillo(1) # el numero refiere al giro del primer rodillo
d,e,f=giro_rodillo(2)
g,h,i=giro_rodillo(3)
rodillo (a,b,c,d,e,f,g,h,i)
while bolsillo>10:
    apuesta=int(input('Dinero que apostaras esta ronda: $'))
    if apuesta<10 or apuesta>500:
        print ('La apuesta no puede ser menor a $10 ni mayor a $500, ingresa una nueva apuesta: ', end='')
        apuesta=int(input('$'))
    if apuesta<10 or apuesta>500:
        print ('El juego se ha detenido pues has ingresado una cantidad incorrecta en la apuesta dos veces')
        break
    a,b,c=giro_rodillo(1) # el numero refiere al giro del primer rodillo
    d,e,f=giro_rodillo(2)
    g,h,i=giro_rodillo(3)
    #b=' 6 '
    #e='- -'
    #h=' 6 '
    rodillo (a,b,c,d,e,f,g,h,i)
    #revisar booleanos
    if b==e==h==' * ':
        ganancia=apuesta*100
        print ('Wow!, es tu dia de suerte, has sacado la combinacion ganadora, tu ganancia es de $'+str(ganancia))
    elif b==e==h!='- -':
        ganancia=apuesta*50
        print ('Excelente tiro, un trio perfecto, tu ganancia es de $'+str(ganancia))
    elif b!=e!=h!='- -' and (b==h==' * ' or b==e==' * ' or e==h==' * '):
        ganancia=apuesta*25
        print ('Gran tiro, dos comodines y sin caer entre numeros, tu ganancia es de $'+str(ganancia))
    elif b!='- -' and e!='- -' and h!='- -' and (b==h or b==e or e==h):
        ganancia=apuesta*10
        print ('Un par y un comodin! que suerte, tu ganancia es de $'+str(ganancia))
    elif b==h==' * ' or b==e==' * ' or e==h==' * ':
        ganancia=apuesta*5
        print ('Par de comodines!, no es una combinacion que se repita mucho, tu ganancia es de $'+str(ganancia))
    elif b==h!='- -' or b==e!='- -' or e==h!='- -':
        ganancia=apuesta*3
        print ('Sigue asi!, ha salido un par, tu ganancia es de $'+str(ganancia))
    elif b==' * ' or e==' * ' or h==' * ':
        ganancia=apuesta
        print ('Has sacado el comodin, no ganas pero mantienes tu dinero: $'+str(ganancia))
