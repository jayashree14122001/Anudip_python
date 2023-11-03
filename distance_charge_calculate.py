d= int(input("Enter the distance(km) to know the distance charges:"))
if (d>=1) and (d<=50):
    
    print("The fare of given distance is:",(d*8))
elif  (d>=51) and (d<=100):
    print("The fare of given distance is:",(d*10))
else :
    print("The fare of given distance is:",(d*12))

    
#output
#Enter the distance(km) to know the distance charges:50
#The fare of given distance is: 400
