#เปิดไฟล์
#open("ชื่อไฟล์หรือpath","โหมด","encode(ไว้ทำให้ภาษาอื่นอ่านได้)")
try:
    fr = open("D:\python\หัดอ่านไฟล์Text\student.txt","r",encoding="utf-8")
    print(fr.read())
    fr.close
    
except Exception as e:
    print(e)
except FileNotFoundError:
    print("หาไฟล์ไม่เจอจร้า")