username = input("Enter username : ")
passowrd = input("Enter password : ")

class Atm():
    def __init__(self, bank_balance, card_number, card_owner, last_withdrawl_amount, bank_name):
        self.bankbalance = bank_balance,
        self.cardnumber = card_number,
        self.cardowner = card_owner,
        self.lastWithamt = last_withdrawl_amount,
        self.bankname = bank_name
        

Dakshiin = Atm("20000", "1234567890", "Dakshiin", "1000", "SBI")

if(username=="Dakshiin" and passowrd=="123"):
    show_details = input("What do you want to know? (bankbalance, cardnumber, cardowner, lastWithamt, bankname) : ").lower()
    print(show_details)
    if(show_details=="bankbalance"):
        print(Dakshiin.bankbalance)
    elif(show_details=="cardnumber"):
        print(Dakshiin.cardnumber)
    elif(show_details=="cardowner"):
        print(Dakshiin.cardowner)
    elif(show_details=="lastWithamt"):
        print(Dakshiin.lastWithamt)
    elif(show_details=="bankname"):
        print(Dakshiin.bankname)
    else:
        print("Does not exist in current Atm")

else:
    print("Username or Password is incorrect...")

