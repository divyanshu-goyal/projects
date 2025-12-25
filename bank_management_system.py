import mysql.connector as c
con = c.connect(host="localhost", user="root", passwd="admin", database="project")
cursor = con.cursor()

def calculate_interest(account_number, interest_rate): 
        cursor.execute("SELECT balance FROM bank WHERE acc_no={}".format(account_number)) 
        account_data = cursor.fetchone() 
        if account_data: 
            balance = account_data[0] 
            interest = (balance * interest_rate) / 100 
            new_balance = balance + interest 
            cursor.execute("UPDATE bank SET balance={} WHERE acc_no={}".format(new_balance, account_number)) 
            con.commit() 
            print("Interest of {} credited to account {}".format(interest, account_number)) 
        else: 
            print("Account not found")

def generate_account_number():
    cursor.execute('SELECT MAX(acc_no) FROM bank')
    result = cursor.fetchone()[0]
    return result + 1

def merge_accounts(primary_account, account_to_merge): 
        cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(primary_account)) 
        primary_account_data = cursor.fetchone() 
        cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account_to_merge)) 
        account_to_merge_data = cursor.fetchone() 
        if primary_account_data and account_to_merge_data: 
            cursor.execute("SELECT balance FROM bank WHERE acc_no={}".format(account_to_merge)) 
            account_to_merge_balance = cursor.fetchone()[0] 
            cursor.execute("UPDATE bank SET balance=balance+{} WHERE acc_no={}".format(account_to_merge_balance, primary_account)) 
            cursor.execute("DELETE FROM bank WHERE acc_no={}".format(account_to_merge))            
            con.commit() 
            print("Accounts merged successfully.") 
        else: 
            print("One or both accounts not found.") 
 
