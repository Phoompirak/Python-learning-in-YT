#การสร้าง Dict
"""
                 โครงสร้าง

 ชื่อตัวแปร = {key:value, key:value, key:value} #เมื่อมี : ก็จะรู้เองว่าเป็นDict
 ต้องตั้งชื่อแทนindexเพื่อเรียกใช้ข้อมูล

"""
colors = {"red":"สีแดง","yellow":"สีเหลือง", "green":"สีเขียว", 98:"บ้านวิโรจน์", 100:"บ้านป่าตู่", True:"อะดชัลี่ญะ", False:"ไม่เห็นจะอัดชารียะเล"}
city = {"bangkok":"กรุงเทพ"}
animal = dict({"ไก่":"chicken", "แมว":"cat", "dog":"น้องหมา"})

#การเรียกใช้
print(animal["ไก่"])
print(city["bangkok"])
print(colors.get(98)) #เรียกใช้อีกแบบ
print(colors.get(True))

#เพิ่มข้อมูล+เปลี่ยนข้อมูล
colors.update({"orange":"สีส้ม", "red":"แดง"})
print(colors)

for k,v in colors.items(): #ถ้าอยากได้valueก็ colors.value() ได้ทั้งkey:valueก็ colors.item()
    print("Key :",k,"    Value :",v)

#ลบข้อมูล
colors.pop("red") #เลือกค่า
colors.popitem() #ลบตัวท้ายพึ่งเพิ่มมา
print(colors)

#ลบทั้งสมาชิก
colors.clear()
print(colors)

#ก็อปข้อมูล
x=animal.copy()
print("x :",x)



#โจทย์Dictซ้อนDict
market={
    "ร้านป้าพัง":{
        "name":"ป้าพัง",
        "menu":["กะเพราไก่","ก๋วยเตี๋ยว"],
        "zone":["ตะวันออก",""],
    },
    "ร้านลุงป้อม":{
        "name":"ลุงป้อม",
        "menu":["โซดา","เบียร์"],
        "ZONE":"ทางเข้าตลาด",
    },
    "ร้านน้าตู่":{
        "name":"น้าตู่",
        "menu":["หญ้าสด","หญ้าหวาน","หญ้าแห้ง"],
        "zone":"ข้าง 7-11",
    }
}

print(market["ร้านลุงป้อม"]["menu"])

if "หญ้าหวาน" in market["ร้านน้าตู่"]["menu"]:
    print("ร้านน้าตู่มีหญ้าหวานขาย")
else:
    print("ไม่มีหญ้าหวาน ")