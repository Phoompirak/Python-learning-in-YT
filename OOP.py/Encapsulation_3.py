#Encapsulation การซ่อนข้อมูลหรืออนุญาติให้ดูข้อมูล
class Employee:
    #Class variable ถ้าประกาศเป็นprivateจะนำไปแสดงค่าข้างนอกclassไม่ได้
    _minSalary = 12000
    _maxSalary = 50000
    _companyName = "บริษัทPhOoMจักกำ"
    def __init__(self, name, salary, department):
        #Instane variable
        #protected attribute 
        self._name = name
        
        #private method เก็บข้อมูลไว้ใช้ในclassเท่านั้น
        self.__salary = salary
        self.__department = department
        #เรียกใช้showDataในนี้ได้
        #self._showData()
        
        #protected attribute
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))
    
    #Setter methodไว้เซ็ตค่าหลายค่าพร้อมกัน
    def setName(self, newname):
        self._name = newname
    def setSalary(self, newsalary):
        self.__salary = newsalary
    def setDepartment(self, newdepartment):
        self.__department = newdepartment

    #Getter methodเรียกดูค่า
    def getName(self):
        return self._name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

obj1 = Employee("Phoom", 20000, "Programmer")
#ต้องใส่ขีดให้เหมือนกันถึงจะเปลี่ยนข้อมูลได้
#    |
#    v
obj1._name = "Phoompirak karajak"
#ลองเปลี่ยนค่าPrivate method
obj1.__salary = 999999
obj1.__department = "CEO"
obj1._showData()

print(f"นักงานดีเด่นประจำปีคือ =>{obj1.getName()} และเขาทำงานตำแหน่ง =>{obj1.getDepartment()}")

print(f"งานเดือนข้อต่ำของ{Employee._companyName} คือ {Employee._minSalary}")