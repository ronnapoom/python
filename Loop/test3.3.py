print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
food_fav = []
n = 0
while(True) :
    n += 1
    food = str(input("อาหารโปรดลำดับที่ {} :\t".format(n)))
    food_fav.append(food)
    if(food == "exit") :
        break
for n in range (1,n) :
    print(n,".",food_fav[n-1], end = " " )     
    
