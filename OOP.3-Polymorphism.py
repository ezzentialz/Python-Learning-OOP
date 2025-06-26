#🔮 Polymorphism คืออะไร? (อย่างละเอียดขึ้น)
#Polymorphism มาจากภาษากรีก แปลว่า "หลายรูปแบบ" (Poly = หลาย, Morph = รูปแบบ)

#ในทาง OOP หมายถึง:

#"วัตถุต่างชนิดกัน (แต่มาจากคลาสแม่เดียวกัน หรือมี interface เหมือนกัน) สามารถตอบสนองต่อคำสั่งเดียวกันได้แตกต่างกันไป"

#นึกภาพง่าย ๆ เหมือนปุ่ม "เล่น" (Play) บนเครื่องเล่นต่างชนิดกัน:

#ปุ่ม "เล่น" บนเครื่องเล่นเพลง ก็คือ "เล่นเพลง"
#ปุ่ม "เล่น" บนเครื่องเล่นวิดีโอ ก็คือ "เล่นวิดีโอ"
#ถึงแม้จะเป็นปุ่ม "เล่น" เหมือนกัน แต่การกระทำข้างหลังแตกต่างกัน ขึ้นอยู่กับชนิดของเครื่องเล่นนั้น ๆ ครับ

#ใน Python, Polymorphism มักจะเกิดขึ้นได้ 2 รูปแบบหลัก ๆ:

#Method Overriding: (อันนี้เอสทำไปแล้ว!) คือการที่คลาสลูกเขียน method ที่มีชื่อเหมือนกับคลาสแม่ ทำให้เมื่อเรียกใช้ method นั้นจาก object ของคลาสลูก มันจะเรียก method ของคลาสลูกแทนของคลาสแม่

#ตัวอย่าง: Animal มี speak(), Dog และ Cat override speak() ให้มีเสียงต่างกัน
#Polymorphism with Functions and Collections: คือการที่เราสามารถเก็บ object ที่มาจากคลาสต่างกัน (แต่มี method ชื่อเดียวกัน) ไว้ใน collection เดียวกัน (เช่น list) และสามารถเรียก method นั้น ๆ ผ่าน loop ได้อย่างราบรื่น โดยที่แต่ละ object จะแสดงพฤติกรรมตามที่มัน override ไว้

#ตัวอย่าง: animals = [Cat(), Dog(), Cat(), Dog()] 
# แล้ว for a in animals: print(a.speak()) 
# แต่ละ object จะ speak() ในแบบของตัวเอง
'''
โจทย์: Class Employee → Manager, Developer
เราจะสร้างระบบการทำงานเบื้องต้นของพนักงานในบริษัทครับ

Class Employee (คลาสแม่):

มี __init__(self, name): เก็บชื่อพนักงาน
มี method perform_duty(self): ให้ return f"{self.name} is performing general duties."
Class Manager (คลาสลูก):

สืบทอดจาก Employee
มี __init__(self, name, department): รับชื่อและแผนก
ใช้ super().__init__(name) เพื่อส่งชื่อไปให้คลาสแม่
เก็บ self.department = department
Override method perform_duty(self): ให้ return f"{self.name} is managing the {self.department} department."
Class Developer (คลาสลูก):

สืบทอดจาก Employee
มี __init__(self, name, language): รับชื่อและภาษาที่เชี่ยวชาญ
ใช้ super().__init__(name) เพื่อส่งชื่อไปให้คลาสแม่
เก็บ self.language = language
Override method perform_duty(self): ให้ return f"{self.name} is coding in {self.language}."
การทดสอบ Polymorphism (รวมทุก object ใน list):

สร้าง object manager = Manager("Alice", "HR")
สร้าง object developer = Developer("Bob", "Python")
สร้าง employees = [manager, developer]
ใช้ for loop วนลูปผ่าน employees และเรียก perform_duty() ของแต่ละคน
'''

class Employee():               #สร้างคลาส แม่()
    def __init__(self, name):   # สร้าง init เก็บค่า name ไว้ใน self
        self.name = name        # กำหนด self.name ให้เก็บค่า name
    def perform_duty(self):     # สร้าง perform_duty('self')
        return f"{self.name} is performing general duties."   #แล้ว คืนค่าให้ print ชื่อ + str
    
class Manager(Employee):                   #สร้างคลาสลูก(คลาสแม่)
    def __init__(self, name, department):  # สร้าง init เก็บค่า name และ department ไว้ใน selfของคลาสลูกManager
        super().__init__(name)             # กำหนด ให้ name ไปเก็บอยู่ใน คลาสแม่[super().__init__()]
        self.department = department       # สร้าง และ กำหนด self.department ให้เก็บค่า department ไว้ในคลาสลูกเอง
    def perform_duty(self):                # สร้าง perform_duty(self) ของตัวเอง เพื่อ override คำสั่งคลาสแม่
        return f"{self.name} is managing the {self.department} department."  # คืนค่า override ให้ print ชื่อ +str + department 

class Developer(Employee):                  # ทำแบบ ข้อด้านบนเลย แค่สร้าง คลาสลูกเพิ่มขึ้นมาอีก 1 อัน เฉยๆ
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
    def perform_duty(self):
        return f"{self.name} is coding in {self.language}."
    
manager = Manager("Alice", "HR")                # กำหนด manager คือ คลาส Manager("__", "__")  โดยเพิ่ม ชื่อ และ ตำแหน่ง
developer = Developer("Bob", "Python")          # กำหนด developer คือ คลาส Developer('__'). '__') โดยเพิ่ม ชื่อ และ ภาษา
employees = [manager, developer]                # กำหนด employees โดย ให้ manager และ developer อยู่ใน list

for e in employees: print(e.perform_duty())     # ในการทำงาน จะใช้ loop เข้ามากำหนดทุกตัวให้ ใช้งาน perform_duty ของแต่ละคลาสที่มีการ override ของตัวเอง