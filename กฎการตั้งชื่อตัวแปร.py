# ทดลองเล่นๆ

''' ทดสอบคอมเม้นหลายบรรทัด
(Multi Line Comment)
'''
print("Villager")
print("All")
print("Bee")
print("OMG...")
print("Hello world")
print("Yare yare")
print("And")
print("welcome to new york")
print("Wil")
print("Zoo")
print("Unity")
print(True)
print(False)


"""
กฎของการตั้งชื่อ(เขียนตัวแปร)
1.ใส่ตัวเลข ตัวอักษร เครื่องหมาย
2.ห้ามขึ้นต้นด้วยตัวเลขและสัญลักษณ์(ยกเว้นอันเดอร์สกอร์_)
3.ห้ามซ้ำกับKeywords(เช่น class,def,Flase,True,for,is,in,None)
4.case sensitive(ตัวพิมพ์เล็กกับใหญ่แตกต่างกัน)

"""

name="A"
NAME="B"
nAmE="C"
print(name)
print(NAME)
print(nAmE)



#int=ตัวเลข   str=ตัวหนังสือ   float=ทศนิยม
x=10
y=3.14
z="20"

#แปลงตัวหนังสือเป็นตัวเลข(แปลงstrหรือfloatที่เป็นตัวเลขที่ไม่สามารถดำเนินการทางคณิตศาสตร์ได้ให้เป็นตัวเลขที่ดำเนินการทางคณตศาสตร์ได้)
phoom=x+int(z)
print(phoom)
print(type(phoom))

#แปลงตัวเลขเป็นตัวหนังสือ(แปลงintหรือfloatให้เป็นstrข้อความที่ไม่สามารถนำมาคำนวณทางคณิตได้)
pi=str(x)+z
print(pi)
print(type(pi))

#แปลงตัวเลขเป็นทศนิยม(แปลงintหรือstrที่เป็นfloatตัวเลขให้เป็นทศนิยม)
print(float(z))
print(float(x))

#แปลงทศนิยมให้เป็นตัวเลขธรรมดา(แปลงfloatให้เป็นint)
print(int(y))

last=int(input("ป้อนชั้นพีระมิดของคุณ :"))


for row in range(1, last+1):
    for column in range(1, row+1):
        print(column, end="")

    print((" "))