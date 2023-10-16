#คลาสแม่ถ้าใช้private varriable คลาสลูกจะดูไม่ได้
#การสืบทอดคุณสมบัติ
""" 
คลาสแม่
class Employee:

คลาสลูก
class Programer(Employee)

"""
#Super
class Employee:
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "บริษัทPhOoMจักกำ"
    def __init__(self, name, salary, department): 
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self._department))
        
    #รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12
    
    def _getIncome(self, bonus=0):
        return (self.__salary *12)+bonus
    
    #ระบุทุกอย่างแบบเรียงแถว
    def __str__(self):
        return (f"ชื่อพนักงาน = {self.__name} , แผนก = {self._department} , เงินเดือน = {self.__salary} , รายได้ต่อปี = {self._getIncome()}")


class Accounting(Employee):
    __departmentName = "แผนบัชญี"
    def __init__(self, name, salary):
        #เรียกใช้constructorคลาสแม่
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = "แผนพัฒนาโปรแกรม"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()


account = Accounting("น้องนัทตี้",18000)
print("รายได้ต่อปีคือ {}".format(account._getIncome()))
print("\t")
programmer = Programmer("น้องภูมิมี้",50000)
print("รายได้ต่อปีคือ {}".format(programmer._getIncome()))
print("\t")
sale = Sale("น้องเอเจ้น",20000)
print("รายได้ต่อปีคือ {}".format(sale._getIncome()))
print("\t")

account = Accounting("เก่ง", 19000)
print(account.__str__())
