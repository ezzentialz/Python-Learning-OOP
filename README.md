สรุปบทเรียน Python OOP: การเขียนโปรแกรมเชิงวัตถุ
Object-Oriented Programming (OOP) หรือการเขียนโปรแกรมเชิงวัตถุ เป็นกระบวนทัศน์ (Paradigm) การเขียนโปรแกรมที่เน้นการจัดระเบียบโค้ดให้เป็น "วัตถุ (Objects)" ซึ่งมีทั้งข้อมูล (Attributes) และพฤติกรรม (Methods) ของตัวเอง ทำให้โค้ดเป็นระเบียบ, เข้าใจง่าย, นำกลับมาใช้ซ้ำได้ และแก้ไขปรับปรุงได้ง่ายขึ้น

หัวใจของ OOP ประกอบด้วย "4 เสาหลัก" ที่เราได้เรียนรู้กันไปแล้ว:

1. Encapsulation (การห่อหุ้ม)
แนวคิด: การรวมข้อมูล (Attributes) และฟังก์ชัน (Methods) ที่ทำงานกับข้อมูลนั้นๆ เข้าไว้ด้วยกันในหน่วยเดียวที่เรียกว่า Class (คลาส) หรือ Object (วัตถุ) และซ่อนรายละเอียดภายในที่ไม่จำเป็นต้องรู้จากภายนอก

ประโยชน์:

ควบคุมการเข้าถึงข้อมูล: ป้องกันการแก้ไขข้อมูลโดยไม่ตั้งใจจากภายนอก

ความเป็นระเบียบ: โค้ดที่เกี่ยวข้องอยู่ด้วยกัน

บำรุงรักษาง่าย: หากมีการเปลี่ยนแปลงโครงสร้างข้อมูลภายใน Object ก็จะไม่กระทบกับส่วนอื่นของโปรแกรมที่เรียกใช้วัตถุนั้น

ใน Python:

เราใช้ Class ในการห่อหุ้ม

_single_underscore: โดยทั่วไปใช้เป็น protected convention (บ่งบอกว่าไม่ควรเข้าถึงโดยตรงจากภายนอก แต่ก็ยังทำได้)

__double_underscore (หรือ Name Mangling): ทำให้ Attributes/Methods นั้นเข้าถึงได้ยากขึ้นจากภายนอก (กลายเป็น _ClassName__attributeName) แต่ก็ยังไม่ใช่ private ที่แท้จริงเหมือนในภาษาอื่น ๆ

Python

class Car:
    def __init__(self, make, model, year):
        self.make = make         # Public attribute
        self.model = model       # Public attribute
        self.__year = year       # Private-like attribute (Name Mangling)
        self._speed = 0          # Protected-like attribute (Convention)

    def get_info(self):
        return f"{self.make} {self.model} ({self.__year})"

    def _accelerate(self, amount): # Protected-like method
        self._speed += amount
        print(f"Speed increased to {self._speed} km/h")

    def __decelerate(self, amount): # Private-like method
        self._speed -= amount
        print(f"Speed decreased to {self._speed} km/h")

# การใช้งาน
my_car = Car("Toyota", "Camry", 2023)
print(my_car.get_info())
# print(my_car.__year) # จะเกิด AttributeError (ต้องเรียก my_car._Car__year)
# my_car._accelerate(50)
2. Inheritance (การสืบทอดคุณสมบัติ)
แนวคิด: การสร้าง Class ใหม่ (Subclass/Child Class) โดยสืบทอดคุณสมบัติ (Attributes) และพฤติกรรม (Methods) มาจาก Class ที่มีอยู่แล้ว (Superclass/Parent Class)

ประโยชน์:

นำโค้ดกลับมาใช้ซ้ำ (Code Reusability): ไม่ต้องเขียนโค้ดซ้ำ ๆ สำหรับคุณสมบัติที่เหมือนกัน

ขยายความสามารถ: เพิ่มคุณสมบัติหรือแก้ไขพฤติกรรมบางอย่างให้เฉพาะเจาะจงกับ Subclass นั้น ๆ

จัดระเบียบโค้ด: สร้างลำดับชั้นของ Class ที่ชัดเจน

ใน Python:

Subclass จะระบุ Parent Class ในวงเล็บ: class ChildClass(ParentClass):

ใช้ super().__init__() เพื่อเรียกใช้ Constructor ของ Parent Class (จำเป็นต้องทำเพื่อให้ Attributes ของ Parent ถูก Initialize)

