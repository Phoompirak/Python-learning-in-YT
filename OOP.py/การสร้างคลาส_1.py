#Class & Object
#ข้อมุลของพนักงาน

class Employee:
    #การสร้าง Constructor จะถูกเรียกตอนถูกสร้างขึ้นมา
    def __init__(self, name, salary, department):
        print("Default Constructor")
        self.name=name
        self.salary=salary
        self._department=department
    #สร้าง Method

    # def detail(self, name, salary, department):
    #     self.name=name
    #     self.salary=salary
    #     self.department=department
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self._department))
        print("------------------------------------")

    #เคลียร์แรมไรต่างๆเพิ่มประสิทธิภาพบางภาษาต้องทำ
    def __del__(self):
        pass
#การสร้างวัตถุ Object
emp1 = Employee(name="Paphara", salary=40000, department="บัชญี")
emp1.showdata()
emp2 = Employee(name="Phoompirak", salary=40000, department="โปรแกรมเมอร์")
emp2.name = "Phoompirak karajak"
emp2.salary = 100000
emp2.showdata()
emp3 = Employee(name="Bung", salary=40000, department="ผู้จัดการ")
emp3.showdata()

#เช็คว่าถูกสร้างจากClass Employeeไหม
print(isinstance(emp1, Employee))
#มาจากคลาสไหน
print(emp1.__class__)

#ดูMethodในClass
print(dir(emp1))