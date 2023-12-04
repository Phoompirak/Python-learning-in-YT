import math

x=min(3,4,5,-10,30,40)
print(f"ค่าน้อยสุด = {x}")
y=max(3,4,5,-10,30,40)
print(f"ค่ามากสุด = {y}")
z=abs(-50)
print(f"ค่าสัมบูรณ์ของz = {z}")
p=pow(5,3)
print(f"5ยกกำลัง3 = {p}")

#รูท
result=math.sqrt(64)
print(f"ค่ารูท64 = {result}")

#ปัดเศษทศนิยม
score=80.46
print(f"ปัดเศษลง = {math.floor(score)}")
print(f"ปัดเศษขึ้น = {math.ceil(score)}")
print(f"ค่าPIEคงที่ = {math.pi}")

#ตรีโกณมิติ
#ต้องแปลงก่อนเพราะค่าเริ่มต้นเป็นเรเดียน
convert=math.radians(30) # degree => radians
print(f"เรเดียน = {convert}")
sin=math.tan(convert) # radians
print(f"ค่าsin = {sin}")

#หาระยะห่างพื้นที่
piont1 = [5,4]
piont2 = [5,13]
#d = |x1-x2|
d = math.dist(piont1,piont2)
print(f"Distance => {d}")

#หาค่าลอการิทึม (Log)
l1 = math.log2(32) #เปลี่ยนเลขท้ายlogได้ เช่น math.log10()
print(f"Logarithm => {l1}")