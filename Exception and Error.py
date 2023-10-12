# Exception ข้อผิดพลาด
# Error syntaxผิด
"""

try:
    คำสั่งรันโปรแกรมปกติ
except:
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด

"""
#ValueError => ค่าผิดพลาด
#ZeroDivisionError
"""
while True:
    try:
        name= input("ป้อนชื่อผู้ใช้โปรแกรม :")
        if name == "ภูมิ":
            raise Exception("มีชื่อในระบบแล้วนะครับ")
        number = int(input("ป้อนเลขตัวที่ 1:"))
        number1 = int(input("ป้อนเลขตัวที่ 2:"))
        #ตรงนี้จะเริ่มมีError
        score = number/number1
        if number1 == 0 and number == 0:
            break
        if number and number1 < 0:
            #ทำErrorใช้เอง
            raise Exception("ไม่สามารถป้อนต่าติดลบได้นะครับ")
        print(f"{number}หาร{number1}={score}")

    except ValueError:
        print("ต้องป้อนตัวเลขถึงจะหารได้")
    except ZeroDivisionError:  #ห้ามหาร 0 กับ10
        print("ห้ามหารด้วยศูนย์นะแจ๊ะ")
    except TypeError:
        print("ชนิดข้อมูลไม่ตรงกัน ผิดจากในโปรแกรม")

    #ถ้าจำไม่ได้ว่าต้องเช็คอะไรล่ะ ให้โปรแกรมบอกเราเลย
    except Exception as e:
        print(e)
    else:
        print("โอนเงินสำเร็จ")

    #Finally
    finally:
        print("ทำงานต่อไป...\n")
"""

#โปรแกรมบัญชีธนาคาร

#Data
account = {"Mr.A":5000, "Mr.B":0}

def getBalne():
    print("ยอดเงินคงเหลือในบัญชี :",account)

def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception ("ต้องป้อนตัวเลขเท่านั้น")
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องมากกว่า0")
    print("ฝากเงินเข้าบัญชี A:",account)
    account["Mr.A"]+=money

def withdraw(money):
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องมากกว่า0")
    if money>account["Mr.A"]:
        raise Exception ("จำนวนเงินไม่เพียงพอ")
    print("ถอนเงินจากบัญชี A:",money)
    account["Mr.A"]-=money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception ("ต้องป้อนตัวเลขเท่านั้น")
    if money<=0:
        raise Exception ("ค่าตัวเลขต้องมากกว่า0")
    if account["Mr.A"]<=money:
        raise Exception ("ยอดเงินของคุณน้อยกว่าจำนวนที่กรอก")
    print("ทำการโอนเงินไปยังบัญชี B :",money)
    account["Mr.B"]+=money
    account["Mr.A"]-=money

"""
try:
    getBalne()
    deposit(1000)
    getBalne()
except Exception as e:
    print(e)
"""

try:
    getBalne()
    transfer(999.44)
    getBalne()
except Exception as e:
    print(e)