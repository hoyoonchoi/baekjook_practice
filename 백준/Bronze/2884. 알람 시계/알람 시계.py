h,m= input().split( )
h= int(h)
m= int(m)


if (m>=45):
    print(h,m-45)
else:
    if(h==0):
        nh=61-(45-m)
        print(23,nh-1)
    else:
        nh=61-(45-m)
        print(h-1,nh-1)