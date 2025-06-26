'''
Abstraction (การสรุปนามธรรม) เนี่ย เป็นเสาหลักของ OOP ที่มักจะถูกพูดถึงคู่กับอีก 3 เสาหลักที่เหลือเลยครับ! 
แต่มันเป็นแนวคิดที่ค่อนข้างเป็นนามธรรม (สมชื่อ) และบางครั้งก็ทับซ้อนกับการทำงานของ Encapsulation อยู่บ้างครับ
'''

# การทำงานของ Abstraction
#Abstract Class: คือคลาสที่ไม่สามารถสร้าง object ได้โดยตรง (สร้าง Book() ไม่ได้) แต่มีไว้เพื่อให้คลาสอื่นมาสืบทอด
#Abstract Method: คือเมธอดที่ไม่มีการ implement (ไม่มีเนื้อหา) ในคลาสแม่ แต่ บังคับ ให้คลาสลูกที่สืบทอดไปต้องเขียนเมธอดนี้ขึ้นมาเอง

# ตัวอย่างง่ายๆ - ลดราคา ให้ vip / vvip

from abc import abstractmethod   #มีการimport abc จาก abstractionmethod เข้ามา

class Member :                  #สร้างคลาสแม่ เป็น abstraction method
    @abstractmethod             # เรียกใช้งาน abstractionmethod
    def Discount():             # กำนหดให้ method Discount() เป็น Abstraction
        pass                    # Pass - ไม่มีค่า ที่เก็บไว้ 
    
class vip(Member):              #สร้างคลาสลูกขึ้นมา inhertiance คลาสแม่ 
    def Discount(self):         # ใช้งาน คลาสแม่ที่เป็น abstractmethod แล้ว กำหนด Discountให้เก็บค่าไว้
        return 0.1              # คืนค่าที่เก็บไว้ 0.1 ไว้ใน discount() 
    
class vvip(Member):             #สร้างคลาสลูก แบบ ด้านบน
    def Discount(self):
        return 0.2              
    
v1 = vip()                      #สร้าง ออบเจ็ค v1 คือ vip()
v2 = vvip()                     #สร้าง ออบเจ็ค v2 คือ vvip()

print(v1.Discount())
print(v2.Discount())   