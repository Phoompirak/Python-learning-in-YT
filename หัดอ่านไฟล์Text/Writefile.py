#อ่านไฟล์เหมือนกับReadแค่เปลี่ยนโหมด
try:
    #เขียนทับข้อความเก่าใช้ "w" 
    #"a" คือ เขียนเพิ่ม
    fw=open("D:\python\หัดอ่านไฟล์Text\Score.txt","a",encoding="utf-8")
    string = input("ป้อนข้อความของคุณ :")
    fw.writelines(string+"\n")

    fr = open("D:\python\หัดอ่านไฟล์Text\Score.txt","r",encoding="utf-8")
    #ถ้าใช้ line จะดึงมาทีละตัวอักษร
    lines = fr.readlines()
    s = 1
    for x in lines:
        print(f"บรรทัดที่{s}=>{x}")
        s+=1
    fr.close()
    fw.close()

# try:
    # fw = open("D:\python\หัดอ่านไฟล์Text\Score.txt","w",encoding="utf-8")
    # fw.write("Hello Who?\n")
    # fw.writelines("สาหวาดดีค้าบท่านสมาชิกชมรมคนชอบ...อิ๊ๆ\n")
    # fw.write("Socre stupid :10/10")
    # fw.close()

except FileNotFoundError:
    print("หาไฟล์ไม่เจอจร้า")
