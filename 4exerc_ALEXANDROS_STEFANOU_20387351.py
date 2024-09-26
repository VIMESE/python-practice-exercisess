days =0
x = 0
y = 0
ej = 0
em = 0

def euro_to_yen(euro):
    global y
    y = euro*164.80
    return y

def total_cost():
    global x, ej, days
    while days<7:
        x = float(input())
        ej = x + ej
        days +=1
        if days == 7:
            break    
    return ej

def yen_to_euro(y,ej):
    global em
    em = y - ej
    return em/164.80


print(euro_to_yen(2000))
print(total_cost())
print(yen_to_euro(y,ej))
