# OOP - Object oriented program
#คืออะไร OOP คือ “การเขียนโค้ดโดยใช้ สิ่งของ (Object) เป็นพระเอก”

#ทุกสิ่งในโลกสามารถเป็น “object” ได้
#เช่น “นักเรียน” → มีชื่อ, อายุ, และสามารถ “พูด”, “กินขนม”, “นอน” ได้ = เป็น Object 🎒

#| Function style          | OOP style                             |
#| ----------------------- | ------------------------------------- |
#| ใช้แค่ฟังก์ชัน              | ใช้ **class** สร้าง object               |
#| ไม่มีการจำตัวตน            | ทุก object มีคุณสมบัติของมันเอง            |
#| เขียนแยก ๆ กระจัดกระจาย    | รวมข้อมูล + พฤติกรรมไว้ใน class เดียว      |

'''ตัวอย่างแรก

class Student:
    def __init__(self, name, age):  <<<# สร้างฟังชั่น _init_(กำหนดให้:self รับค่า>>, name, age)  
    ***เพิ่มเติม _init_ คือฟังชั่นสร้าง object/self คือตัวแทนของ object นั้นๆ
    
        self.name = name  <<<# ใช้ค่า self + (.name) = name  รับค่าชื่อ
        self.age = age   <<<# ใช้ค่า self  + (.age) = age รับค่าอายุ

    def introduce(self):   <<<# สร้างฟังชั่น introduce(  ค่า self):
        return f"My name is {self.name}. I'm {self.age} years old."  <<<# ให้คืนค่า โดยการ print" my name is {self.name}. i'm {self.age} บลาๆๆ

# สร้าง object
s1 = Student("Ezz", 21)  ##### เมื่อกำหนดclass เสร็จแล้ว ก็เอามาใส่ ตัวแปร s1 เป็นการใส่ object เข้าไปในตัวแปร
print(s1.introduce()) ### *** สังเกตุว่าคำสั่ง print ให้ print: object introduce() ที่เก็บอยู่ในตัวแปร s1 

'''

# OOP มี 4 เสา ที่ต้องรู้
# Encapsulation    - คือการซ่อนข้อมูลภายใน object ไม่ให้คนอื่นมาแกะมั่วๆ เราเข้าถึงผ่าน method เท่านั้น
# Inheritance      - คือการสืบทอดclass หรือ เอาคุณสมบัติจาก class เก่ามาใช้ได้เลย
# Polymorphism     - คือ method เดียวกัน ทำงานต่างกันได้ตาม object
# Abstraction      - คือ ซ่อน “วิธีทำ” ไว้ แล้วให้คนใช้แค่ “สิ่งที่ต้องการ”


# *** Encapsulation - การซ่อนข้อมูลภายใน object ***
# สมมุติว่าเราสร้าง class BankAccount ขึ้นมาให้ลูกเก็บเงิน
'''
ตัวอย่างแบบแรก ที่ไม่ได้ใช้ Encapsulation
'''
#class BankAccount:
#    def __init__(self):
#        self.balance = 100

#acc = BankAccount()
#acc.balance = -9999  # โอ้ยยย โดนแฮก!
#print(acc.balance)

#ใครก็แก้ balance ได้ = ไม่ปลอดภัยเลย 😱


'''
ตัวอย่างแบบที่สอง ใช้ Encapsulation
'''
#class BankAccount:
#   def __init__(self):
#        self.__balance = 100  # 🔒 ใส่ __ เพื่อซ่อน

#    def deposit(self, amount):
#        self.__balance += amount

#    def get_balance(self):
#        return self.__balance

#acc = BankAccount()
#acc.deposit(50)  # เติมเงิน
#print(acc.get_balance())  # ✅ ดูยอดเงิน = 150

'''
แล้ว __balance มันคืออะไร?
การใส่ __ (2 ขีด) คือทำให้ ตัวแปรนี้ private

คนอื่น ไม่สามารถเข้าถึงตรง ๆ ได้ ต้องผ่าน method ที่เราสร้างไว้ เช่น .get_balance()
'''

#สรุปสั้น ๆ เสาแรก: Encapsulation
#เปรียบเทียบชีวิตจริง	โค้ดที่เกี่ยว
#บัตร ATM	.deposit(), .get_balance()
#ไม่ให้เข้าถึงเงินโดยตรง	self.__balance

#  แบบฝึกหัด ข้อที่ 1: สร้าง class Counter
#จงสร้าง class ที่ชื่อว่า Counter
#มีตัวแปร __count เริ่มต้นที่ 0
#มี method:

#increment() → บวกเพิ่มทีละ 1

#get_count() → ส่งค่าปัจจุบันออกมา

