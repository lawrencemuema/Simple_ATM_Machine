"""
# hello world
lawrence M. Muema
Atm_project
"""
import os
import functions#calling our functions module

# ***********************************************************************
# our commands

def start():
    print("""
    _____________________________________________________
    _________|  |ATM MACHINE {Beta v1.0}|   |____________
    _____________________________________________________
    """)
    Menu = 5
    while Menu != 0:  
        print("""
        [------------------------------------------]
            1 -> LOGIN [access ATM services]
            2 -> ADMIN [additional operations]
            0 -> exit
        [__________________________________________]

        """)
        Menu = int(input("Input-> "))
        if Menu == 1: #check for storage folder
            clear = lambda: os.system('cls')
            clear()
            functions.log_user()

        elif Menu == 2: #create save file and default user
            clear = lambda: os.system('cls')
            clear()
            functions.call_admin()

        else:
            exit()



def logged_in(acct_id):
    Menu1 = 27
    while Menu1 != 0:  
        print(f"""
        [------------------------------------------]
            Hello {acct_id.upper()}, Welcome to your Account:
        [------------------------------------------]
                'd' -> Deposit  (kshs)
                'w' -> Withdraw (kshs)
                'b' -> Balance
                 0 -> Log Out
        [__________________________________________]

        """)
        Menu1 = input("Input-> ").upper()
        if Menu1 == "D": 
            amount = float(input("Enter amount to DEPOSIT : Kshs "))
            functions.update_query(acct_id,"D",amount)

        elif Menu1 == "W": 
            amount = float(input("Enter amount to WITHDRAW: Kshs "))
            functions.update_query(acct_id,"W",amount)

        elif Menu1 == "B":
            functions.view_acct(acct_id,1)
            
        else:
            clear = lambda: os.system('cls')
            clear()
            start()




if __name__ == '__main__':
    start()