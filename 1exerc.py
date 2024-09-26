print("give me the seconds you want calculated: ")
s = int(input()) 
h = int(s/3600)
m = int((s%3600)/60)
ls = int((s%3600)%60)
txt = "the seconds are {} : {} : {} "
print(txt.format(h,m,ls))
