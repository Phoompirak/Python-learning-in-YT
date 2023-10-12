"""
Set
ไม่สามารถแก้ไขข้อมูลได้
ป้อนข้อมูลใหม่ได้เรื่อย
ป้อนข้อมูลซ้ำไม่ได้
เรียงลำดับไม่แน่นอน(ไม่สามารถระบุindexเพื่อแสดงผลได้)


""" 

#แบบปกติ
fruit = {"มะม่วง", "มะขาม", "มะยม", 50, True}
print(fruit)

#constructor เปลี่ยนTypeได้
fish=set(["ปลาดุก", "ปลาหมอ", "ปลาดุก"])
print(fish)

#เพิ่มข้อมูลเรื่อยๆ
fruit.add("ทุเรียน")
fruit.add("สัปปะรด")
fruit.add(99)
print(fruit)
#เพิ่มหลายอย่างพร้อมกัน
fruit.update(["ตะไคร้", "โหระพา", "ริดชาร์ด"])
print(fruit)

#แปลงเป็นListไม่ได้
list(fruit)
print(type(fruit))

#ดึงสมาชิกออกมาดูอีกแบบ
for item in fruit:
    print("ขข้อมูล -->", item)

print(len(fruit))

#เช็ค
if "มะเฟือง" in fruit:
    print("มีมะเฟืองอยู่ในfruit")
else:
    print("ไม่มีมะเฟืองในfruit")
#เขียนสั้นๆ
print("มะเฟือง" in fruit)

#ลบข้อมูล  ถ้าลบทั้งตัวแปรใช้ del
fruit.remove("มะขาม")
fruit.discard("ทุกคน") #ลบข้อมูลได้เหมือนกันแค่ถ้าไม่เจอสมาชิกแล้วจะไม่Error
print(fruit)