import os
choice = 0
listcoffee = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านดนตรี\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม')
    choice = input('กรุณาเลือกทำรายการ : ')
    screen_clear()

def showmenu(): 
    print('\tรายการเครื่องดนตรี')
    print('\t1.กีต้าร์โปร่้ง 5,500 บาท\n','\t2.กีต้าร์ไฟฟ้า 12,000 บาท\n','\t3.เบส 15,000 บาท\n','\t4.กีต้าร์คลาสสิค 55,000 บาท\n','\t5.แอมป์กีต้าร์ 25,000 บาท')

def pickmenu():
    global pick
    print('\tรายการสินค้า\n 1.กีต้าร์โปร่ง\n 2.กีต้าร์ไฟฟ้า\n 3.เบส\n 4.กีต้าร์คลาสสิค\n 5.แอมป์กีต้าร์')
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listcoffee[0] += 1
    elif pick == 2:
        listcoffee[1] += 1
    elif pick == 3:
        listcoffee[2] += 1
    elif pick == 4:
        listcoffee[3] += 1
    elif pick == 5:
        listcoffee[4] += 1
    screen_clear()

def showuserpick():
    list_score = ['กีต้าร์โปร่ง','กีต้าร์ไฟฟ้า','เบส','กีต้าร์คลาสสิค','แอมป์กีต้าร์']
    list_price = [5500,12000,15000,55000,25000]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listcoffee[i],listcoffee[i]*list_price[i]))

def deletuserpick():
    print('\t\nรายการสินค้า\n 1.กีต้าร์โปร่ง\n 2.กีต้าร์ไฟฟ้า\n 3.เบส\n 4.กีต้าร์คลาสสิค\n 5.แอมป์กีต้าร์')
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก'))
    if depick == 1:
        listcoffee[0] -= 1
    elif depick == 2:
        listcoffee[1] -= 1
    elif depick == 3:
        listcoffee[2] -= 1
    elif depick == 4:
        listcoffee[3] -= 1
    elif depick == 5:
        listcoffee[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'y':
            screen_clear()
        elif c.lower() == 'n':
            screen_clear()
            break