import random
import pickle

class Customer():

    def __init__(self,accNo, name, phNo, branch, bal, pin):
        self.accNo = accNo
        self.name = name
        self.phNo = phNo
        self.branch = branch
        self.bal = bal
        self.pin = pin

def pin(pin, obj):
    if pin == obj.pin:
        return True
    else:
        return False

def createAcc():
    name = input('Enter Your Name: ')
    phNo = input('Enter Your Phone No.: ')
    branch = input('Enter Your Branch: ')
    bal = int(input('Enter Intial Balance: '))
    pin = int(input('Set Pin: '))
    accNo = random.randint(10000,99999)
    c = Customer(accNo, name, phNo, branch, bal,pin)
    try:
        with open('customerData.pkl', 'ab') as fp:
            pickle.dump(c,fp)
    except:
        print()
        print('Error: 404 File Not Found')
        print()
    else:
        print()
        print(f'Your account is successfully generated with Account No. {accNo}')
        print("Please Remember the Account No. as we don't have any provision to recover it  :)")
        print()

def checkBal():
    acc = int(input('Enter Account Number: '))
    p = int(input('Enter PIN: '))
    found = False

    try:
        with open('customerData.pkl', 'rb') as fp:
            while True:
                try:
                    c = pickle.load(fp)
                    if c.accNo == acc:
                        found = True
                        if pin(p,c):
                            print()
                            print(f'Account Number: {c.accNo}')
                            print(f'Name: {c.name}')
                            print(f'Phone Number: {c.phNo}')
                            print(f'Branch: {c.branch}')
                            print(f'Balance: {c.bal}')
                            print()
                            break
                        else:
                            print()
                            print('Wrong Pin!!')
                            print()
                            break
                except EOFError:
                    break
        if not found:
            print()
            print('Account Not Found :(')
            print()
    except:
        print()
        print('Error: 404 File Not Found')
        print()

def withdraw():
    acc = int(input('Enter Account Number: '))
    p = int(input('Enter PIN: '))
    data = []
    try:
        with open('customerData.pkl', 'rb') as fp:
            found  = False
            while True:
                try:
                    data.append(pickle.load(fp))
                except EOFError:
                    break
            for c in data:
                if c.accNo == acc:
                    found  = True
                    if pin(p,c):
                        amt = int(input('Enter Amount to Withdraw: '))
                        if c.bal >= amt:
                            c.bal -= amt
                            print()
                            print(f'Withdraw Successfull !! Your current Balance is {c.bal}')
                            print()
                        else:
                            print()
                            print('Insufficient Balance')
                            print()
                        break
                    else:
                        print()
                        print('Wrong Pin!!')
                        print()    
                        break
        if found:
            with open('customerData.pkl', 'wb') as fp:
                for c in data:
                    pickle.dump(c, fp)
        else:
            print()
            print('Account Not Found :(')
            print()
    except:
        print()
        print('Error: 404 File Not Found')
        print()

def deposit():
    acc = int(input('Enter Account Number: '))
    p = int(input('Enter PIN: '))
    data = []
    try:
        with open('customerData.pkl', 'rb') as fp:
            found  = False
            while True:
                try:
                    data.append(pickle.load(fp))
                except EOFError:
                    break
            for c in data:
                if c.accNo == acc:
                    found  = True
                    if pin(p,c):
                        amt = int(input('Enter Amount to Deposit: '))
                        c.bal += amt
                        print()
                        print(f'Deposit Successfull !! Your current Balance is {c.bal}')
                        print()
                        break
                    else:
                        print()
                        print('Wrong Pin!!')
                        print()            
                        break
        if found:
            with open('customerData.pkl', 'wb') as fp:
                for c in data:
                    pickle.dump(c, fp)
        else:
            print()
            print('Account Not Found :(')
            print()
    except:
        print()
        print('Error: 404 File Not Found')
        print()

def transfer():
    sender = int(input("Enter Your Account Number: "))
    p = int(input('Enter PIN: '))
    data = []
    s_found = False
    t_found = False
    try:
        with open('customerData.pkl', 'rb') as fp:
            while True:
                try:
                    data.append(pickle.load(fp))
                except EOFError:
                    break
            for s in data:
                if s.accNo == sender:
                    s_found = True
                    if pin(p,s):
                        target = int(input("Enter Recipient's Account Number: "))
                        for t in data:
                            if t.accNo == target:
                                t_found = True
                                amt = int(input('Enter Amount to Tranfer: '))
                                if s.bal >= amt:
                                    s.bal -= amt
                                    t.bal += amt
                                    print()
                                    print(f'Transfer Successfull !! Your Current Balance is {s.bal}')
                                    print()
                                else:
                                    print()
                                    print('Insufficient Balance')
                                    print()
                    else:
                        wrongPin = True  
                        break
        if s_found and t_found:
            with open('customerData.pkl', 'wb') as fp:
                for c in data:
                    pickle.dump(c, fp)
        elif wrongPin:
            print()
            print('Wrong Pin!!')
            print()
        else:
            print()
            print(f'Either Account Not Found :( Please Check Again...')
            print()
    except:
        print()
        print('Error: 404 File Not Found')
        print()

def menu():
    print('======= Welcome to Bank =======')
    print('1. Create Account')
    print('2. Check Balance')
    print('3. Withdraw')
    print('4. Deposit')
    print('5. Transfer')
    print('0. Exit')

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        createAcc()
    elif choice == 2:
        checkBal()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        deposit()
    elif choice == 5:
        transfer()
    elif choice == 0:
        print('Visit Again...')
        break
    else:
        print('Invalid Choice !!')
