#Overloading & Overriding
""" 

Overloading
คือเมธอดที่มีชื่อเหมือนกันและอยู่ภายในคลาสเดียวกัน
สิ่งที่แยกความอตกต่างของเมธอดที่เป็น overloading method
คือ พารามิเตอร์ (เป็นผลมาจากคุณสมบัติ OO คือ polymorphism)

Overriding
คือ เมธอดของคลาสลูก(subclass) ที่มีชื่อเหมือนกับเมธอดของคลาสแม่(superclass)
(เป็นผลมาจากคุณสมบัติ OO คือ inheriitance)


คลาสย่อยต้องรีเทีร์นข้อมูลไม่งั้นกดรันแล้วจะโชว์คำว่าNone
"""

class Employee:
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "บริษัทPhOoMจักกำ"
    def __init__(self, name, salary, department): 
        self._name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self._department))
        return None

    #รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12
    
    def _getIncome(self, bonus=0, overtime=0):
        return (self.__salary * 12)+bonus+overtime
    
    #ระบุทุกอย่างแบบเรียงแถว
    def __str__(self):
        return (f"ชื่อพนักงาน = {self._name} , แผนก = {self._department} , เงินเดือน = {self.__salary} , รายได้ต่อปี = {self._getIncome()}")




class Accounting(Employee):
    __departmentName = "แผนบัชญี"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        #เป็นค่าสร้างขึ้นมาใหม่
        self.age = age

    def __str__(self):
        return super().__str__()+"อายุ = {}".format(self.age)
    
    def _showData(self):
        super()._showData()
        print("อายุ = {}".format(self.age))
        return ("----")
    

class Programmer(Employee):
    __departmentName = "แผนพัฒนาโปรแกรม"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.experience = experience
        self.skill = skill
    
    def __str__(self):
        return super().__str__()+"ประสบการณ์การทำงาน = {} , ทักษะ = {}".format(self.experience,self.skill)
    
    def _showData(self):
        super()._showData()
        print("ประสบการณ์การทำงาน = {}".format(self.experience))
        print("สกิลที่มี = {}".format(self.skill))
        return ("----")
    
        

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area
    
    def __str__(self):
        return super().__str__()+"พื้นที่รับผิดชอบ = {}".format(self.area)
    
    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = {}".format(self.area))
        return ("----")

account = Accounting("Som", 20000, 14)
print(account._showData())

programmer = Programmer("Phoompirak", 50000, "Make game PC", "Python and C")
print(programmer._showData(),"รายได้ต่อปีรวมโบนัสรวมovertime = ",programmer._getIncome(2500, 5000))

sale = Sale("Aip", 30000, "Bangkok")
print(sale._showData())

print("__str__ = ",programmer.__str__())
#เคยลืมว่า self.__name จะไม่สามารถให้classอื่นเข้าดูได้
print(f"รายได้ต่อปีของ = {programmer._name} คือ {programmer._getIncome()}")