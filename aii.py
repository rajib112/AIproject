print("\n\n\t\t\t\t\t\t\t\t\tWELCOME TO INTELLIGENT VEHICLE PARKING SYSTEM")
car=int(input("Enter car parking price:"))
car=int(car)
bike=int(input("Enter bike parking  price:"))
bike=int(bike)
truck=int(input("Enter truck parking price:"))
truck=int(truck)
bus=int(input("Enter bus parking  price:"))
bus=int(bus)
bicycle=int(input("Enter bicycle parking price:"))
bicycle=int(bicycle)
print("Enter total number of parking slots")
maxx=int(input())
total=0
cnum=[]
bnum=[]
busnum=[]
tnum=[]
bicnum=[]
slot=[]
tslot=maxx
b=1
while b!=0:
    choice =int(input("Press 1 to park a vehicle\n 2 to pay parking fee for your vehicle and 0 to terminate\n"))
    a=1
    while choice==1 and maxx>0 and a!=0:
        vehicle=int(input("Parking vehicle now...\n1\t--\tCar\n2\t--\tBike\n3\t--\tTruck\n4\t--\tBus\n5\t--\tBicycle\n"))
        p=int(input("Enter your vehicle number"))
        if vehicle==1:
            cnum.append(p)
            slot.append(p)
        elif vehicle==2:
            bnum.append(p)
            slot.append(p)
        elif vehicle==3:
            tnum.append(p)
            slot.append(p)
        elif vehicle==4:
            slot.append(p)
            busnum.append(p)
        elif vehicle==5:
            slot.append(p)
            bicnum.append(p)
        maxx-=1
        a=int(input("Press any number to park another vehicle and 0 to exit\n"))
    if maxx==0:
        print("All parking slots are full")
    while choice==2 and a!=0:
           vnum=int(input("Enter you vehicle number\n"))
           if vnum in slot:
               if vnum in cnum:
                   print("Please pay "+str(car)+" rupees at the counter")
                   del cnum[cnum.index(vnum)]
               elif vnum in bnum:
                   print("Please pay "+str(bike)+" rupees at the counter")
                   del bnum[bnum.index(vnum)]
               elif vnum in tnum:
                   print("Please pay "+str(truck)+" rupees at the counter")
                   del tnum[tnum.index(vnum)]
               elif vnum in busnum:
                   print("Please pay "+str(bus)+" rupees at the counter")
                   del busnum[busnum.index(vnum)]
               elif vnum in bicnum:
                   print("Please pay "+str(bicycle)+" rupees at the counter")
                   del bicnum[bicnum.index(vnum)]
               del slot[slot.index(vnum)]
           else:
               print("Sorry we cannot find your vehicle")
           a=int(input("Press 0 to terminate and any other number to pay parking fee of another vehicle\n"))
    b=int(input("Press to 0 to terminate and any other number to continue\n"))
        
            
            
        
