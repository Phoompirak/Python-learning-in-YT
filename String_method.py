"""
Python String Methods
= ชุดวิธีการในตัวที่คุณสามารถใช้กับสตริงได้
"""
#ตัวพิมพ์ใหญ่แค่ตัวแรก
P = "pHoOmPiraK KArAJak"
print(f"ตัวพิมพ์ใหญ่ตัวแรก ={P.capitalize()}")

#พิมพ์เล็กทุกตัว
print(f"พิมพ์เล็กทุกตัว = {P.casefold()}")

#ทำให้อยู่ตรงกลาง space (หรือเปลี่ยนspaceเป็นอย่างอื่นก็ได้)
#Syntax = string.center(length, character)
print(f"ตรงกลาง = {P.center(20)}")

#เช็คว่า string ที่กำหนดมีกี่ตัว
print("k มีกี่ตัว =", P.count("K"))

#จริง ถ้าตัวสุดท้ายเหมือนกับตัวที่กำหนด
#Syntax = string.endwith(value, start, end)
print("เช็คตัวท้าย =", P.endswith("."))

#หาตัวที่ต้องการ
#Syntax = string.find(value, start, end)
print("หา raK =", P.find("raK"))
