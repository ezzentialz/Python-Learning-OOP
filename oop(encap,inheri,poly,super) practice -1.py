#🧪 โจทย์รวม OOP: ระบบจัดการสัตว์เลี้ยง 🐾
#เราจะสร้างระบบง่าย ๆ สำหรับจัดการสัตว์เลี้ยงในบ้านครับ โดยมีคลาสหลัก ๆ ดังนี้:

#Class Pet (คลาสแม่):

#Encapsulation:
#มี __init__(self, name, age): เก็บชื่อและอายุของสัตว์เลี้ยง (กำหนดให้ __name และ __age เป็น private attribute เพื่อซ่อนข้อมูล)
#มี method get_name(self): คืนค่าชื่อของสัตว์เลี้ยง
#มี method get_age(self): คืนค่าอายุของสัตว์เลี้ยง
#มี method set_age(self, new_age): กำหนดอายุใหม่ (ถ้า new_age มากกว่า 0)

#Polymorphism (Base Method):
#มี method make_sound(self): ให้ return "Some generic pet sound."
#Class Dog (คลาสลูก):

#สืบทอดจาก Pet
#มี __init__(self, name, age, breed): รับชื่อ อายุ และสายพันธุ์
#ใช้ super().__init__(name, age) เพื่อส่งชื่อและอายุไปให้คลาสแม่
#เก็บ self.__breed = breed (เป็น private attribute)
#มี method get_breed(self): คืนค่าสายพันธุ์
#Override Method:
#Override make_sound(self): ให้ return "Woof! Woof!"
#Class Cat (คลาสลูก):

#สืบทอดจาก Pet
#มี __init__(self, name, age, color): รับชื่อ อายุ และสี
#ใช้ super().__init__(name, age) เพื่อส่งชื่อและอายุไปให้คลาสแม่
#เก็บ self.__color = color (เป็น private attribute)
#มี method get_color(self): คืนค่าสี
#Override Method:
#Override make_sound(self): ให้ return "Meow!"
#การทดสอบระบบ (Polymorphism & Interaction):

#สร้าง object dog = Dog("Buddy", 3, "Golden Retriever")
#สร้าง object cat = Cat("Whiskers", 2, "Black")
#สร้าง pet_list = [dog, cat]
#วนลูปผ่าน pet_list แล้ว:
#พิมพ์ชื่อและอายุของแต่ละตัว (ใช้ get_name() และ get_age())
#ให้แต่ละตัวส่งเสียง (เรียก make_sound())
#ลองเปลี่ยนอายุของ dog ด้วย dog.set_age(4) แล้วพิมพ์อายุอีกครั้ง

class Pet():                                # สร้างคลาส แม่ (Parent/Base Class) ชื่อ Pet
    def __init__(self, name, age):          # Constructor: เมื่อสร้าง object Pet ต้องส่ง name, age
        self.__name = name                  # เก็บค่า name ในตัวแปร private: __name (Encapsulation)
        self.__age = age                    # เก็บค่า age ในตัวแปร private: __age (Encapsulation)

    def get_name(self):                     # Getter Method: สำหรับเข้าถึง __name
        # ไม่มี parameter อื่นนอกจาก self เพราะหน้าที่คือ "เอาค่าออกมา"
        return self.__name                  # คืนค่าชื่อที่ถูกเก็บไว้

    def get_age(self):                      # Getter Method: สำหรับเข้าถึง __age
        # ไม่มี parameter อื่นนอกจาก self เพราะหน้าที่คือ "เอาค่าออกมา"
        return self.__age                   # คืนค่าอายุที่ถูกเก็บไว้

    def set_age(self, new_age):             # Setter Method: สำหรับเปลี่ยนค่า __age
        # รับ new_age เป็น parameter เพื่อนำไปกำหนดค่าใหม่
        if new_age > 0:                     # ตรวจสอบเงื่อนไขว่าอายุใหม่ต้องมากกว่า 0
            self.__age = new_age            # ✅ กำหนดค่าใหม่ให้ __age ตรงนี้เลย (ไม่ใช้ return ==)
        # ไม่ต้องมี return เพราะหน้าที่คือเปลี่ยนค่า ไม่ใช่คืนค่าอะไรกลับไป

    def make_sound(self):                   # Method พื้นฐานสำหรับเสียงสัตว์
        return "Some generic pet sound."    # เสียงทั่วไปของสัตว์เลี้ยง

