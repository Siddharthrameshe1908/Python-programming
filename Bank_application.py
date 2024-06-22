# class Bank:
#     Bank_name = 'Indian Bank'
#     def __init__(self, name,email_id, Branch, IFSC_code, phone_no,Total_bal, pin_num):
#         self.name = name
#         self.email_id = email_id
#         self.Branch = Branch
#         self.IFSC_code = IFSC_code
#         self.phone_no = phone_no
#         self.Total_bal = Total_bal
#         self.pin_num = pin_num
#     def check_customer(self):
#         customer_name = input("Enter your name :")
#         if customer_name == self.name:
#             print("Welcome to Indian Bank")
#         else:
#             print("Invalid user")
#     def Input_pin(self):
#         return int(input("Enter the PIN"))
#         if input_pin != self.pin_num:
#             print("Invaild user")
#     def Customer_details(self):
#         print(f"Customer Name :{self.name}")
#         print(f"Email id : {self.email_id}")
#         print(f"Branch : {self.Branch}")
#         print(f"IFSC code : {self.IFSC_code}")
#         print(f"Phone no : {self.phone_no}")
#         print(f"Total balance : {self.Total_bal}")
#     def Withdrawal(self):
#         if self.Input_pin() == self.pin_num:
#             amt = int(input("Enter the amount to be withdraw :"))
#             if amt <= self.Total_bal:
#                 self.Total_bal = self.Total_bal - amt
#                 print("Transcation successfull")
#             else:
#                 print(f"Insufficient Balance")
#     def deposit(self):
#         if self.Input_pin() == self.pin_num:
#             amt = int(input("Enter the amount to be deposited :"))
#             if amt <= 100000:
#                 self.Total_bal = self.Total_bal + amt
#                 print("Transcation successful")
#             else:
#                 print("Amount Exceeded")
#         else:
#             print("Invalid PIN")
#     def Current_balance(self):
#         if self.Input_pin() == self.pin_num:
#             print(f"Current Balance :{self.Total_bal}")
#         else:
#             print("Invalid PIN")
# customer1 = Bank('sid','sid@123.gmail.com','Pondy',12345566,6385835749,30000,1234)
# customer2 = Bank('neela','neela@123.gmail.com', 'Andhra', 987654321, 123455660321,50000,4321)
# customer3 = Bank('priya','prita@123.gmail.com','Pondy',2468248,1357913578,100000,2468)
# # Bank.Customer_details(cus1)
# customer1.check_customer()
# customer1.Customer_details()
# customer1.Withdrawal()
# customer1.deposit()
# customer1.Current_balance()