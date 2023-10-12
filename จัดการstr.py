 # index => 0
 # มีทั้งหมด 24 ตัวที่ใส่ไปเว้นวรรคมี 7 ตัว
P = "   Phoompirak Phoom Channel   "  

# ก่อนถึงตำแหน่งสุดท้าย เช่น ถ้าใส่3จะถึงแค่2 (นับเว้นวรรคด้วย)
print(P[0:13]) 

#ถ้าจะนับจากข้างหลังก็ใส่ติดลบ -
print(P[-10:])

#การใช้Lenเอาไว้ดูว่าstrมีกี่ตัว
print(len(P))

#การใช้Stripเพื่อลบช่องว่างซ้ายขวาออก
#P = P.strip()
#print(len(P))

#การใช้lstripเพื่อลบช่องว่างข้างซ้ายและลบขวาใช้rstrip
P = P.lstrip()
print(len(P))

#การแปลง Case ของ String
print(P.upper())  #ตัวพิมพ์ใหญ่ทั้งหมด
print(P.lower()) #ตัวพิมพ์เล็กทั้งหมด
print(P.capitalize()) #ให้ตัวพิมพ์ใหญ่แค่ข้างหน้าสุด

#การแทนที่คำ
print(P.replace("Phoom","Aharen")) #ใช้แทนที่คำ
print(P.replace("Phoom","Aharen",1)) #ใช้แทนที่คำแต่เลือกแทนที่่แค้่คำแรก


#ใช้ตัวแปรใหม่เพื่อไม่ให้งง?
#เช็คข้อความ => True , False
test = "ไปซื้อข้าวและอาหารที่ตลาด"

x = "ข้าว" in test #เช็คว่ามีคำว่าข้าวอยู่ในตัวแปรtestไหม
print(x)

#ถ้า x เป็นTrueก็จะทำงานต่อไปได้   สิ่งที่ให้ทำต่อคือแทนคำว่าไข่ลงไปแทนคำว่าข้าว
if x:
  test=test.replace("ข้าว","ไข่") # สามารถใส่ Not เพื่อให้ทำงานขั้วตรงข้าม


print(test)



#การต่อ String โดยใช้เครื่องหมาย + (Concatinate)

fname = "Phoompirak"
lname = "karajak"
age = "15"


fullname = fname+lname+age
print(fullname+"555")
print("ชื่อ :"+fname+"\tนามสกุล :"+lname+"\tอายุ :"+age)

#การจัดรูปแบบการแสดงผล format + {}

one = "Phoompirak"
two = "karajak"
three = "15"
four = 500.12345

text = "ชื่อ :{0}\tนามสกุล :{1}\tอายุ :{2}\nอาชีพ :{3}\tเงินเดือน :{4:.2f}"
print(text.format(one,two,three,"โปรแกรมเมอร์",four))

#นับจำนวนคำในประโยค count = นับ

fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด จะแวะไปสวนทุเรียนด้วย"

print(fruit.count("ทุเรียน"))

#เช็คคำข้างหน้าว่าใช่ตามที่กำหนดไหม Startswith
Name = "นายกอไก่ ใจดี"
print(Name.startswith("นาย"))

#เช่นการดูว่าสิ่งที่ป้อนที่ใช่นายไหม
Your = str(input("ป้อนคำนำหน้าของคุณ :"))

if Your.startswith("นาย"):
  print("เป็นเพศชาย")

elif Your.startswith("นางสาว" and "นาง"):
  print("เป็นเพศหญิง")

else :
  print("ไม่รู้")


#การเช็คแค่ตอนจบจนถึงตัวที่กำหนด Endswith
#กำหนดเลขหวยที่ออกเพือ่ให้คนมาตรวจ
#กำหนดให้คนมาตรวจหวยแค่ 2 ตัวล่าง

หวยที่ออก = "123456"

หวยที่คุณซื้อ = str(input("กรุณาป้อนหวยของคุณ :"))

if หวยที่คุณซื้อ.endswith("56"):
  print("คุณถูกหวย")

else :
  print("คุณถูกหวยแดก!!")
