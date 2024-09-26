print("give me the years of your subscription")
years = int(input())
print("give me the price of the packet you chose")
price = float(input())

if years==1:
    yp = 12 * price * 0.95

if years ==2 or 3:
    yp = 12 * price * 0.9

if years >=4:
    yp= 12 * price * 0.8
        
if years ==0:
    yp= 6*(price-(6*price*0.5))

print(f"your yearly consumption price comes at {round(yp, 2)}" )
