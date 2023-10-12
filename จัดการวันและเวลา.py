# Module Date / Time
import datetime

result = datetime.datetime.now()
print(result.year)
print(result.month)
# print(result)

newdate = datetime.datetime(2020, 6, 20, 15)  # yyyy,m,d
print(newdate)

# รูปแบบแสดงผลใหม่
print("เริ่มต้น =", result)
print(result.strftime("%x"))  # mm/dd/yyyy สั้น
print(result.strftime("%c"))  # D/M/Number/Time
print(result.strftime("%H:%M:%S %p"))  # Time/Minute/Second/AM.,PM.
print(result.strftime("%j"))  # 1-366
print(result.strftime("%a"))  # Day สั้น
print(result.strftime("%A")) #Day เต็ม
print(result.strftime("%w")) #0=Sunday, Monday=1
print(result.strftime("%d")) #วันที่
print(result.strftime("%b")) #เดือนแบบสั้น
print(result.strftime("%B")) #เดือนแบบยาว

print(result.strftime("%d %A %B %Y"))

#ว/ด/ป
print(result.strftime("%d / %m / %Y"))