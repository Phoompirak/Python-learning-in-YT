number=[1,2,3,4,5,6,7,8,9,10] #Listมีสมาชิก10คน
fruit=["มะม่วง","มะนาว","มะยม","มะละกอ"]

print("ก่อนเพิ่ม =>",fruit)
#append() นำสมาชิกใหม่มาเพิ่ม ต่อท้าย
fruit.append("มะปราง")
fruit.append("แตงโม")
print("หลังเพิ่ม =>",fruit)

#insert (index,สมาชิกใหม่)
fruit.insert(1,"ทุเรียน")
print("หลังแทรก =>",fruit)

#การลบข้อมุล
#remove
fruit.remove("มะยม")
print("หลังremove =>",fruit)
#pop
fruit.pop() #ใส่สองครั้งก็จะลบตัวล่าสุดสองครั้ง
fruit.pop()
print("หลังpop =>",fruit)
#del
del fruit[2] #กำหนดตัสมาชิกที่จะลบได้ (ถ้าไม่ใส่indexเลยจะลบทั้งสมาชิกลบทั้งตัวแปรออก)
print("หลังdel =>",fruit)
#clear
fruit.clear() #ก็จะไม่มีสมาชิก
print("หลังclear = >",fruit)


#การคัดลอกข้อมูลในList
x=[]
print("สร้างListว่าง",x)
x=fruit.copy()
print("คักลอกข้อมูลด้วยcopy =>",x)

#การรวมข้อมูลList
data=["เอก","ต้น","กัน"]
alldata=number+data
print("รวมListด้วยการ+ =>",alldata)
#รวมListแบบไม่ต้องสร้างListใหม่เพิ่ม
data.extend(number)
print

#การหาสมาชิกที่ชื่อเหมือนกันด้วยCount
Nameall=["Prayut","Peesaded","Phoompirak","Pupongsit","Gayreyei","Phoompirak","Prayut","Phoompirak"]
z=Nameall.count("Phoompirak")
print("ชื่อPhoompirakมีกี่ตัวในList Nameallกันนะ =>",z)


#การเรียงลำดับข้อมูลตัวเลขด้วย Sort,reverse
Number=[]
while True:
    x=int(input("ป้อนเลข :"))
    if x<0:
        break
    Number.append(x)

print("ก่อนเรียง=>",Number)
Number.sort()
print("หลังเรียง=>",Number)
Number.reverse()
print("หลังreverd",Number)
print("จบโปรแกรมเรียงเลขที่ผู้ใช้ป้อน")

#หาค่ามากที่สุด/น้อยที่สุด/ผลรวม
print(max(Number))
print(min(Number))
print(sum(Number))

#หาเลขคู่/คึ่
number=[]
odd=[] #เลขคี่
even=[] #เลขคู๋
while True:
    x=int(input("ป้อนเลขคู่และคี่=>"))
    if x<0:
        break
    if x%2==0:
        even.append(x)
    if x%2!=0:
        odd.append(x)
    number.append(x)
print("เลขทั้งหมด=>",number)
print("เลขคี่=>",odd)
print("เลขคู่=>",even)

#หาเลขคู่คี่อีกแบบ
Lecbers=[12,37,5,42,8,3]
even = []
odd = []
while len(Lecbers) > 0 :
    Lecber = Lecbers.pop() #ลบตัวล่าสุด
    if(Lecber%2 == 0):
        even.append(Lecber)
    else:
        odd.append(Lecber)
print("หาเลขคู่คี่อีกแบบ=>","even=>",even,"odd",odd)

#เรียงชื่อด้วย sort ก็ได้
student=["แก้ว","กร","โดม","โอม","ภูมิ"]
print("ก่อนเรียง=>",student)
student.sort()
print("หลังเรียง=>",student)

#หลังสุดไปหน้าสุด [::-1]
fruit=["มะม่วง","มะพร้าว","มะยม","มะเฟือง"]
print("ก่อนย้อน=>",fruit)
fruit=fruit[::-1]
print("หลังเรียง=>",fruit)


#หาค่าเลขยกกำลัง
Number=[1,2,3,4,5,6,7]
print("ยังไม่ยกกำลัง=>",Number)

#แบบไม่ย่อ
for i in range(len(Number)):
    Number[i]=Number[i]**2 #หรือ Number[i] = Number[i]*Number[i] ก็ได้
print("เลขยกกำลัง=>",Number)

#แบบย่อลดรูป
Number=[i*i for i in Number]
print("ยกกำลังแบบลดรูป",Number)


#จับคู่คำ
"""
Hi , Hello
กร , กัง

"""
greeting=["สวัสดี","Hi","Hello"]
people=["กร","กัง","อีง"]
result=[]
for x in greeting:
    for y in people:
        result.append(x+y)
print(result)

#จับคู่ราคาสินค้า
fruits=["มะม่วงดอง","เกี๊ยว","เงาะกระป๋อง"]
price=["50","10","15"]

for x,y in zip(fruits,price): #หรือจะใช้ ::-1 เพื่อreverse
    print("สินค้า=>",x,"ราคา",y)


#ค้นหาจำนวนอักษรในList
messege=["aa","cba","caa","ddd","bca","caaaa","saas"]
result=[]
for item in messege:
    result.append(item.count("a"))
print(result)