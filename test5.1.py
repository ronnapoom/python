class nisit : 
    def __init__(self,name,sex,grade,department,province) :
        
        self.name = name
        self.sex = sex
        self.grade = grade
        self.department =  department
        self.province = province
    
    def show_nisit(self) :
        print("-----------------------introduce-----------------------")
        print("Hello My name is",self.name + " SEX ",self.sex + " GRADE ",self.grade + " DEPARTMENT ",self.department + " PROVINCE ",self.province)

data = []
nisit_np = input("NAME-LASTNAME,SEX,GRADE,DEPARTMENT,PROVINCE : ")
split_nisit_np = nisit_np.split(",")    #แยกข้อมูลโดยใช้คำสั่ง split
data.append(split_nisit_np[0])
data.append(split_nisit_np[1])
data.append(split_nisit_np[2])
data.append(split_nisit_np[3])
data.append(split_nisit_np[4])

x = nisit(data[0],data[1],data[2],data[3],data[4])
x.show_nisit()


