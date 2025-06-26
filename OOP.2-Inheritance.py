# เสาที่ 2: Inheritance (การสืบทอด)
'''
🏛️ นิยามแบบเข้าใจง่าย
Inheritance = "ลูกได้รับสิ่งที่พ่อแม่มี โดยไม่ต้องสร้างใหม่"

หรือในโลกของโค้ด…

class หนึ่ง (ลูก) สามารถ “สืบทอด” method และ attribute จาก class อื่น (แม่) ได้เลย
ประหยัดเวลา ไม่ต้องเขียนซ้ำ!
'''

#class Animal → มี method .breathe(), .eat()
#class Dog(Animal) → ไม่ต้องเขียน breathe ใหม่

#class Parent:
#    def greet(self):
#        return "Hello!"

#class Child(Parent):
#    pass  # ไม่เขียนอะไร ก็ยังใช้ greet() ได้

#c = Child()
#print(c.greet())  # ✅ Hello!


#Class: Vehicle → Car
#คลาสแม่ Vehicle มี method .start() → return "Engine started"
#คลาสลูก Car สืบทอด Vehicle
#สร้าง object mycar แล้วเรียก .start()

class Vehicle:
    def start():
        return f"Engine started"

class Car(Vehicle):
    pass

c = Car
print(c.start())


#Inheritance: Animal → Cat, Dog
#class Animal (แม่)
#มี method .speak()
#ไม่ต้องกำหนดเสียงในแม่ ให้แค่ return "..."

#class Cat (ลูก)
#สืบทอดจาก Animal
#เขียน method .speak() → return "Meow!"

#class Dog (ลูก)
#สืบทอดจาก Animal
#เขียน method .speak() → return "Woof!"

class Animal():
    def speak(self):
        return "..."
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
cat = Cat()
dog = Dog()

print(cat.speak())
print(dog.speak())


#class: Animal
#__init__(self, name) → เก็บชื่อสัตว์ไว้ใน self.name

#class: Dog(Animal)
#ใช้ super().__init__(name) เพื่อสืบทอด name จาก Animal

#เพิ่ม attribute breed ใน __init__ ของตัวเอง

class Animal():
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
d = Dog("Buddy", "Golden Retriever")
print(d.name)
print(d.breed)