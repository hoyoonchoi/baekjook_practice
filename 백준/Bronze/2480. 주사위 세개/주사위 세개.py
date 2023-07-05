a,b,c= input().split( )
a=int(a)
b=int(b)
c=int(c)
if( (a==b)and(b==c)):
    print(10000+ a*1000)
elif((a==b)or(c==a)):
    print(1000+ a*100)
elif((b==c)):
    print(1000+ b*100)
else:
    if (a>b):
        k=int(a)
        if(k<c):
            k=int(c)
    else:
        k=int(b)
        if(k<c):
            k=int(c)
    print(k*100)            
            
    