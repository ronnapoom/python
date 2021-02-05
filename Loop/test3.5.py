student = int(input("PLEASE ENTER STUDENT : "))
print("-"*45)
i = 0
a1 = a2 = a3 = a4 = a5 = 0
while(i < student) :
    score = int(input("PLEASE ENTER SCORE : "))
    if score <= 100 and score >= 90 :
        a1 += 1
    elif score < 90 and score >= 80 :
        a2 += 1
    elif score < 80 and score >= 70 :
        a3 += 1
    elif score < 70 and score >= 60 :
        a3 += 1
    elif score < 60 and score >= 50 :
        a4 += 1
    elif score < 50 and score >= 0 :
        a5 += 1
    i += 1
   
print("90-100 : ", "*" *int(a1))
print("80-89 : ", "*" *int(a2))
print("70-79 : ", "*" *int(a3))
print("60-69 : ", "*" *int(a4))
print("50-59 : ", "*" *int(a5))