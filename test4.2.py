vocab_dictionary = {}

def menu():
    global choice
    print("-"*50 + '\n 1.พจนานุกรม\n 2.แสดงคำศัพท์ทั้งหมด \n 3.ลบคำศัพท์ \n 4.ออกจากโปรแกรม')
    choice = input("ENTER CHOICE: ")

def add_vocab():
    vocab = input("\nเพิ่มคำศัพท์ :\t")
    type_vocab = input("ชนิดของคำ(n. , v. , adj. , adv.): ")
    mean = input("ความหมาย: ")
    vocab_dictionary[vocab] = type_vocab, mean
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว")

def show_vocab():
    print("\n\tคำศัพท์ทั้งหมด\n {0:<15}{1:<8}{2}".format('คำศัพท์','ประเภท','ความหมาย'))
    for enter in vocab_dictionary:
        print("{}:<3{}".format(enter, '', vocab_dictionary[enter]))

def delete_vocab():
    delete_word = input("\nพิมพ์คำศัพท์ที่ต้องการลบ: ")
    yes_no = input("ต้องการลบ {} ใช่หรือไม่ (yes / no): ".format(delete_word))
    if yes_no == 'y':
        del vocab_dictionary[delete_word]
        print("ลบ" ',' +delete_word+ ',' "เรียบร้อยแล้ว")
while True:
    menu()
    if choice == '1':
        add_vocab()
    elif choice == '2':
        show_vocab()
    elif choice == '3':
        delete_vocab()
    elif choice == '4':
        e = input("ต้องการออกจากโปรแกรมใช่หรือไม่ y/n: ")
        if e.lower() == 'n':
            os.system('cls')
        elif e.lower() == 'y':
            os.system('cls')
            break