สามารถ Override (เขียนทับ) Method ของ Parent ได้

Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method") # บอกว่าต้องไป implement ใน Subclass

class Dog(Animal): # Dog สืบทอดจาก Animal
    def __init__(self, name, breed):
        super().__init__(name) # เรียกใช้ __init__ ของ Animal
        self.breed = breed

    def speak(self): # Override method speak
        return f"{self.name} says Woof!"

class Cat(Animal): # Cat สืบทอดจาก Animal
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self): # Override method speak
        return f"{self.name} says Meow!"

# การใช้งาน
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Tabby")
print(my_dog.speak())
print(my_cat.speak())
3. Polymorphism (การพ้องรูป / หลายรูปแบบ)
แนวคิด: ความสามารถของ Object ต่าง ๆ ที่จะตอบสนองต่อ Method เดียวกันในรูปแบบที่แตกต่างกัน ขึ้นอยู่กับชนิดของ Object นั้น ๆ

ใน Python:

Python สนับสนุน Polymorphism โดยธรรมชาติผ่าน "Duck Typing" (ถ้ามันเดินเหมือนเป็ด ร้องเหมือนเป็ด มันก็คือเป็ด)

หาก Objects หลาย Class มี Method ชื่อเดียวกัน (แม้จะมาจากคนละ Parent Class ก็ตาม) เราสามารถเรียก Method นั้น ๆ ได้โดยไม่ต้องสนว่า Object นั้นมาจาก Class ไหน

Method Overriding: เป็นรูปแบบหนึ่งของ Polymorphism ที่ Subclass ให้การทำงานที่แตกต่างออกไปสำหรับ Method ที่มีอยู่แล้วใน Parent Class (ดังที่เห็นในตัวอย่าง Inheritance ของ speak() Method)

Python

def make_animal_speak(animal_object):
    """ฟังก์ชันที่รับ Object ของสัตว์และเรียก Method speak ของมัน"""
    print(animal_object.speak())

# การใช้งาน Polymorphism
animal1 = Dog("Rex", "German Shepherd")
animal2 = Cat("Fluffy", "White")
# animal3 = Animal("Generic Animal") # จะเกิด NotImplementedError ถ้าเรียก speak()

make_animal_speak(animal1) # Rex says Woof!
make_animal_speak(animal2) # Fluffy says Meow!

# นี่คือ Polymorphism เพราะฟังก์ชัน make_animal_speak() ไม่ต้องรู้ว่าเป็น Dog หรือ Cat
# แค่รู้ว่ามี Method ชื่อ speak() ก็พอ
4. Abstraction (ความเป็นนามธรรม)
แนวคิด: การแสดงเฉพาะข้อมูลที่จำเป็นและซ่อนรายละเอียดที่ซับซ้อนหรือไม่เกี่ยวข้อง เพื่อให้ผู้ใช้ (หรือ Programmer คนอื่น) ใช้งานได้ง่ายขึ้น โดยไม่ต้องรู้ว่าโค้ดทำงานเบื้องหลังอย่างไร

ใน Python:

Python ไม่มี abstract class หรือ interface โดยตรงเหมือนบางภาษา แต่สามารถสร้างแนวคิดนี้ได้โดยใช้ Module abc (Abstract Base Classes)

เรามักจะเห็น Abstraction ผ่านการใช้ Library หรือ Framework ต่าง ๆ ที่เราเรียกใช้ฟังก์ชัน โดยไม่ต้องรู้การทำงานภายใน (เช่น print(), len())

การออกแบบ Class ให้มี Method ที่จำเป็น แต่ปล่อยให้ Subclass ไป Implement เอง (คล้าย raise NotImplementedError ในตัวอย่าง Animal ข้างบน) ก็เป็นส่วนหนึ่งของ Abstraction

Python

from abc import ABC, abstractmethod

class Shape(ABC): # กำหนดให้ Shape เป็น Abstract Base Class
    @abstractmethod
    def area(self): # Abstract method: ต้องถูก implement ใน Subclass
        pass

    @abstractmethod
    def perimeter(self): # Abstract method: ต้องถูก implement ใน Subclass
        pass

    def description(self): # Regular method
        return "This is a geometric shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# การใช้งาน
# shape_obj = Shape() # จะเกิด TypeError: Can't instantiate abstract class Shape
my_circle = Circle(5)
print(f"Area of Circle: {my_circle.area()}")
print(f"Perimeter of Circle: {my_circle.perimeter()}")
print(my_circle.description())
