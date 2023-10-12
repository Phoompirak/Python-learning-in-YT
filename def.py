"""
โครงสร้าง

def ชื่อตัวแปร():

ชื่อเหมือนกันไม่ได้

"""

def Sayhi():
    print("Hello word")

Sayhi()

#Global Variavle(ตัวแปรนอก) / Local Variable(ตัวตัวแปรใน)

def displayNumber():
    x=10
    print("Hello = ",x,"ใน")
 
x=20
displayNumber()
print("Hello = ",x,"นอก")


#รับค่าเข้ามาที่ Function
def myfunction(Name,Lastname,c):
    print("Hello Mr.",Name,Lastname,"age 40")

myfunction("Jojo","Dudu","40")
myfunction(4,10,11)
#เปลี่ยนค่าตัวแปรได้
Fname = "Phoom"
Lname = "300x"
Age = 40
myfunction(Fname, Lname, Age)

"""
Arguments => ค่าที่ส่งเข้าไปใน function =>Name, Lastname, c

Parameter => ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน (Arguments) =>Fname, Lname, Age
อาส่ง - พารับ
"""

def mydata(a, b):
    print("a+b = ",a+b)

mydata(5, 9) #5, 9 เป็นArguments  a, b เป็นParameter

def Searchnumber(number):
    if number%2 == 0:
        print(number, "เป็นเลขคู่")
    else:
        print(number, "เป็นเลขคี่")

A = [3, 5, 7, 2, 10]
print(type(A))
for i in A:
    Searchnumber(i)


# *agrs => ค่าใน Parameter มีได้หลายค่า
def sumpulse(*agrs):
    sum=0
    for item in agrs:
        sum+=item
    print("sum :", sum)

sumpulse(10, 29, 33, 111)


# Keyword Arguments
def displayData(ffname, llname, city):
    print("ชื่อ =", ffname)
    print("นามสกุล =", llname)
    print("จังหวัด =", city)

displayData(city="ระยอง", llname="โคตร",ffname="นายรวย")


#List Parameter
def DisplayfruitList(Fruit):
    for i in Fruit:
        print("ผลไม้ =>",i)
    print(" ")

def DisplayAnimalTup(Animal):
    for x in range(len(Animal)):
        print("สัตว์ =>",Animal[x])

fruit=["Banana", "Papaya", "Orange"]
DisplayfruitList(fruit)
animaltup=("Dog", "Chicken", "Hamter")
DisplayAnimalTup(animaltup)


# Function  return ค่า
"""
1.ไม่มีการรับค่าและส่งค่า
def name():

2.มีการรับค่าและส่งค่า
def name(a, b):

3.รับค่าเข้าไปทำงาน และส่งออกมา
def add(a,b):
    return a+b

4.รีเทิร์นออกจากฟังก์ชันก็ได้
def add(a, b):
    x = a-b
    if x%2 == 0:
        return
    a+=3
    b+=1
"""
def add(a,b):
    return a+b

def shownumber():
    return 500

x= add(10,20)
print(x)
z= shownumber()
print(z)

def randomNumber(x):
    if x == '100':
        print("ถูกหวย")
        return 1000
    else:
        print("ไม่ถูกหวย")
        return 0

Money=randomNumber("100")
N = 300
result = Money-N
print("เงินรางวัล =>",Money,"\nคงเหลือ =>",result)




# **kwargs ใส่ข้อมูลตอนใช้ฟังก์ชันได้ไม่จำกัด => ชื่อ Parameter มีได้หลายชื่อ
def displayDataname(**kwargs):
    print(kwargs)

displayDataname(Firstname="Phoompirak", Lastname="Karajak", Age=15, City="อำนาจเจริญ")
displayDataname(Firstname="Phoompirak", Lastname="Karajak", Status="โสด", City="อำนาจเจริญ")
displayDataname(Firstname="Prayeay", Status="โสด", City="อำนาจเจริญ")


#ฟังก์ชันเรียกใช้ฟังก์ชัน
def equal(x, y, z):
    A = compareMax(x, y) #10,20   แบบย่อ 
    M = compareMax(A, z) #20,30      return compareMax(compareMax(x,y),z)
    return M

