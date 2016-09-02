def rodillo(r,s,t,u,v,w,x,y,z):
    print ('   |-----|-----|-----|')
    print ('   |',t,'|',w,'|',z,'|')
    print ('-->|',s,'|',v,'|',y,'|')
    print ('   |',r,'|',u,'|',x,'|')
    print ('   |-----|-----|-----|')
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

a,b,c=giro_rodillo(1) # el numero refiere al giro del primer rodillo
d,e,f=giro_rodillo(2)
g,h,i=giro_rodillo(3)
rodillo(a,b,c,d,e,f,g,h,i)
