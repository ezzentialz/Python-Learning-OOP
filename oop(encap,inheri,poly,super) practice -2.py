#🧪 โจทย์รวม OOP: ระบบจัดการบัญชีธนาคาร 🏦
#เราจะสร้างระบบจัดการบัญชีธนาคารแบบง่าย ๆ ครับ

#Class BankAccount (คลาสแม่):

#Encapsulation:
#มี __init__(self, account_number, initial_balance=0):
#เก็บหมายเลขบัญชีเป็น __account_number (private)
#เก็บยอดเงินคงเหลือเป็น __balance (private) โดยกำหนดค่าเริ่มต้นเป็น 0 หากไม่ได้ระบุ
#มี get_account_number(self): คืนค่าหมายเลขบัญชี
#มี get_balance(self): คืนค่ายอดเงินคงเหลือ
#มี deposit(self, amount):
#เพิ่ม amount เข้าไปใน __balance
#ถ้า amount เป็นบวกเท่านั้น
#คืนค่าข้อความ เช่น "Deposited [amount]. New balance: [new_balance]"
#มี withdraw(self, amount):
#ลด amount ออกจาก __balance
#ถ้า amount เป็นบวกและมีเงินพอในบัญชี
#คืนค่าข้อความ เช่น "Withdrew [amount]. New balance: [new_balance]"
#ถ้าเงินไม่พอ ให้คืนค่า "Insufficient funds."
#Polymorphism (Base Method):
#มี get_account_details(self): คืนค่าข้อความ "Account [account_number], Balance: [balance] baht."
#Class SavingsAccount (คลาสลูก):

#สืบทอดจาก BankAccount
#มี __init__(self, account_number, initial_balance=0, interest_rate=0.01):
#ใช้ super().__init__(account_number, initial_balance) เพื่อส่งข้อมูลพื้นฐานให้คลาสแม่
#เก็บ __interest_rate (private)
#มี get_interest_rate(self): คืนค่าอัตราดอกเบี้ย
#มี add_interest(self):
#คำนวณดอกเบี้ยจาก __balance และ __interest_rate
#เพิ่มดอกเบี้ยเข้าใน __balance
#คืนค่าข้อความ "Interest added. New balance: [new_balance]"
#Override Method:
#Override get_account_details(self): คืนค่าข้อความ "Savings Account [account_number], Balance: [balance] baht, Interest Rate: [interest_rate*100]%."
#Class CheckingAccount (คลาสลูก):

#สืบทอดจาก BankAccount
#มี __init__(self, account_number, initial_balance=0, overdraft_limit=500):
#ใช้ super().__init__(account_number, initial_balance) เพื่อส่งข้อมูลพื้นฐานให้คลาสแม่
#เก็บ __overdraft_limit (private) คือ วงเงินเบิกเกินบัญชี
#มี get_overdraft_limit(self): คืนค่าวงเงินเบิกเกินบัญชี
#Override Method:
#Override withdraw(self, amount):
#อนุญาตให้ถอนเงินเกินได้ถึง __overdraft_limit (เช่น ถ้ามียอด 100 แต่เบิกเกิน 200 ก็จะติดลบ 100 แต่ถ้าวงเงินเบิกเกินบัญชีคือ 500 ก็จะยังถอนได้)
#ถ้าถอนได้ ให้เรียก super().withdraw(amount) เพื่อใช้ logic การถอนของคลาสแม่ (แต่ต้องปรับเงื่อนไขการตรวจสอบก่อน)
#ถ้าถอนไม่ได้ (เกินวงเงินเบิกเกินบัญชีรวม) ให้คืนค่า "Withdrawal denied: Exceeds overdraft limit."
#Override get_account_details(self): คืนค่าข้อความ "Checking Account [account_number], Balance: [balance] baht, Overdraft Limit: [overdraft_limit] baht."
#การทดสอบระบบ (Polymorphism & Interaction):

#สร้าง savings = SavingsAccount("S123", 1000, 0.02) (ดอกเบี้ย 2%)
#สร้าง checking = CheckingAccount("C456", 500, 1000) (เบิกเกินได้ 1000)
#สร้าง bank_accounts = [savings, checking]
#วนลูปผ่าน bank_accounts และพิมพ์ get_account_details() ของแต่ละบัญชี
#ทำการฝากเงินเข้า savings 200 บาท
#ทำการถอนเงินจาก checking 800 บาท (ดูว่าเบิกเกินได้หรือไม่)
#ทำการถอนเงินจาก checking อีก 1000 บาท (ดูว่าจะถอนเกินวงเงินรวมหรือไม่)
#เพิ่มดอกเบี้ยให้ savings ด้วย add_interest() แล้วพิมพ์รายละเอียดอีกครั้ง


class BankAccount():
    def __init__(self,account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance
        
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit: {amount}. New Balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        
        elif amount > self.__balance:
            return "Insufficient funds."
        else:
            self.__balance -= amount
            return f"Withdraw {amount}. New Balance: {self.__balance} baht."
        
    def get_account_details(self):
        return f"Account {self.__account_number}, Balance: {self.__balance} baht."
    
class SavingAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.1):
        super().__init__(account_number, initial_balance)
        self.__interest_rate = interest_rate 
    
    def get_interest_rate(self):
        return self.__interest_rate
    
    def add_interest_rate(self):
        interest_amount = self._BankAccount__balance * self.__interest_rate 
        self._BankAccount__balance += interest_amount
        return (f"Interest added. New balance: {self._BankAccount__balance}")
    
    def get_account_details(self):
        return (f"Savings Account: {self._BankAccount__account_number}, Balance: {self._BankAccount__balance} baht, Interest Rate: {self.__interest_rate*100:.1f}%.")
    
class CheckingAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=500):
        super().__init__(account_number, initial_balance)
        self.__overdraft_limit = overdraft_limit 
        
    def get_overdraft_limit(self):
        return self.__overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        
        if amount > (self._BankAccount__balance + self.__overdraft_limit):
            return "Withdrawal denied: Exceeds overdraft limit." 
        else:
            self._BankAccount__balance -= amount
            return f"Withdrew {amount}. New Balance: {self._BankAccount__balance} baht."
           
    def get_account_details(self):
        return (f"Checking Account {self._BankAccount__account_number}, Balance: {self._BankAccount__balance} baht, Overdraft Limit: {self.__overdraft_limit} baht.")
    
saving = SavingAccount("S123", 1000, 0.02)
checking = CheckingAccount("C456", 500, 1000)
bank_accounts = [saving, checking]

for ba in bank_accounts:
    print(ba.get_account_details())
    
print(f"-"* 50)
    
print(saving.deposit(200))
print(checking.withdraw(800))
print(checking.withdraw(1000))
print(saving.add_interest_rate())

print(f"-"* 50)

for ba in bank_accounts:
    print(ba.get_account_details())