class Dog(Pet):                             # สร้างคลาสลูก Dog สืบทอดจาก Pet (Inheritance)
    def __init__(self, name, age, breed):   # Constructor ของ Dog รับ name, age, breed
        super().__init__(name, age)         # ✅ ใช้ super() เรียก constructor ของคลาสแม่ (Pet)
        # เพื่อให้ Pet จัดการเก็บ name และ age ให้
        self.__breed = breed                # เก็บค่า breed ในตัวแปร private: __breed ของ Dog เอง

    def get_breed(self):                    # Getter Method สำหรับเข้าถึง __breed ของ Dog
        return self.__breed                 # คืนค่าสายพันธุ์

    def make_sound(self):                   # Override Method: เขียน method make_sound ทับของคลาสแม่
        return "Woof! Woof!"                # กำหนดเสียงเฉพาะของ Dog

class Cat(Pet):                             # สร้างคลาสลูก Cat สืบทอดจาก Pet (Inheritance)
    def __init__(self, name, age, color):   # Constructor ของ Cat รับ name, age, color
        super().__init__(name, age)         # ✅ ใช้ super() เรียก constructor ของคลาสแม่ (Pet)
        # เพื่อให้ Pet จัดการเก็บ name และ age ให้
        self.__color = color                # เก็บค่า color ในตัวแปร private: __color ของ Cat เอง

    def get_color(self):                    # Getter Method สำหรับเข้าถึง __color ของ Cat
        return self.__color                 # คืนค่าสี

    def make_sound(self):                   # Override Method: เขียน method make_sound ทับของคลาสแม่
        return "Meow!"                      # กำหนดเสียงเฉพาะของ Cat

# --- การทดสอบระบบ (Polymorphism & Interaction) ---
dog = Dog("Buddy", 3, "Golden Retriever")   # สร้าง object Dog
cat = Cat("Whiskers", 2, "Black")           # สร้าง object Cat
pet_list = [dog, cat]                       # สร้าง list ที่เก็บ object ของ Dog และ Cat (Polymorphism)

print("--- Initial Pet Info ---")
for p in pet_list:                          # วนลูปผ่าน list ของสัตว์เลี้ยง
    # เรียก get_name() และ get_age() เพื่อดึงข้อมูลที่ถูก Encapsulate
    print(f"Pet Name: {p.get_name()}, Age: {p.get_age()}")
    # เรียก make_sound() ซึ่งจะแสดงเสียงตามคลาสที่ Override ไว้ (Polymorphism)
    print(p.make_sound())
    # สามารถเรียก method เฉพาะของคลาสลูกได้ ถ้าต้องการ เช่น
    if isinstance(p, Dog): # ตรวจสอบว่าเป็น object ของ Dog หรือไม่
        print(f"  Breed: {p.get_breed()}")
    elif isinstance(p, Cat): # ตรวจสอบว่าเป็น object ของ Cat หรือไม่
        print(f"  Color: {p.get_color()}")
    print("-" * 20) # พิมพ์เส้นแบ่งเพื่อความสวยงาม

# --- ลองเปลี่ยนอายุของ dog และพิมพ์อีกครั้ง ---
dog.set_age(4) # เรียก setter method เพื่อเปลี่ยนอายุของ dog
print(f"\n--- After changing Buddy's age ---")
print(f"{dog.get_name()}'s new age: {dog.get_age()}") # เรียก getter เพื่อดูอายุใหม่