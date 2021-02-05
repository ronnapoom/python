import datetime
name = [] 
score = [] 
times = [] 
hit = []
def time_a():
    timeis = time.localtime()
    x = time.strftime('%d %N %Y, %H:%M:%S', timeis)
    print(x)

amout = int(input('กรุณาพิมพ์จำนวนผู้ซ้อมยิงปืน: '))
for i  in range(amout):
    print("ป้อนข้อมูลคนที่",1+i)
    name_ = input("ชื่อผู้ซ้อม: ")
    score_ = float(input("คะแนน: "))
    time_ = float(input("ระยะเวลาที่ใช้: "))
    name.append(name_)
    score.append(score_)
    times.append(time_)
    hit.append(score_/time_)
for i  in range(amout):
    j = i 
    for j in range(amout):
        if hit[i] > hit[j]:
            a, b, c, d = hit[i], name[i], score[i], times[i]
            hit[i], name[i], score[i], times[i] = hit[j], name[j], score[j], times[j]
            hit[j], name[j], score[j], times[j] = a, b, c, d
timeis = time.localtime()
a = time.strftime('%A', timeis)
b = time.strftime('%Y',timeis)
print("Shotgun" +a+ "Training",b,"\nCondition: 1")
time_a()
print('-'*100)
print("{0: -<6}{1: -<6}{2: -<8}{3: -<17}{4: -<12}{5: -<15}{6}".format("NO.","PTS","TIME","COMPETITOR#Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
print("-"*100)
for i in range(amout):
    stage_point = (hit[i]/hit[0])*50
    stage_percent = (stage_point/(hit[i]/hit[0])*50)*100
    print("{0: <16}{1: <6}{2: <8}{3: <17}{4: <12}{5: <15}{6}".format(1+i, int(score[i]), int(time[i]), name[i], "%.4f"%hit[i], "%.4f"%stage_point, "%.2f"%stage_percent))