while True: 
    print("*"*91) 
    print(" "*27,end=" ") 
    print("       BANK MANAGEMENT SYSTEM") 
    print("*"*91) 
 
    choice=int(input('''1: OPEN AN ACCOUNT\n2: CASH WITHDRAWL\n3: CASH DEPOSIT\n4: ACCOUNT STATEMENT \n5: UPDATE ACCOUNT
            \n6: DELETE ACCOUNT\n7: TRANSFER FUNDS\n8: LOAN\n9: TOTAL ACCOUNTS \n10: INTEREST CALCULATION\n11: ACCOUNT MERGING
            \nENTER YOUR CHOICE:''')) 
    
    if choice==1:  
        name=input("ENTER NAME OF ACCOUNT HOLDER: ") 
        balance=int(input("ENTER OPENING BALANCE: ")) 
        mob=input("ENTER MOBILE NUMBER: ")     
        query="insert into bank values({},'{}','{}','{}')".format(generate_account_number(),name,balance ,mob)  
        cursor.execute(query) 
        con.commit() 
        print("-"*91)     
        print("                                   ACCOUNT OPENED SUCCESSFULLY....") 
        print("-"*91) 
 
    if choice == 2:
        account = int(input("ENTER ACCOUNT NUMBER: "))
        query = "select * from bank where acc_no={}".format(account)
        cursor.execute(query)
        data = cursor.fetchone()
        if cursor.rowcount > 0:
            balance = data[2]
            print("BALANCE", balance)
            amnt = int(input("ENTER THE AMOUNT: "))
            print("*" * 91)
            print("                                   AMOUNT WITHDRAWN SUCCESSFULLY")
            print("*" * 91)
            cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account))
            updated_data = cursor.fetchone()
            if updated_data:
                print()
                print("                                   Account details:")
                print("Account Number: ", updated_data[0])
                print("Name: ", updated_data[1])
                print("BALANCE: ", balance - amnt)
                print("Mobile Number: ", updated_data[3])
        else:
            print("                                   ACCOUNT NUMBER NOT FOUND....")
 
    if choice == 3:
        account = int(input("ENTER ACCOUNT NUMBER: "))
        query = "select * from bank where acc_no={}".format(account)
        cursor.execute(query)
        data = cursor.fetchone()
        if cursor.rowcount > 0:
            balance = data[2]
            print("BALANCE", balance)
            amnt = int(input("ENTER THE AMOUNT: "))
            print("                                   AMOUNT DEPOSITED SUCCESSFULLY")
            cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account))
            updated_data = cursor.fetchone()
            if updated_data:
                print()
                print("                                   Account details:")
                print("Account Number: ", updated_data[0])
                print("Name: ", updated_data[1])
                print("BALANCE: ", balance + amnt)
                print("Mobile Number: ", updated_data[3])
        else:
            print("                                   ACCOUNT NUMBER NOT FOUND....")
 
    if choice == 4:
        account = int(input("ENTER ACCOUNT NUMBER: "))
        cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account))
        updated_data = cursor.fetchone()
        if updated_data:
            print("-" * 91)
            print("                                   Account details:")
            print("Account Number: ", updated_data[0])
            print("Name: ", updated_data[1])
            print("BALANCE: ", updated_data[2])
            print("Mobile Number: ", updated_data[3])
            print("-" * 91)
        else:
            print("                                   ACCOUNT NUMBER NOT FOUND")
     
    if choice == 5:
        ch = int(input(
            "1: UPDATE NAME\n"
            "2: UPDATE MOBILE_NUMBER\n\n"
            "3: UPDATE BRANCH\n"
            "ENTER YOUR CHOICE: "
        ))
        if ch == 1:
            account = int(input("ENTER ACCOUNT NUMBER: "))
            Name = input("ENTER UPDATED NAME: ")
            cursor.execute("update bank set name='{}' where acc_no={}".format(Name, account))
            con.commit()
            cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account))
            updated_data = cursor.fetchone()
            if updated_data:
                print("*" * 91)
                print("                                   Updated account details:")
                print("*" * 91)
                print("Account Number: ", updated_data[0])
                print("Name: ", updated_data[1])
                print("BALANCE: ", updated_data[2])
                print("Mobile Number: ", updated_data[3])
            else:
                print("                                   Account not found")
        if ch == 2:
            account = int(input("ENTER ACCOUNT NUMBER: "))
            mobile = input("ENTER UPDATED MOBILE_NUMBER: ")
            cursor.execute("update bank set mobile='{}' where acc_no={}".format(mobile, account))
            con.commit()
            cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account))
            updated_data = cursor.fetchone()
            if updated_data:
                print("*" * 91)
                print("                                   Updated account details:")
                print("*" * 91)
                print("Account Number: ", updated_data[0])
                print("Name: ", updated_data[1])
                print("BALANCE: ", updated_data[2])
                print("Mobile Number: ", updated_data[3])
            else:
                print("                                   Account not found")
        if ch == 3:
            account = int(input("ENTER ACCOUNT NUMBER: "))
            branch = input("ENTER UPDATED BRANCH: ")
            cursor.execute("update bank set branch='{}' where acc_no={}".format(branch, account))
            con.commit()
            cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account))
            updated_data = cursor.fetchone()
            if updated_data:
                print("*" * 91)
                print("                                   Updated account details:")
                print("*" * 91)
                print("Account Number: ", updated_data[0])
                print("Name: ", updated_data[1])
                print("BALANCE: ", updated_data[2])
                print("Mobile Number: ", updated_data[3])
            else:
                print("                                   Account not found")
    if choice==6: 
        account = int(input("ENTER ACCOUNT NUMBER TO DELETE: ")) 
        cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account)) 
        data = cursor.fetchone() 
        if cursor.rowcount > 0: 
            cursor.execute("DELETE FROM bank WHERE acc_no={}".format(account)) 
            con.commit() 
            print("                                   ACCOUNT DELETED SUCCESSFULLY") 
        else: 
            print("                                   ACCOUNT NUMBER NOT FOUND") 
 
    if choice == 7: 
        sender_account = int(input("ENTER SENDER ACCOUNT NUMBER: ")) 
        receiver_account = int(input("ENTER RECEIVER ACCOUNT NUMBER: ")) 
        amount = int(input("ENTER AMOUNT TO TRANSFER: ")) 
        cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(sender_account)) 
        sender_data = cursor.fetchone() 
        cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(receiver_account)) 
        receiver_data = cursor.fetchone() 
        if sender_data and receiver_data: 
            sender_balance = sender_data[2] 
            receiver_balance = receiver_data[2] 
            if sender_balance >= amount: 
                sender_balance -= amount 
                receiver_balance += amount 
                cursor.execute("UPDATE bank SET balance={} WHERE acc_no={}".format(sender_balance, sender_account)) 
                cursor.execute("UPDATE bank SET balance={} WHERE acc_no={}".format(receiver_balance,receiver_account)) 
                con.commit() 
                print("                                   AMOUNT TRANSFERRED SUCCESSFULLY") 
            else: 
                print("                                   INSUFFICIENT FUNDS") 
        else: 
            print("                                   SENDER OR RECEIVER ACCOUNT NOT FOUND") 
    
    if choice == 8: 
        account = int(input("ENTER ACCOUNT NUMBER: ")) 
        query = "select * from bank where acc_no={}".format(account) 
        cursor.execute(query) 
        data = cursor.fetchone() 
        if cursor.rowcount > 0: 
            loan_amount = int(input("ENTER LOAN AMOUNT: ")) 
            balance = data[2] 
            if loan_amount <= (balance * 2):  # Assuming loan limit is twice the balance 
                balance += loan_amount 
                cursor.execute("UPDATE bank SET balance={} WHERE acc_no={}".format(balance, account)) 
                con.commit() 
                print("                                   LOAN GRANTED SUCCESSFULLY") 
                cursor.execute("SELECT * FROM bank WHERE acc_no={}".format(account)) 
                updated_data = cursor.fetchone() 
                if updated_data: 
                    print("*"*91) 
                    print("                                   Updated account details:")               
                    print("Account Number: ", updated_data[0]) 
                    print("Name: ", updated_data[1]) 
                    print("BALANCE: ",updated_data[2]) 
                    print("Mobile Number: ", updated_data[3]) 
            else: 
                print("                                   LOAN AMOUNT EXCEEDS LIMIT") 
        else: 
            print("                                   ACCOUNT NUMBER NOT FOUND") 
    
    if choice==9: 
        cursor.execute("SELECT COUNT(*) FROM bank") 
        total_accounts = cursor.fetchone()[0] 
        print("Total Number of Accounts:", total_accounts) 
    
    if choice == 10:  
        account_number = int(input("Enter account number: ")) 
        interest_rate = 0.05 
        calculate_interest(account_number, interest_rate) 
         
    if choice==11: 
        primary_acc = int(input("Enter primary account number: ")) 
        merge_acc = int(input("Enter account number to merge: ")) 
        merge_accounts(primary_acc, merge_acc)