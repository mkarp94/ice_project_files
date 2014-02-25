import random, os

#TAKE USER INPUT AND RUN FUNCTION TO INSERT Credit Card into user account
def add_card():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print """
    ==================================
    ADD A Credit Card to your account:
    ==================================
        """
    CreditCard = None
    while None == CreditCard: 
        print """
        Select the card type:
            1 - American Express
            2 - Visa
            3 - MasterCard
            4 - Discover
            5 - Exit
            """
        CreditCard = raw_input("Enter a choice and press enter:  ")
        if CreditCard == "1":
            CreditCard = "American Express"
        elif CreditCard == "2":
            CreditCard = "Visa"
        elif CreditCard == "3":
            CreditCard = "MasterCard"
        elif CreditCard == "4":
            CreditCard = "Discover"
        elif CreditCard == "5":
            CreditCard = None
            raw_input("Press Enter to return to the menu:  ")
            return 
        else:
            CreditCard = None
            print "ERROR ADDING RECORD!"    

    
    Last4Digits = None  
    while  None == Last4Digits or len(Last4Digits) != 4: 
        Last4Digits = raw_input("Enter the last 4 digits of the card: ")
    
    expiration_date = None
    while None == expiration_date or len(expiration_date) != 5: 
        expiration_date = raw_input("Enter the expiration date (mm/dd): ")
 
    Bank = None
    while None == Bank or CreditCard != "American Express": 
        print """
        Select the financial institution backing the credit:
            1 - Chase
            2 - Bank of America
            3 - Wells Fargo
            4 - HSBC
            5 - CapitalOne
            6 - Exit
            """
        Bank = raw_input("Enter a choice and press enter:  ")
        if Bank == "1":
            Bank = "Chase"
        elif Bank == "2":
            Bank = "Bank of America"
        elif Bank == "3":
            Bank = "Wells Fargo"
        elif Bank == "4":
            Bank = "HSBC"
        elif Bank == "5":
            Bank = "CapitalOne"
        elif Bank == "6":
            Bank = None
            raw_input("Press Enter to return to the menu:  ")
            return 
        else:
            Bank = None
            print "ERROR ADDING RECORD!"
            
    
    annualInterestRate = None
    while annualInterestRate < 0 or annualInterestRate > 1.00:
        annualInterestRate = raw_input("What is the yearly specified interest rate on the balance outstanding(enter data as 17.24% as 0.1724): ")
        annualInterestRate = float(annualInterestRate)
    
    balance = None
    while balance == None: 
        balance = raw_input("What is the balance on the card (enter a positive number if there is debt outstanding on the card): ")
        balance  = float(balance)
        
    credit_limit = None
    while credit_limit == None or credit_limit <= 0:
        credit_limit = raw_input("What is the credit limit on the card ending in " + str(Last4Digits) + ": ")
        credit_limit   = float(credit_limit)
#def __init__(self, credit_card_company, last4digits, expiration_date, bank, annual_interest_rate, credit_limit, min_monthly_payment_rate, balance = 0, rewards = None)