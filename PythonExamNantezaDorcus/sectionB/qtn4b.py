# a platform that will do the following 
# welcome,WITU Sacco
# 1. Deposit Money
# 2. Withdraw Money 
# 3. Checks 1, money is deposited and the minimum deposit should be 1000.
# 4. selects 2, money should be withdrawn and a minimum withdrawal is 500.
# 5. selects 3, the account  balance should be displayed
# run program until the student decides to quit.

def  wituSacco():
    
    accountBalance = 0
    run = 1
    while run ==1:
        
        print("\n Welcome to Witu Sacco.") 
        
        
        print('1. Deposit Money')
        print('2.Withdraw Money')
        print('3. Check Balance')
        
        studentChoice = int(input("Enter your selection(1,2,or 3): "))
                            
        
                            
        if studentChoice ==1:
            print('\n... processing a deposit transction...')
            depositAmount = int(input("Enter amount to be deposited: "))
            
            if depositAmount <= 1000:
                print('\n...The minimum deposit should be 1000')
            else:
                print(f" Dear student you have deposited: {depositAmount:,} and your accountBalance is:{accountBalance:,}")
           
        elif studentChoice ==2:
            print('\n... processing money Withdrawn ...')
            withdrawAmount = int(input("Enter amount to withdraw: "))
            
            if withdrawAmount < 500:
                print('\n...The minimum withdraw is 500')
            else:
                print(f" Dear student you have withdraw: {withdrawAmount:,} and your accountBalance is:{accountBalance:,}")
            
        else:
            accountBalance = 0
            
            finalAmount = withdrawAmount - accountBalance
            
            print (f"Your accountBalance is: {accountBalance:,} and your accountBalance is {finalAmount:,}")
            
            run = int(input("Press 1 to continue or any number to quit: "))
             
            if run !=1:
                break
wituSacco()