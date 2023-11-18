"""
Python string methods
จัดการข้อความ
"""
P = "Phoom\t300X\tChannel"
Phoom = "     5Phoom5     "

""" ###เปลี่ยนแปลงข้อความ### """
# พิมพ์ใหญ่ตัวแรกเท่านั้น
print("capitalize = ",P.capitalize())

# ตัวพิมพ์เล็กทั้งหมด
print("lower = ",P.lower())
# ใหญ่
print("Upper = ", P.upper())

# เลือกความกว้างของเว้นวรรค
print("expandtabs = ",P.expandtabs(2))

# รวมข้อความโดยใช้#เป็นตัวคั่น
print("Join = ", "#".join(P))

# ลบเว้นวรรคด้านซ้ายหรือขวา l=left, r=right
print("lstrip = ", Phoom.lstrip())
print("rstrip = ", Phoom.rstrip())

# แยกข้อความที่ต้องการและเปลี่ยนเป็นtuple
print("Partition = ", P.partition("300X"))

# เปลี่ยนข้อความที่ระบุเป็นข้อความใหม่ที่ระบุ
print("Replace = ", P.replace("Phoom", "Apple")) # string.replace(oldvalue, newvalue, count)

# แยกข้อความออกจากกันด้วยตัวอักษรที่มีอยู่
print("Split = ", P.split("\t"))


""" ##เช็ค## """
number = "1234"
# เช็คว่าเป็นข้อความไหม
print("Isalpha = ", P.isalpha())
# มี(a-z), (0-9), _, ไม่ขึ้นต้นด้วยตัวเลขและเว้นวรรค เท่านั้นไหม
print("Isidentifier = ", P.isidentifier())

#เช็คว่าเป็นตัวอักษรหรือเลขไหม(ไม่รวมเว้นวรรค)
print("Isalnum = ",P.isalnum())

# อักขระเป็นตัวเลขไหม
print("Isdigit = ", number.isdigit())
print("Isnumeric = ", number.isnumeric())

# True ถ้าอักขระทั้งหมดเป็นspace
print("Isspace = ", P.isspace())


# เป็นอักษรasciiไหม
print("Ascii = ", P.isascii())

# เช็คข้อความที่ป้อนว่าIndexที่เท่าไหร่
print("Index = ", P.index('o'))

# เช็คจำนวนตัวอักษรหรือข้อความที่ต้องการ
print("count = ",P.count("h")) #string.count(value, start, end)

# เช็คstrตัวแรกว่าใช่ตามที่ระบุไหม (เลือกได้ไ ไม่จำเป็นต้องเป็นแค่ต้นแรกสุด)
print("Startswith = ", P.startswith("P")) #string.startswith(value, start, end)

