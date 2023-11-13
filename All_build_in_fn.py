#Build in Function = ฟังก์ชั่นในตัว

"""### หลักๆ ###"""
#Isinstance
#x = isinstance("Hello", (float, int, str, list, dict, tuple))
x = 14
print(f"เป็นชนิดข้อมูลที่ว่าไหม = {isinstance(x, int)}")
#Map
def my_func(a):
    return len(a)
x = map(my_func, ('apple', 'banana', 'cherry'))
print(list(x))
#Reverse str
print("กลับข้อความ =", sorted("Phoom", reverse=True))
#sum หาผลรวมของเลขในlist
a=[1, 2, 3, 4, 5, 6]
print("sum ผลรวมList = ", sum(a))



print("\n ##เพิ่มเติม## \n")
"""เพิ่มเติม"""
#หาค่าสัมบูรณ์ของตัวเลข
print("ค่าสัมบูรณ์ของ -105 = ", abs(-105))

"""
all, any = เหมือนตัวบ่งปริมาณในตรรกศาสตร์
all = ต้องจริงทุกกรณีถึงจะเป็นจริง
any = ถ้าจริงแค่ตัวเดียวจะส่งค่าจริงออกมา
"""
#all
bool_list = [True, True, True]
print(f"ใช้ all เช็ค bool_list = {all(bool_list)}")
#any
my_data = [2,6,4,5,8]
is_even = any(item % 2 == 0 for item in my_data)
print(f"ใช้ any เช็ค my_data = {is_even}")

#เปลี่ยน ascii เป็น characters
print(ascii("Hello å %@"))

#แสดงเลขฐาน2 ของเลขที่ป้อนมา
print(f"แปลง 123 เป็น binary = {bin(123)}")

#โชว์ค่า bool ของ Object
print(f"ค่า bool ของ 4!=1 = {bool(4!=1)}")

#ค่าByte
print(f"Bytes = {bytes(4)}")

#เปลี่ยนอักษร เป็น Unicode code = chr(number)
print("Unicode code =", chr(97))

#เปลี่ยนList เป็น Index และ Value ซึ่งส่งค่าออกมาเป็นTuple
#Syntax = enumerate(iterable, start)
y = ('apple', 'banana', 'cherry')
y = enumerate(y)
print("Enumerate =", list(y))

#filter(function, iterable)
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)

for x in adults:
    print(f"Filter กรองเลขที่มากกว่า18 = {x}")

#เเปลงค่า format(value, format)
y = format(0.5, '%')
x = format(525, 'x')
print(f"format 0.5 to % = {y} and x to 'x'format = {x}")