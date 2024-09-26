x = 0
chickens = 0
min =-1
sum = 0
mesos = 0
while x < 20:
    vathmos = int(input())
    if vathmos >= 90 and vathmos <=100:
        print("arista")
    elif vathmos >= 75 and vathmos <=89:
        print("brava")
    elif vathmos >= 50 and vathmos <=74:
        print("perases")
    elif vathmos >= 0 and vathmos <50:
        print("you shall not pass")        #goated reference
    else:
        min= 0
        break;

    if vathmos == 0:
        chickens += 1
    if vathmos > min:
        min= vathmos

    sum = vathmos + sum
    mesos = sum/20

print(f"max: {min} kai mo: {mesos} ")
print(f"den egrapsan {chickens} diagonisma")

    
        
