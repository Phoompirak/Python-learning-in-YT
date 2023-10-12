#primitive
a=1
a1=2
a2=3
a3=4
a4=5
a5=6
a6=7

"""
#Non primitive : list
#ทริค DRUD+len+in
#เทคนิคจำฟังก์ชันลบสมาชิก CRUD = clear, remove, update, del

"""
number=[] #list ว่าง
Number=[1,2,3,4,5,6] #list มีสมาชิก 1-6
name=["นาย A", "นาย B", "นาย C"] #list name มีสมาชิก 3 คน
all=[10,"นายไข่",True,3.14,-10]
#construtor
name=list(["นาย A","นาย B","นาย C"])

#แสดงผล
#print(name)
#print(all)
#print(number)

#เข้าถึงข้อมูล list
print(Number[2])
print(all[-2])
print(all[1:3])
print(all[-3:-1])

#ดึงข้อมูลจากlistทีละตัว
fruit = ["มะม่วง", "มะนาว", "มะขาม", "มะยม"]
for i in range(len(fruit)):
    print(fruit[i])


#นำสมาชิกใหม่มาต่อท้ายเพื่อนด้วย append()
fruit.append("มะพร้าว")
#เพิ่มแบบเลือก Index ได้ใช้ insert()
fruit.insert(2, "แตงโม")
print("appendกับinsertเสร็จ :",fruit)


#การลบสมาชิก แบบระบุชัดเจน remove()
fruit.remove("มะยม")
print("Remove fruit =>",fruit)

#แบบเอาตัวท้าย(ล่าสุด)สุดออก pop()
fruit.pop()
print("Pop fruit =>",fruit)

#แบบบอก Index ใช้ del()
del fruit[1]
print("Del fruit =>",fruit)
#ถ้าไม่ระบุ Index จะลบทั้ง list    del fruit

#แบบเคลียร์ทุกสมาชิก(ทำให้เป็นlistว่าง) clear()
fruit.clear()
print("Clear fruit",fruit)



#คัดลอกlist  copy()
#Number = [1, 2, 3, 4, 5, 6]
x=[]
x = Number.copy()
print("Copy Number to x =>",x)

#รวมสมาชิก
allgroup = Number+name
print(allgroup)
#รวมListแบบไม่ต้องสร้างListใหม่
name.extend(Number)
print("Extend name and Number =>",x)


#หาสมาชิกที่กำหนดว่ามีกี่ตัว
NumBer_Xor = [1, 2, 3, 4, 5, 6, 7, 6, 4, 6, 24, 2, 6]
Xor = NumBer_Xor.count(6)
print("เลข 6 มี =>",Xor,"ตัว")