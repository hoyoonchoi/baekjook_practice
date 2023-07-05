h,m= input().split( )
h= int(h)
m= int(m)
t= int(input())

nh =int(h+ t/60) 
nm =int(m+ t%60) 

if (nm>=60):
    nm= nm-60
    nh= nh+1
    if (nh>23):
       nh= nh-24

else:
    if(nh>23):
        nh= nh-24

print(nh,nm) 