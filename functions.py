import os #to create custom folders
import time #to delay responses
import json #to save user data
import datetime


user_template = {} #make an empty dictionary
user_template["data"] = [] #create an empty list as the first key / value


#################################################################################################
def create_list():
    try:
        path = os.getcwd()
        path2 = path + "/user_info.json"
        isthere = os.path.exists(path2)
        if isthere:     #checks if the file is already there
            time.sleep(1)
            print("\tStorage file already created....")
        else:
            user_template['default_user'] = {
                "user_id": 0,  
                "username" : 'trial',
                "pin":0000,
                'balance':{
                    "KES":140, 
                    "USD":0
                }
            }

            with open(path2, "w") as fresh:
                json.dump(user_template, fresh, indent=4)
                # users.write('\n')
                print("\tNew storage file and default user created....")
    except: 
        print("\tThere was a problem writing to the save file.")



#################################################################################################
def add_user(a,b):    
    try:
        # read content from the json file then call the write to function.
        # path = os.getcwd()
        # path = path + "/user_info.json"

        def write_to_file(info,a,id):
            with open("user_info.json", "w") as andika:
                json.dump(info, andika, indent=4)
            time.sleep(1)
            print("...................................")
            print(f"\tUser {a} created. Account ID -> {id}.")
            
        with open("user_info.json", "r") as chukua:
                old_content = json.load(chukua)
                id = a[0:3] + b[2:4]
                x = {
                    "user_id": a[0:3] + b[2:4],  
                    "username" : a,
                    "pin":b,
                    'balance': {
                        "KES":0, 
                        "USD":0
                    }
                }
                old_content["data"].append(x) # adding the data to the json file.

        write_to_file(old_content,a,id) #calls the write function and passes the new data
        
    except: 
        print("\tThere was a problem writing to the save file.")




########################################################################################################
def read_data():
        path = os.getcwd()
        path = path + "/user_info.json"

        with open(path, "r") as zetu:
            zata = json.load(zetu)
            print("""
        ******************* ALL ACCOUNTS ********************
            """)

            # print(zata)
            count = 0
            for p in zata["data"]:
                if p['user_id'] == "tri00" or p['user_id'] == "admin": #displays all profiles apart from trial user
                    continue
                print('\tAcct Id: ' + p['user_id'])
                print('\tName: ' + p['username'].upper())
                print('\tPin: ' + "####")
                print('\tBal: ' + "KSH " + str(p["balance"]['KES']) +" || $"+ str(p["balance"]['USD']))
                print('')
                count += 1
            print(f'-> {count} Accounts retrieved')




################################################################################
def view_acct(acct_id,balance = 0):
        print(f"""
        ****** {acct_id.upper()}'s DETAILS ******
            """)

        #read from json file
        path = os.getcwd()
        path = path + "/user_info.json"

        with open(path, "r") as yetu:
            yata = json.load(yetu)

        if balance == 0: # here we are not checking user balance, just admin picking info
            for k in yata["data"]:
                if k['user_id'] == acct_id:

                    print('\tAcct Id: ' + k['user_id'])
                    print('\tName: ' + k['username'])
                    print('\tPin: ' + "####")
                    print('\tBal: ' + "KSH " + str(k["balance"]['KES']) +" || $ "+ str(k["balance"]['USD']))
                    print('')
        elif balance == 1: # here we are picking balance from users side
            for k in yata["data"]:
                if k['user_id'] == acct_id:

                    print('\tAcct Id: ' + k['user_id'])
                    print('\tBal: ' + "KSH " + str(k["balance"]['KES']) +" || $ "+ str(k["balance"]['USD']))
                    print('')
            

"""
****************************************************************************************************
ADMIN PANEL. WE HAVE TWO INTERFACES, ONE FOR USERS AND THE OTHER FOR THE BANKERS
****************************************************************************************************
"""
def call_admin():
    Menu = 10
    while Menu != 0:  
        print("""
        [------------------------------------------]
           Hello ADMIN, Welcome to your menu:
        [------------------------------------------]

            1 -> Create storage file & default user
            2 -> create new user accounts
            3 -> Read all user data
            4 -> View specific accounts
            0 -> Go back to ATM Dashboard
        [__________________________________________]

        """)
        Menu = int(input("Input-> "))
        if Menu == 1: #create save file and default user
            create_list()

        elif Menu == 2: # Create new user accounts 
            user_x = input("\tEnter Username: ")
            user_y = input("\tEnter Pin: ")
            add_user(user_x,user_y)

        elif Menu == 3: # Read all user accounts apart from the trial user
            read_data()

        elif Menu == 4: # search/Read a users accounts, for testing try "acct_id = trial"
            search = input("\tEnter the account id to search for: ") 
            view_acct(search)
            
    else:
            clear = lambda: os.system('cls')
            # clear = lambda: os.system('clear')  # linux system
            clear()
            import atm_break


