try:
    # fw=open("D:\python\หัดอ่านไฟล์Text\Score_student.txt","w",encoding="utf-8")
    # while True:
    #     studentid=input("ป้อนรหัสนักเรียน: ")
    #     if studentid == "exit":
    #         break
    #     score=input("ป้อนคะแนนสอบ: ")
    #     fw.writelines(studentid+"\t"+score+"\n")
    # fw.close()


    fr = open("D:\\python\\หัดอ่านไฟล์Text\\Score_student.txt","r",encoding="utf-8")
    
    #"w" จะเขียนทับไฟล์Grade.txtตัวเก่าเลย
    fw = open("D:\\python\\หัดอ่านไฟล์Text\\Grade.txt","w",encoding="utf-8")
    for line in fr.readlines():
        score = int(line[-4:].strip()) #ลบช่องว่องทั้งหมด
        studentid = line[:-4]
        if score>=80:
            grade="A"
        elif score>=70 and score<=79:
            grade="B"
        elif score>=60 and score<=69:
            grade="C"
        else:
            grade="F"
        print(f"รหัส = {studentid} คะแนน = {score} grade = {grade}")
        fw.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fr.close()
    fw.close()

except Exception as e:
    print(e)