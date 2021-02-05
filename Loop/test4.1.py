print('\tโปรแกรมรายการสินค้า')
print('-'*35)
x = 0
choose_list = ['\t1.เมาส์','\t2.แป้นพิมพ์','\t3.จอแสดงผล','\t4.หูฟัง','\t5.ไมค์โครโฟน','\t6.ลำโพง']
price_list = [1990,2990,6590,990,790,2990]
cargo_list = [0,0,0,0,0,0]
def menu() :
    global choice
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n4.หยิบสินค้าออกจากตะกร้า\n5.ปิดโปรแกรม\n')
    choice = int(input('กรุณาเลือกรายการสินค้า'))

def choose_def() :
    for x in range(0,6) :
        print(choose_list[x],' ราคา ',price_list[x],' บาท')

def choice_def() :
    for x in range(0,6) :
        print(choose_list)
    pick = int(input('เลือกหยิบสินค้าหมายเลข หรือ พิมพ์ 7 เพื่อออก : '))
    if pick == 1 :
        cargo_list[0] += 1
    elif pick == 2 :
        cargo_list[1] += 1
    elif pick == 3 :
        cargo_list[2] += 1
    elif pick == 4 :
        cargo_list[3] += 1
    elif pick == 5 :
        cargo_list[4] += 1
    elif pick == 6 :
        cargo_list[5] += 1
    elif pick == 7 :
        menu()

def showlist_def() :
    print(''*10,'สินค้าที่คุณหยิบไปมีดังนี้',''*10)
    print('-'*5,'{0:-<15}{1:-<15}{2:-<15}',format('สินค้า','จำนวน','ราคา'))
    for x in range(0,6) :  
       print(choose_list[x],'\t',cargo_list[x],'\t',cargo_list[x]*price_list[x]) 

while(True) :
    menu()
    if choice == 1 :
        choose_def()
    elif choice == 2 :
        choose_def
    elif choice == 3 :
        choose_def
    elif choice == 5 :
        break