#####################################################################################################
#####################################################################################################
#####################################################################################################


"""
****************************************************************************************************
DAHSBOARD OPERATIONS, log ins, deposits, withdrawals.....
****************************************************************************************************
"""

def log_user():
    #keeps on asking for user input until you find the correct account
    logged = False
    tries = 0
    def user_login(a_id,pin):
        with open("user_info.json", "r") as f:
            all_users = json.load(f)

            for k in all_users["data"]:
                if k['user_id'] == a_id and k['pin'] == pin:
                    print("\tChecking Credentials from  Mainframe\n".upper())
                    time.sleep(2)
                    print("\tloading.................\n")
                    time.sleep(1)
                    print("\tloading.................\n")
                    time.sleep(1)
                    print("\tAccess granted. Opening Dashboard\n\n")
                    time.sleep(2)
                    clear = lambda: os.system('cls')
                    clear()
                    import atm_break 
                    atm_break.logged_in(a_id)

                    logged = True

    while logged == False and tries < 6:
        if tries == 0:
            a_id = input("\tEnter Account ID: ")
            pin = input("\tEnter Passkey: ")
            clear = lambda: os.system('cls')
            clear()
            user_login(a_id,pin)
            tries += 1
        elif tries < 5:
            print(f"\tyou have {tries} incorrect tries")
            print("\t****************************")
            a_id = input("\tEnter Account ID: ")
            pin = input("\tEnter Passkey: ")
            clear = lambda: os.system('cls')
            clear()
            user_login(a_id,pin)
            tries += 1
        else:
            print(f"\t\aToo many incorrect tries")
            time.sleep(1)
            import atm_break
            atm_break.start()




#################################################################################################
def update_query(a_id,operation = "",amount = 0):   
    
    # try:
        

        def write_to_file(info,acct_id,bal,trans):
            with open("user_info.json", "w") as andika:
                json.dump(info, andika, indent=4)
            time.sleep(1)
            x = datetime.datetime.now() 

            if bal < trans:
                stmnt = "Withdrawal"
            elif bal > trans:
                stmnt = "Deposit"
            print("\n\t*********************************")
            print(f"""
            'RECIEPT':

        {x.strftime('%d')}-{x.strftime('%a')}-{x.strftime('%b')}-{x.year}
        Account {acct_id} Updated. 
        {stmnt} transaction of { bal - trans} was done. 
        New balance -> Kshs {bal} || $ {round(bal/107.75,2)}.
            """)
            print("\t*********************************")
            print("\t*********************************\n")
            
        with open("user_info.json", "r") as chukua:
                old_content = json.load(chukua)

                if operation == "D": # deposit operation
                    for k in old_content["data"]:
                        if k['user_id'] == a_id:
                            pick1 = k['user_id']
                            pick2 = k['username']
                            pick3 = str(k['pin'])
                            pick4 = k["balance"]['KES']
                            pick5 = k["balance"]['USD']

                    balance_kes = pick4 + amount
                    x = {
                        "user_id": pick1,  
                        "username" : pick2,
                        "pin":pick3,
                        'balance': {
                            "KES":round(balance_kes,2), 
                            "USD":round(balance_kes/107.75,2)
                        }
                    }
                elif operation == "W":
                    for k in old_content["data"]:
                        if k['user_id'] == a_id:
                            pick1 = k['user_id']
                            pick2 = k['username']
                            pick3 = str(k['pin'])
                            pick4 = k["balance"]['KES']
                            pick5 = k["balance"]['USD']

                    balance_kes = pick4 - amount
                    x = {
                        "user_id": pick1,  
                        "username" : pick2,
                        "pin":pick3,
                        'balance': {
                            "KES":round(balance_kes,2), 
                            "USD":round(balance_kes/107.75,2)
                        }
                    }

                #update in the old ways. delete then write
               
                del_data = {
                        "user_id": pick1,  
                        "username" : pick2,
                        "pin":pick3,
                        'balance': {
                            "KES":pick4, 
                            "USD":pick5
                        }
                }
                old_content["data"].remove(del_data) #removing the old data
                old_content["data"].append(x) # adding the data to the json file.

        write_to_file(old_content,a_id,balance_kes,pick4) #calls the write function and passes new balance
    
    # except: 
    #     print("\tThere was a problem writing to the save file.")
    