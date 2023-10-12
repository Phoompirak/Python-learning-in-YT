#Tuple เป็นฟังชั่นไว้เก็บข้อมูลหลายข้อมูลคล้ายๆListแต่แก้ไขไม่ได้
tup=(1,2,3,4,"Ruksika","while444","Phoompirak",True,3.99,4.99,5.99)

#ดูTypeได้เหมือนเป็นชนิดข้อมูลๆนึงเลย
print(type(tup))
#เลือกแสดงข้อมูลบางตัว
print(tup[2:5])
print(tup[:-1])

#Tuple แก้ไขไม่ได้แต่แปลงเป็นList แล้วค่อยแก้ข้อมูลได้
lis=list(tup) #แปลงTupleเป็นList จะแปลงกลับก็แค่สลับคำ
lis[1]="อำนาจเจริญ"
print(lis)

for item in tup:
    print("สมาชิกของtup=>",item)

if "ทุเรียยน" in tup:
    print("ทุเรียนเป็นสมาชิกtup")
else:
    print("ทุเรียนไม่เป็นสมาชิกtup")
if "True" in tup:
    print("Trueมีในtup")
else:
    print("Trueเป็นสมาชิกTrue")

#ดูจำนวนสมาชิก
print("นับเริ่มที่ 0-7 รวมเป็น=>",len(tup))

#สร้างtupleต้องมีเครื่อง , ไม่งั้นมันอาจจะมองเป็นstr
x=("Phoom300x",)
print("Typeของx=>",type(x))
#ถึงจะเอาข้อมูลมาเพิ่มใส่ในTupleได้
name=("Phoompiral","Atriwat")
new=("Natty",) 
name=name+new #หรือจะแปลงtypeตอน+ก็ได้  tuple(new)
print("Typeของname",type(name))

#การลบข้อมูลออกทั้งหมดด้วย del
del x


#เอาสมาชิกออก
print("Before pop=>",tup)
lis=list(tup)
lis.pop()          #หรือจะใช้ฟังชั่นอะไรที่มีในListก็ได้เพราะแปลงเป็นListแล้ว remove,clear
print("After pop=>",lis)

#เช็คว่าเจอที่ index ที่เท่าไหร่
z=tup.index(4)
print(z)

#สลับค่าTuple
x=(50,60)
y=(88,99)
print("ก่อนสลับค่า :",x,y)
x,y=y,x
print("หลังสลับค่า :",x,y)

#เปลี่ยนสมาชิกตัวอักษรให้เรียงเป็นขัอความ
Character=('P','h','o','o','m')
name="".join(Character)
print(name)

#reverse tuple
x=(100,20,30,15,10,5,500)
print("Before :",x)

y=tuple(reversed(x))
print("After :",y)
#ถ้สReversed Str จะแยกข้อความออกเป็นตัวอักษรเดี่ยว
N="Phoompirak"
M=tuple(reversed(N))
print(M)