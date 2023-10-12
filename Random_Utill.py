import random

# for i in range(15):
#     """
#     random.uniform = ทศนิยมเยอะๆจุด
#     random.randrange 
#     random.randint = จำนวนเต็ม
#     random.shuffle() = สลับตำแหน่งในลิสต์(returnค่าออกมาเอง)
#     """
#     items = [1,2,3,4,5,"A","B","C"]
#     x = random.choice(items) # start,stop,step
#     print(x)

#รหัสผ่าน ATM = 132
ATM_PASSWORD = "251250"
result = "" #สำหรับเก็บผลลัพธ์

while result != ATM_PASSWORD:
    result = ""
    #lenเพื่อดูว่าถูกไหมแบบทีละตัว
    for letter in range(len(ATM_PASSWORD)):
        list_number = random.choice("0123456789") #abcdefghijklmnopqrstuvwxyz
        result = "".join(list_number)+str(result)
        print(f"Sreach = {result}")
print(f"CRACK PASSWORD IS {result}")