def compareMax(x, y):
    if x>y:
        return x
    else:
        return y

max = equal(10, 20, 30)
print("ค่ามากสุด :",max)



#Recursive Function
"""
หาจุดวนซ้ำ
หาจุดออกจาก function (retunr)
ต้องมี parameter


1-5 โดยไม่ใช้ loop
"""

def addNumber(NumBer):
    if NumBer==5:
        return
    print("Def no loop :",NumBer)
    NumBer+=1
    addNumber(NumBer)

addNumber(1)

#Sigma
def summation(NumBer):
    if NumBer==1:
        return NumBer
    else:
        return NumBer+summation(NumBer-1)

"""
การหา Sigma
5
5 + summation(5-1)
5 + 4 + summation(3)
5 + 4 + 3 + summation(2)
5 + 4 + 3 + 2 +summation(2-1)

5 + 4 + 3 + 2 + 1

"""
x = summation(100)
print("Sigma :",x)


#สร้างฟังก์ชันหาค่า Factorial
"""
5! = 5 x 4 x 3 x 2 x 1 = 120

"""
def Factorial(number):
    if number==1:
        return number
    else:
        return number * Factorial(number-1)

x = Factorial(5)
print("Factorial function :",x)


# Fibonacci number
#คือต่อผลบวกของสองตัวล่าสุดไปเรื่อย F(n) = F(n-1) + F(n-2)
#0, 1, 1,2,3,5,8,...

def Fibonacci(number):
    if number<=1:
        return number# 2 ลำดับแรก
    else:
        return Fibonacci(number-1) + Fibonacci(number-2) #เลขลำดับถัดไป

for i in range(10):
    print(Fibonacci(i))



# Pass
def getName(name):
    if name == "kong":
        print("ยินดีด้วย")
    else:
        pass

def getLast():
    pass

def getcity():
    print("อยู่กรุงเทพ")



# Lambda function ฟังก์ชันไม่มีชื่อ
"""

lambda argument : expression

"""

x = lambda names:names
sum = lambda x,y:x+y

print("sum by Lambda :",sum(5,10))
print("Name by lambda :",x("Phoompirak"))

#Def ช้อน Lambda
def myPower(x):
    #x= ตัวเลข
    #a= เลขชี้กำลัง
    return lambda a : x**a

y = myPower(5)
result = y(2) # y กายเป็นชื่อของฟังก์ชัน Lambda
print("Def nested Lambda :",result)


#หาผลรวม
def summation(number):
    total, avg = 0, 0
    for i in number:
        total+=i
    avg = total/len(number)
    return total,avg

x = [1,2,3,4,5,6,7,8]
y,z = summation(x)
print(f"ผลรวม Def :{y} and Average :{z}")


#หาจำนวนตัวอักษรพิมเล็ก/พิมพ์ใหญ่

def checkString(message):
    result = {"UPPER":0, "LOWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWER"]+=1
        else:
            pass
    return result


x = checkString("ABcDef")
print(f"Upper and Lower :{x}")


#หาเบอร์โทรติดต่อด้วยการพิมพ์ข้อความ
Data = {"191":"แจ้งเหตุด่วน","1668":"รถโรงพยาบาล","1447":"ดับเพลิง"}

def SreachNumber(message):
    for key, value in Data.items():
        if value == message:
            return "เบอร์ติดต่อ =>",key
    return "ไม่มีข้อมูล"
        

FBI = input("ป้อนข้อมูล :")
NUMBER = SreachNumber(FBI)
print(str(f"ข้อมูลติดต่อของคุณ :{NUMBER}"))



#หอคอยฮานอย
def Hanoi(n, a, b, c): #จำนวนจาน, จุดย้าย, จุดพัก, จุดไป
    #a => c
    if(n==0):
        return
    Hanoi(n-1, a, c ,b) #ย้าย a (ล, ก) -> b | c จุดพัก
    print(f"จานที่ ={n} จาก = {a} ไป = {c}")
    Hanoi(n-1, b, a, c)

Hanoi(3, "3", "2", "1")