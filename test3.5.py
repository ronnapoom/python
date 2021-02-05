student = int(input("PLEASE ENTER STUDENT :"))
print("-"*45)
i =  0
a1 = a2 = a3 = a4 = a5 = a6 = 0
while i < student :
    score = int(input("PLEASE ENTER SCORE :"))
    if 90 <= score <= 100 :
        a1 += 1
    elif 80 <= score < 90 : 
        a2 += 1
    elif 70 <= score < 80 :
        a3 += 1
    elif 60 <= score < 70 :
        a4 += 1
    elif 50 <= score < 60 :
        a5 += 1
    else :
        a6 += 1
    i += 1

print("90-100 : ","*"*int(a1))
print("80-89  : ","*"*int(a2))
print("70-89  : ","*"*int(a3))
print("60-79  : ","*"*int(a4))
print("50-69  : ","*"*int(a5))
print("0-49   : ","*"*int(a6))

     
