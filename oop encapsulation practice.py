#ข้อที่ 1: SecureBox
#จงสร้าง class SecureBox
#มีตัวแปร __item (เริ่มเป็น None)
#method:
#.store(item) → เก็บของใส่กล่อง
#.retrieve() → ดึงของออกมา (และล้างของในกล่อง)
#ถ้ากล่องว่าง ให้ return "Box is empty"

class SecureBox():
    def __init__(self):
        self.__item = None
        
    def store_item(self, items):
        self.__item = items
        
    def store_retrieve(self, items):
        if self.__item is None:
            return "Box is empty"
        else:
            items = self.__item
            self.__item = None  # ล้างของในกล่อง
            return f"Here is your: {items}"
sb = SecureBox()
sb.store_item("paper")

print(sb.store_retrieve("paper"))
print(sb.store_retrieve("pencil"))


#🔸 ข้อที่ 2: QuizScore
#สร้าง class QuizScore ที่ใช้เก็บคะแนนของแต่ละข้อ
#มีตัวแปร __scores เป็น list
#method:\n
#.add(score) → เพิ่มคะแนนแต่ละข้อ
#.average() → คืนค่าคะแนนเฉลี่ย
#ถ้าไม่มีคะแนนเลย ให้ return "No score yet"

class QuizScore():
    def __init__(self):
        self.__scores = []
    
    def add_score(self, score):
        self.__scores.append(score)
    
    def average_score(self):
        if not self.__scores:
            return f"No Score yet"
        else:
            avg = sum(self.__scores) / len(self.__scores)
            return f" you average score is {avg}"
        
qs = QuizScore()
qs.add_score(100)
qs.add_score(90)
qs.add_score(50)

print(qs.average_score())



#🔸 ข้อที่ 3: UserLogin
#จงสร้าง class UserLogin
#มีตัวแปร __username, __password
#method:
#.set_credentials(username, password)
#.login(username, password) → ตรวจสอบความถูกต้อง
#ถ้าตรง → return "Login successful"
#ถ้าผิด → return "Invalid credentials"


class UserLogin():
    def __init__(self):
        self.__username = ''
        self.__password = ''
    
    def set_credentials(self,username, password):
        self.__username = username
        self.__password = password
        
    def login(self, username, password):
        if username == self.__username and password == self.__password:
            return "Login successful"   
        else:
            return "Invalid credentials"
ul = UserLogin()
ul.set_credentials('ed',1234)

print(ul.login('ed',1234))
print(ul.login('admin',1234))





# Class: WaterBottle
#จำลองขวดน้ำที่ใส่น้ำและเปิดดูได้
#📦 คุณสมบัติ:
#มีตัวแปร __water (เริ่มต้นเป็น 0)
#method:
#.fill(amount) → เติมน้ำ (เพิ่มจากที่มีอยู่)
#.check() → ดูว่าน้ำเหลืออยู่กี่ ml

class WaterBottle():
    def __init__(self):
        self.__water = 0
    
    def fill_bottle(self, amount):
        self.__water += amount
        
    def check_bottle(self):
        return self.__water
    
wb = WaterBottle()
wb.fill_bottle(100)
print(wb.check_bottle())

wb.fill_bottle(154)
print(wb.check_bottle())

#Class: SnackBox
#ตัวแปร __snacks เป็น list (เริ่มเป็นกล่องว่าง)
#method:
#.add_snack(snack) → เพิ่มขนมลงกล่อง
#.take_snack() → หยิบขนมชิ้นล่าสุดออก (แบบ LIFO)
#ถ้ากล่องว่าง ให้ return "No snack left!"

class SnackBox():
    def __init__(self):
        self.__snacks = []
        
    def add(self, snack):
        self.__snacks.append(snack)
        return self.__snacks
        
    def take(self, snack):
        if not self.__snacks:
            return "No snack left!"
        else:
            self.__snacks.remove(snack)
            return (f"here is your: {snack}")
        
        
    def remain(self):
        return self.__snacks
        
sb = SnackBox()
sb.add("Lay")
sb.add("Coke")


print(sb.remain())
print(sb.take("Lay"))
print(sb.remain())