class Counter():
    def __init__(self): 
        self.__count = 0
    
    def increment(self):
        self.__count += 1
        
    def get_count(self):
        return self.__count
    
c = Counter()
c.increment()
c.increment()
print(c.get_count())   



#ข้อที่ 2: สร้าง class PasswordVault
#สร้าง class PasswordVault ที่เก็บรหัสผ่าน (private)
#มี method:

#set_password(pw) → เก็บรหัส

#check(pw) → ถ้า pw ตรงกับรหัสเดิม ให้ return "Access Granted"

# ตัวอย่างการใช้งาน
#vault = PasswordVault()
#vault.set_password("secret123")
#print(vault.check("wrong"))     # Expected: None
#print(vault.check("secret123")) # Expected: Access Granted


class PasswordVault():
    def __init__(self):
        self.__password = ""
        
    def set_password(self, pw):
        self.__password = pw
        
    def check(self, pw):
        if pw == self.__password:
            return "Access Granted"
        
vault = PasswordVault()
vault.set_password("secret123")

print(vault.check("wrong"))
print(vault.check("secret123"))




#ข้อที่ 3: บัญชีแบบมีถอน
#ปรับ BankAccount ให้มี:

#withdraw(amount) → ถ้ายอดเงินพอ ให้ถอน, ถ้าไม่พอให้ return “Insufficient funds”

# ตัวอย่างการใช้งาน
#acc = BankAccount()
#acc.deposit(100)
#print(acc.withdraw(50))  # OK
#print(acc.withdraw(100)) # Expected: Insufficient funds

class BankAccount():
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        else:
            self.__balance -= amount
            return f"Withdraw {amount}" 
        
    def get_balance(self):
        return self.__balance
    
acc = BankAccount()
acc.deposit(100)

print(acc.withdraw(50))  
print(acc.withdraw(200)) 





#ข้อที่ 1: SecretNote
#จงสร้าง class SecretNote
#มีตัวแปร private __note

#write_note(text) → บันทึกข้อความ

#read_note() → ส่งข้อความกลับมา

#ถ้าโน้ตว่างอยู่ ให้ return "No note yet"

class SecretNote():
    def __init__(self):
        self.__note = ""
        
    def write_note(self, text):
        self.__note = text
        
    def read_note(self, text):
        if text == self.__note:
            return (f"yes we have note: {self.__note}")
        else:
            return "No note yet"
sn = SecretNote()
sn.write_note("hi")

print(sn.read_note("python"))
print(sn.read_note("hi"))

sn.write_note("ok")
print(sn.read_note("ok"))

#ข้อที่ 2: TemperatureSensor
#class นี้ใช้เก็บค่าอุณหภูมิ (private: __temp)

#set_temp(value) → เซ็ตค่า temp

#get_temp() → ถ้า temp > 40 ให้ return "Warning: Overheat!"
#ถ้าไม่เกิน ให้ return ค่า temp ปกติ
class TemperatureSensor:
    def __init__(self):
        self.__temp = 0
        
    def set_temp(self, value):
        self.__temp = value
        
    def get_temp(self, value):
        if value > 40:
            return (f"Warning: Overheat!")
        else:
            return f"Temperature: {self.__temp}"
ts = TemperatureSensor()
ts.set_temp(30)

print(ts.get_temp(45))
print(ts.get_temp(1))

#ข้อที่ 3: ScoreManager
#class นี้ไว้เก็บคะแนน

#add(score) → เพิ่มคะแนนเข้าไป (สะสม)

#get_score() → return คะแนนรวม

#ถ้ามีใครพยายามแก้ __score ตรง ๆ → ต้องไม่ส่งผลกระทบ

#💡 Hint: ซ่อน __score และเข้าถึงเฉพาะผ่าน method เท่านั้น


class ScoreManager():
    def __init__(self):
        self.__score = 0
    
    def add_score(self, score):
        self.__score += score
    
    def get_score(self):
        return self.__score

    
sm = ScoreManager()
sm.add_score(100)

print(sm.get_score())



#### ***** ที่ผิดบ่อยๆคือ TypeError: ................    takes 1 positional argument but 2 were given
#### แปลว่า def (ชื่อobject(parameter)) <<<<< ตรง parameter นี้น่ะ ถ้ามี แค่ self คือรับแค่ค่าเดียว หากมีค่าอื่น จะขึ้น error ทันที เช่น
### สมมุติว่า def name(self)   #สมมุติว่า ตรง self = Jirath
### แล้วเราลอง print(name(self))  #ตรงนี้ผลลัพธ์ออกมาแน่นอน คือ Jirath
### แต่หากทะลึ่ง เขียนเป็น print(name(อะไรก็ได้)) # error ทันที เพราะค่า self คือ Jirath แต่หากใส่ค่าอื่น เข้าไปคือพัง