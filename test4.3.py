import datetime
name,pts,time,hit=[],[],[],[]
num =int(input('Enter number of Competitor     : '))
for i in range(num):
    print(i+1,'of Comprtitor')
    regname =input('Name of Competitor             : ')
    regpts =int(input('Enter your PTS                 : '))
    regtime =float(input('Enter your time                : '))
    name.insert(i,regname),pts.insert(i,regpts),time.insert(i,regtime),hit.insert(i,regpts/regtime)
for i in range(num):
    j = i
    for j in range(num):
        if pts[i] > pts[j]:
            a,b,c,d = hit[i],name[i],pts[i],time[i]
            hit[i],name[i],pts[i],time[i]=hit[j],name[j],pts[j],time[j]
            hit[j],name[j],pts[j],time[j]=a,b,c,d
date = datetime.datetime.now()
datenew = date.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun',date.strftime('%A'),'Training',date.strftime('%Y'))
print(datenew)
print('-'*110+'\n{0:-<15}{1:-<15}{2:-<15}{3:-<20}{4:-<15}{5:-<15}{6:-<15}'.format('No.','PTS','TIME','COMPETITOR','HIT FACTOR','STATE POINTS','STATE PERCENT\n'+'-'*110))
for i in range(num):
    print('{0: <15}{1: <15}{2: <15}{3: <20}{4: <15}{5: <15}{6: <1}'.format(i+1,pts[i],time[i],name[i],'%.4f'%hit[i],'%.4f'%float(hit[i]/hit[0]*50),'%.4f'%float((hit[i]/hit[0]*50)/(hit[0]/hit[0]*50)*100)))