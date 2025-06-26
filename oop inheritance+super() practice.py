#โจทย์ฝึก: Override + super()
#🎭 โจทย์: class Robot → class ChatBot
#🔸 class Robot (แม่)
#มี method speak() → return "I am a robot."

#🔸 class ChatBot (ลูก)
#สืบทอดจาก Robot

#Override method speak() แล้วใช้ super().speak()
#ให้ผลลัพธ์รวมเป็น "I am a robot. Let's chat!"

class Robot():
    def speak(self):
        return "I am a robot."
class ChatBot(Robot):
    def speak(self):
        return super().speak() + " Let's chat!"    
    
cb = ChatBot()
print(cb.speak())