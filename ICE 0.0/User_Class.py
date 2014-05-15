# -*- coding: utf-8 -*-
### 
### User_Class.py
### User.name = “string with name of user on cards”
### User.password = “string of password”
###
### User.wallet = {dictionary of user cards}
### User.wallet = {credit_card_1_last_4_digits: Credit_Card_class1, 
###                 credit_card_2_last_4_digits: Credit_Card_class2}
### User.wallet key = credit_card_last_4_digits (string of cards last 4 digits)
### User.wallet value = Credit_Card_class (class object representing a credit card)
###
import datetime, os, pickle
import Credit_Card_Class_w_Rwrds

#import Main_Menu
from Purchase_Class import purchase

#from User_Menu import user_menu

class user(object):
    def __init__(self, name, username, password, reward_structure_preference = "minimize interest paid"):
        """create a person called name"""
        self.name = name
        self.birthday = None #to be filled in later
        self.lastName = name.split(' ')[-1]
        self.firstName = name.split(' ')[0]
        self.username = username
        self.password = password
        self.wallet = {}
        self.reward_structure_preference = reward_structure_preference #("Minimize interest paid, Maximize Points, Minimize % credit used per card)
        self.transaction_id = 0
        self.transactions = {}    
    
    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def getfirstName(self):
        """return self's last name"""
        return self.firstName

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name
    def get_name(self):
        return self.name
    def update_name(self, new_name):
        self.name = new_name
    
    def get_username(self):
        return self.username
    def update_username(self, new_username):
        self.username = new_username
    
    def get_password(self):
        return self.password
    def update_password(self, new_password):
        self.password = new_password
           
    def get_reward_structure_preference(self):
        return self.reward_structure_preference
    def set_reward_structure_preference(self):
        print "default credit optimization set to minimize interest"
        print "Enter 0 to exit and retain default or"
        print "Enter 1 to change optimization preference to maximize points"
        choice = raw_input()
        if choice == "0": return
        else: self.reward_structure_preference = "maximize points"

    def get_wallet(self):
        return self.wallet
    def update_wallet(self, new_wallet):
        self.wallet = new_wallet
    
    def get_total_user_balance(self):
        total_balance = 0
        for key in self.wallet.keys(): 
            total_balance += self.wallet[key].balance
        return total_balance
    def get_total_user_credit_limit(self):
        total_credit = 0
        for key in self.wallet.keys(): 
            total_credit += self.wallet[key].credit_limit
        return total_credit
    
    def get_total_user_points(self):
        pass
    def update_total_user_points(self):
        pass
    def get_theoretical_user_points_post_purchase(self, purchase):
        pass
    def get_total_user_rewards(self):
        pass
    def update_total_user_rewards(self):
        pass
    def get_theoretical_user_rewards_post_purchase(self, purchase):
        pass

    def get_total_user_dollar_credit_used(self): 
        return str(round(self.get_total_user_balance(), 2)) 
    def get_total_user_percent_credit_used(self): 
        return str(round(100.*(1.0*self.get_total_user_balance()/ self.get_total_user_credit_limit()), 2))
    def get_total_user_decimal_credit_used(self):
        return str(round((1.*self.get_total_user_balance() / self.get_total_user_credit_limit()), 3))
    def get_total_user_fractional_credit_used(self): 
        return str(round(self.get_total_user_balance(), 2)) + "/" + str(round(self.get_total_user_credit_limit(), 2))
    
    def get_total_user_dollar_credit_remaining(self): 
        return str(round(self.get_total_user_credit_limit() - self.get_total_user_balance(), 2))
    def get_total_user_percent_credit_remaining(self): 
        return str(round(100.*(1.*self.get_total_user_credit_limit() - self.get_total_user_balance()) / self.get_total_user_credit_limit(), 2))
    def get_total_user_decimal_credit_remaining(self):
        return str(round(((1.*self.get_total_user_credit_limit() - self.get_total_user_balance()) / self.get_total_user_credit_limit()), 3))
    def get_total_user_fractional_credit_remaining(self): 
        return str(round(1.*self.get_total_user_credit_limit() - self.get_total_user_balance(), 2)) + "/" + str(round(self.get_total_user_credit_limit(), 2))
    
    def get_aggregate_card_financial_report(self):
        print 
        print "aggregate financial report for " + self.username
        print "total credit used in dollars = $" + self.get_total_user_dollar_credit_used()
        print "% of total credit used = " + self.get_total_user_percent_credit_used() + "%"
        print "decimal fraction of total credit used = " +self.get_total_user_decimal_credit_used()
        print "fraction of total credit used = " + self.get_total_user_fractional_credit_used()
        print "total credit remaining in dollars = $" + self.get_total_user_dollar_credit_remaining()
        print "% of total credit credit remaining = " + self.get_total_user_percent_credit_remaining() + "%"
        print "decimal fraction of total credit remaining = " +self.get_total_user_decimal_credit_remaining()
        print "fraction of total credit remaining = " + self.get_total_user_fractional_credit_remaining()
        print
    
    
    def choose_optimal_card(self, purchase):
        #compare purchase keyword with those keywords of the cards for rewards and return the card with better user_preference
        #use rewards to test rewards based on preferences
        #use wallet for to drill down on cards
        #Minimize interest paid, Maximize Points, maximize cash back, Minimize % credit used per card
        card_array = [card for card in  self.wallet.keys() if self.wallet[card].is_feasible_purchase(purchase)]
        points_card_array = [card for card in card_array if "Points" in self.wallet[card].rewards_type and (self.wallet[card].rewards_points_base_rate != None or purchase.tag not in self.wallet[card].rewards_special_items_points_rates.keys())]
        #cash_back_card_array = [card for card in card_array if "Cash Back" in self.wallet[card].rewards_type and (self.wallet[card].rewards_cash_back_base_rate != None or purchase.tag not in self.wallet[card].rewards_special_items_cash_back_rates.keys())]
        if len(self.wallet.keys()) == 0: 
            print "no cards in the account"
            return None
        elif len(card_array) == 0: 
            print "no feasible cards to use"
            return None
        elif len(card_array) == 1: 
            return self.wallet[card_array[0]] 
        else: 
            if "minimize interest paid" == self.reward_structure_preference or len(points_card_array)==0:#and len(cash_back_card_array)==0):
                card_last4_interest_dict = {}
                for card in self.wallet.keys():
                    card_last4_interest_dict[card] = self.wallet[card].annual_interest_rate
                card_last4_interest_tuple = min(card_last4_interest_dict.items(), key=lambda x: x[1])
                print card_last4_interest_tuple
                return self.wallet[card_last4_interest_tuple[0]] 
            #WORK ON THIS
            elif "maximize points" == self.reward_structure_preference:
                if len(points_card_array) == 1: return self.wallet[points_card_array[0]] 
                else:
                    card_last4_max_points_dict = {}
                    for card in self.wallet.keys():
                        card_last4_max_points_dict[card] = self.wallet[card].theoretical_points_from_purchase(purchase)
                    card_last4_max_points_tuple = max(card_last4_max_points_dict.items(), key=lambda x: x[1])
                    print card_last4_max_points_tuple
                    return self.wallet[card_last4_max_points_tuple[0]] 
            #elif "maximize cash back" == self.reward_structure_preference:
                #if len(cash_back_card_array) == 1: return self.wallet[cash_back_card_array[0]] 
                #else:
                    #max_cash_back_card = cash_back_card_array[0]
                    #for i in range(1, len(cash_back_card_array)):
                        #if self.wallet[cash_back_card_array[i]].theoretical_cash_back_from_purchase(purchase) > self.wallet[max_cash_back_card].theoretical_cash_back_from_purchase(purchase):
                            #max_cash_back_card = cash_back_card_array[i]
                        #return self.wallet[cash_back_card_array[max_cash_back_card]] 
            #elif "minimize % credit used per card" == self.reward_structure_preference:
                #W0RK on this#W0RK on this#W0RK on this#W0RK on this#W0RK on this#W0RK on this#W0RK on this#W0RK on this
                pass
                '''
	        if len(card_array) == 1: return self.wallet[cash_back_card_array[0]] 
                else:
                    max_cash_back_card = cash_back_card_array[0]
                    for i in range(1, len(cash_back_card_array)):
                        if self.wallet[cash_back_card_array[i]].theoretical_cash_back_from_purchase(purchase) > self.wallet[max_cash_back_card].theoretical_cash_back_from_purchase(purchase):
                            max_cash_back_card = cash_back_card_array[i]
                        return self.wallet[cash_back_card_array[max_cash_back_card]] 
                '''
        

    #choose best card given user preferenece and apply purchase to balances and display renewed financial report for both the card used and the aggregate
    def apply_purchase_user_rewards(self, purchase):
        #display post purchase card specific financial information and rewards as well as aggregate financial report and rewards 
        #use wallet for to drill down on cards
        optimal_card = self.choose_optimal_card(purchase)
        if optimal_card == None:
            print "no feasible cards for purchase"
            return
        else:
            optimal_card.get_card_info()  
            print "Current card balance = " + str(optimal_card.balance)
            print "Purchase Description: " + purchase.product_description
            self.wallet[optimal_card.last4digits].update_balance(optimal_card.balance+purchase.get_purchase_price())       
            if None != optimal_card.rewards_type: 
                if "Points" in optimal_card.rewards_type:
                    optimal_card.analyze_points_info_from_purchase(purchase)
                    self.wallet[optimal_card.last4digits].rewards_points = optimal_card.theoretical_points_post_purchase(purchase)
                if "Cash Back" in optimal_card.rewards_type:
                    optimal_card.analyze_cash_back_info_from_purchase(purchase)
                    self.wallet[optimal_card.last4digits].rewards_cash_back = optimal_card.theoretical_cash_back_post_purchase(purchase)
                    self.wallet[optimal_card.last4digits].update_balance(self.balance-optimal_card.theoretical_cash_back_from_purchase(purchase))
                self.wallet[optimal_card.last4digits].print_rewards() 
            self.transaction_id += 1
            self.transactions[self.transaction_id] = [purchase, optimal_card.last4digits]              
            print "New card balance = " + str(self.wallet[optimal_card.last4digits].balance)  
            self.get_aggregate_card_financial_report()
            raw_input()

    def user_menu(self):
        '''
        ICE_User_DBtest = {}
        fname = 'ICE_User_DBtest.pkl'   
        try:
            ICE_User_DBtest = pickle.load( open( fname, "rb" ) )
            print "file "+ fname + " loaded"
        except IOError, e:
            print "Error writing file: " + str(e)    
        '''
        
        os.system('cls')
        print """
        ========================================
        ICE – INTELLIGENT CARD ENGINE
        ========================================
        1 - Add a Credit Card to your account
        2 - Update a Credit Card in your account
        3 - Display Credit Card Information
        4 - Display Credit Report Options
        5 - Delete a Credit Card from your account
        6 - Run Credit Optimizer
        7 - Make a Purchase
        8 - Export account data to CSV
        9 - Exit
        ================================
        """
        choice = raw_input("Enter a choice and press enter:  ")
    
        while choice != "9":    
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                self.add_card_to_wallet()
                #choice = self.user_menu()
                raw_input()
            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                self.update_card_in_wallet()
                raw_input()
                #choice = self.user_menu()
            elif choice == "3":
                os.system('cls')
                self.display_cards_in_wallet()
                raw_input()
                #choice = self.user_menu()
            elif choice == "4":
                self.display_financial_reports()
                raw_input()
                #choice = self.user_menu()
            elif choice == "5":
                last4digits = raw_input("last 4 digits of card you'd like to delete: ")
                self.wallet[last4digits] = None
                raw_input()
                #choice = self.user_menu()
            elif choice == "6":
                #run optimizer on a given purchase, at close of analysis ask if user would like to apply the purchase
                self.run_optimizer()
                raw_input()
            elif choice == "7":
                #allow a user to enter a purchase and have it added under the user specified optimization
                new_purchase = purchase(raw_input("purchase category: "), raw_input("unit price: "), raw_input("units: "),raw_input("company: "),raw_input("description: "))
                self.apply_purchase_user_rewards(new_purchase)
                raw_input()
            elif choice == "8":
                csvreport_reports.Write_Card_to_CSV()
                #choice = self.user_menu()
            elif choice == "9":
                '''
                try:
                    with open(fname, 'w') as fout:
                        pickle.dump(ICE_User_DBtest, fout)
                        print "printed to file "+ fname
                except IOError, e:
                    print "Error writing file: " + str(e)
                '''
                print "Signed Out"
                return
            #choice = raw_input("Enter a choice and press enter:  ")
            return self.user_menu()
        
    #TAKE USER INPUT AND RUN FUNCTION TO INSERT Credit Card into user account
    def add_card_to_wallet(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
        print """
        ==================================
        Add a Credit Card to your account:
        ==================================
            """
        credit_card_company = None
        while None == credit_card_company: 
            print """
            Select the card type:
                1 - American Express
                2 - Visa
                3 - MasterCard
                4 - Discover
                """
            credit_card_company = raw_input("Enter a choice and press enter:  ")
            if credit_card_company == "1":
                credit_card_company = "American Express"
            elif credit_card_company == "2":
                credit_card_company = "Visa"
            elif credit_card_company == "3":
                credit_card_company = "MasterCard"
            elif credit_card_company == "4":
                credit_card_company = "Discover"
            else:
                credit_card_company = None
                print "ERROR ADDING RECORD!"    
        
        Last4Digits = None  
        while None == Last4Digits or len(Last4Digits) != 4: 
            Last4Digits = raw_input("Enter the last 4 digits of the card: ")
        
        expiration_date = None
        while None == expiration_date or len(expiration_date) != 5: 
            expiration_date = raw_input("Enter the expiration date (mm/dd): ")
    
        Bank = None
        if credit_card_company != "American Express":
            while None == Bank: 
                print """
                Select the financial institution backing the credit:
                    1 - Chase
                    2 - Bank of America
                    3 - Wells Fargo
                    4 - HSBC
                    5 - CapitalOne
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
                else:
                    Bank = None
                    print "ERROR ADDING RECORD!"
                
        annualInterestRate = None
        while annualInterestRate < 0 or annualInterestRate > 1.00:
            annualInterestRate = raw_input("What is the yearly specified interest rate on the balance outstanding(enter data for 17.24% as 0.1724): ")
            annualInterestRate = float(annualInterestRate)
        
        credit_limit = None
        while credit_limit == None or credit_limit <= 0 or credit_limit == "":
            credit_limit = raw_input("What is the credit limit on the card ending in " + str(Last4Digits) + ": ")
            credit_limit = float(credit_limit)
        
        min_monthly_payment_rate = None
        while min_monthly_payment_rate == None: 
            min_monthly_payment_rate = raw_input("What is the minimum monthly payment rate on the balance outstanding(enter data for 5.24% as 0.0524): ")
            min_monthly_payment_rate  = float(min_monthly_payment_rate)
        
        balance = None
        while balance == None: 
            balance = raw_input("What is the balance on the card (enter a positive number if there is debt outstanding on the card): ")
            balance  = float(balance)
        
        
        #####WORK ON THIS!!!!!!!!#######################
        transactions = None             
        #while None == transactions:
                #transactions = raw_input("If the card has currently has any cash back enter the amount otherwise enter 0: ")
                #transactions =    
        
        rewards_type = None
        while None == rewards_type: 
            print """
            Select the rewards type for the card:
                1 - Points
                2 - Cash Back
                3 - Points & Cash Back
                4 - No Rewards
                """
            rewards_type = raw_input("Enter a choice and press enter:  ")
            if rewards_type == "1":
                rewards_type= "Points"
            elif rewards_type == "2":
                rewards_type = "Cash Back"
            elif rewards_type == "3":
                rewards_type = "Points & Cash Back"
            elif rewards_type == "4":
                rewards_type = None
                break
            else:
                rewards_type = None
                print "ERROR ADDING REWARDS!"
            
        if None == rewards_type:
            rewards_points = None
            rewards_points_base_rate = None
            rewards_special_items_points_rates = {}
            rewards_cash_back = None
            rewards_cash_back_base_rate = None
            rewards_special_items_cash_back_rates = {}
            self.wallet[Last4Digits] = Credit_Card_Class_w_Rwrds.credit_card(credit_card_company, Last4Digits, expiration_date, Bank, 
                annualInterestRate, credit_limit, min_monthly_payment_rate, balance, transactions,
                rewards_type, rewards_points, rewards_points_base_rate, rewards_special_items_points_rates,
                rewards_cash_back, rewards_cash_back_base_rate, rewards_special_items_cash_back_rates)

        elif None != rewards_type:
            rewards_points = None
            if "Points" in rewards_type:                
                while None == rewards_points or rewards_points < 0:
                    rewards_points = raw_input("If the card has currently has any points enter the amount otherwise enter 0: ")
                    rewards_points  = int(rewards_points)
            

            rewards_points_base_rate = None
            if "Points" in rewards_type:                
                while None == rewards_points or rewards_points_base_rate < 0:
                    rewards_points_base_rate = raw_input("If the card has a base rate for points across purchases enter the rate as a decimal otherwise enter 0: ")
                    rewards_points_base_rate  = float(rewards_points_base_rate)

            rewards_special_items_points_rates = {}
            if "Points" in rewards_type:
                choice = raw_input("Are there any categories that would receieve special points rates per purchase? (yes/no): ")                
                while choice.lower() != "no":
                    if choice.lower() == "yes":
                        key = raw_input("Enter the category to receive special rates: ")
                        value = raw_input("Enter the rate as a decimal: ")
                        value = float(value)
                        rewards_special_items_points_rates[key] = value
                    choice = raw_input("Are there any categories that would receieve special points rates per purchase? (yes/no): ")
        
            rewards_cash_back = None
            if "Cash Back" in rewards_type:                
                while None == rewards_cash_back or rewards_cash_back < -.5:
                    rewards_cash_back = raw_input("If the card has currently has any cash back enter the amount otherwise enter 0: ")
                    rewards_cash_back  = float(rewards_cash_back) 
            
            rewards_cash_back_base_rate = None
            if "Cash Back" in rewards_type:                
                while None == rewards_cash_back_base_rate or rewards_cash_back_base_rate < 0:
                    rewards_cash_back_base_rate = raw_input("If the card has a base rate for cash back across purchases enter the rate as a decimal otherwise enter 0: ")
                    rewards_cash_back_base_rate = float(rewards_cash_back_base_rate)   
                    if 0 == int(rewards_cash_back_base_rate): break
            
            rewards_special_items_cash_back_rates = {}
            if "Cash Back" in rewards_type:
                choice = raw_input("Are there any categories that would receieve special cash back rates per purchase? (yes/no): ")                
                while choice.lower() != "no":
                    if choice.lower() == "yes":
                        key = raw_input("Enter the category to receive special rates: ")
                        value = raw_input("Enter the rate as a decimal: ")
                        value = float(value)
                        rewards_special_items_cash_back_rates[key] = value
                    choice = raw_input("Are there any categories that would receieve special points rates per purchase? (yes/no): ")
       
        self.wallet[Last4Digits] = Credit_Card_Class_w_Rwrds.credit_card(credit_card_company, Last4Digits, expiration_date, Bank, 
                annualInterestRate, credit_limit, min_monthly_payment_rate, balance, transactions,
                rewards_type, rewards_points, rewards_points_base_rate, rewards_special_items_points_rates,
                rewards_cash_back, rewards_cash_back_base_rate, rewards_special_items_cash_back_rates)
    
    def update_card_rewards(self, last4digits = None):
        for key in self.wallet.keys(): 
            self.wallet[key].get_card_info()
        if last4digits == None: 
            last4digits = raw_input("Please enter the last 4 digits of the card you'd like to update: ")

        print """
        ========================================
        Update a card in your account:
        ========================================
        1  - Update the rewards type
        2  - Update the current number of rewards points 
        3  - Update the base rate for rewards points on purchases
        4  - Update the rewards points rates for special categories
        5  - Update the cash back earned
        6  - Update the base rate for cash back earned on purchases
        7  - Update the rates for cash back earned on special categories
        8  - Exit
        ================================
        """
        choice = raw_input("Enter a choice and press enter:  ")
    
        while choice != "8":    
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                updated_rewards_type = None
                while None == updated_rewards_type: 
                    print """
                    Select the rewards type for the card:
                        1 - Points
                        2 - Cash Back
                        3 - Points & Cash Back
                        4 - No Rewards
                        """
                    updated_rewards_type = raw_input("Enter a choice and press enter:  ")
                    if updated_rewards_type == "1":
                        updated_rewards_type = "Points"
                    elif updated_rewards_type == "2":
                        updated_rewards_type = "Cash Back"
                    elif updated_rewards_type == "3":
                        updated_rewards_type = "Points & Cash Back"
                    elif updated_rewards_type == "4":
                        updated_rewards_type = None
                        updated_rewards_points = None
                        self.wallet[last4digits].update_rewards_points(updated_rewards_points)
                        updated_rewards_points_base_rate = None
                        self.wallet[last4digits].update_rewards_points_base_rate(updated_rewards_points_base_rate)
                        updated_rewards_cash_back = None
                        self.wallet[last4digits].update_rewards_cash_back(updated_rewards_cash_back)
                        self.wallet[last4digits].rewards_cash_back_base_rate = None
                        self.wallet[last4digits].rewards_special_items_points_rates = {}
                        self.wallet[last4digits].rewards_special_items_cash_back_rates = {}
                        choice = 8
                        break
                    else:
                        updated_rewards_type = None
                        print "ERROR ADDING REWARDS!"
                self.wallet[last4digits].update_rewards_type(updated_rewards_type)
                #choice = self.update_card_in_wallet(last4digits)
            
            elif choice == "2":
                raw_input()
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                if None != self.wallet[last4digits].rewards_type:
                    updated_rewards_points = None
                    if "Points" in self.wallet[last4digits].rewards_type:                
                        while None == updated_rewards_points or updated_rewards_points < 0:
                            updated_rewards_points = raw_input("If the card has currently has any points enter the amount otherwise enter 0: ")
                            updated_rewards_points = int(updated_rewards_points)
                    self.wallet[last4digits].update_rewards_points(updated_rewards_points)
                #choice = self.update_card_in_wallet(updated_last4digits)
            
            elif choice == "3":
                os.system('cls')
                if None != self.wallet[last4digits].rewards_type:
                    updated_rewards_points_base_rate = None
                    if "Points" in self.wallet[last4digits].rewards_type:                
                        while None == updated_rewards_points_base_rate or updated_rewards_points_base_rate < 0:
                            updated_rewards_points_base_rate = raw_input("If the card has a base rate for points across purchases enter the rate as a decimal otherwise enter 0: ")
                            updated_rewards_points_base_rate  = float(updated_rewards_points_base_rate)
                    self.wallet[last4digits].update_rewards_points_base_rate(updated_rewards_points_base_rate)

            
            elif choice == "4":
                raw_input()
                os.system('cls')
                if None != self.wallet[last4digits].rewards_type:
                    if "Points" in self.wallet[last4digits].rewards_type: 
                        choice1 = raw_input("Are there any categories that would receieve special points rates per purchase? (yes/no): ")                
                        while choice1.lower() != "no":
                            if choice1.lower() == "yes":
                                key = raw_input("Enter the category to receive special rates: ")
                                value = raw_input("Enter the rate as a decimal: ")
                                value = float(value)
                                self.wallet[last4digits].update_rewards_special_items_points_rates(key, value)
                            choice1 = raw_input("Are there any categories that would receieve special points rates per purchase? (yes/no): ")
                
            
            elif choice == "5":
                raw_input()
                os.system('cls')
                if None != self.wallet[last4digits].rewards_type:
                    updated_rewards_cash_back = None
                    if "Cash Back" in self.wallet[last4digits].rewards_type:                
                        while None == updated_rewards_cash_back or updated_rewards_cash_back < -.5:
                            updated_rewards_cash_back = raw_input("If the card has currently has any cash back enter the amount otherwise enter 0: ")
                            updated_rewards_cash_back  = float(updated_rewards_cash_back) 
                    self.wallet[last4digits].update_rewards_cash_back(updated_rewards_cash_back)
            
            elif choice == "6":
                raw_input()
                os.system('cls')
                if None != self.wallet[last4digits].rewards_type:
                    updated_rewards_cash_back_base_rate = None
                    if "Cash Back" in self.wallet[last4digits].rewards_type:                
                        while None == updated_rewards_cash_back_base_rate or updated_rewards_cash_back_base_rate < 0:
                            updated_rewards_cash_back_base_rate = raw_input("If the card has a base rate for cash back across purchases enter the rate as a decimal otherwise enter 0: ")
                            updated_rewards_cash_back_base_rate = float(updated_rewards_cash_back_base_rate)   
                            if 0 == int(updated_rewards_cash_back_base_rate): break
                    self.wallet[last4digits].update_rewards_cash_back_base_rate(updated_rewards_cash_back_base_rate)
            
            elif choice == "7":
                raw_input()
                os.system('cls')
                if None != self.wallet[last4digits].rewards_type:
                    if "Cash Back" in self.wallet[last4digits].rewards_type: 
                        choice1 = raw_input("Are there any categories that would receieve special cash back rates per purchase? (yes/no): ")                
                        while choice1.lower() != "no":
                            if choice1.lower() == "yes":
                                key = raw_input("Enter the category to receive special rates: ")
                                value = raw_input("Enter the rate as a decimal: ")
                                value = float(value)
                                self.wallet[last4digits].update_rewards_special_items_points_rates(key, value)
                            choice1 = raw_input("Are there any categories that would receieve special points rates per purchase? (yes/no): ")
                                        
            elif choice == "8":
                print "Update complete."
                self.get_rewards_info()
                '''                
                ICE_User_DBtest = {}
                fname = 'ICE_User_DBtest.pkl'
                try:
                    with open(fname, 'w') as fout:
                        pickle.dump(ICE_User_DBtest, fout)
                        print "printed to file "+ fname
                except IOError, e:
                    print "Error writing file: " + str(e)
                    print "Signed Out"
            '''
            else:
                print "ERROR ADDING RECORD!" 
            return self.update_card_in_wallet(last4digits)
            
    #Update a card
    #####WORK ON THIS!!!!!!!!############################WORK ON THIS!!!!!!!!############################WORK ON THIS!!!!!!!!#######################
    #add in functionality to update rewards
    #####WORK ON THIS!!!!!!!!############################WORK ON THIS!!!!!!!!############################WORK ON THIS!!!!!!!!#######################
    def update_card_in_wallet(self, last4digits = None):
        for key in self.wallet.keys(): 
            self.wallet[key].get_card_info()
        if last4digits == None: 
            last4digits = raw_input("Please enter the last 4 digits of the card you'd like to update: ")
        print """
        ========================================
        Update a card in your account:
        ========================================
        1  - Update the credit card company
        2  - Update the cards last 4 digits
        3  - Update expiration date
        4  - Update bank information
        5  - Update annual interest rate
        6  - Update credit limit
        7  - Update minimum payment rate
        8  - Update card balance
        9  - Update card rewards 
        10 - Choose a new card to update
        11 - Exit
        ================================
        """
        choice = raw_input("Enter a choice and press enter:  ")
    
        while choice != "11":    
            if choice == "1":
                raw_input()
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                new_company = None
                while None == new_company: 
                    print """
                    Select the card type:
                        1 - American Express
                        2 - Visa
                        3 - MasterCard
                        4 - Discover
                        5 - Exit
                        """
                    new_company = raw_input("Enter a choice and press enter:  ")
                    if new_company == "1":
                        new_company = "American Express"
                    elif new_company == "2":
                        new_company = "Visa"
                    elif new_company == "3":
                        new_company = "MasterCard"
                    elif new_company == "4":
                        new_company = "Discover"
                    elif new_company == "5":
                        new_company = None
                        raw_input("Press Enter to return to the menu:  ")
                        return self.update_card_in_wallet()
                    else:
                        new_company = None
                        print "ERROR ADDING RECORD!" 
                self.wallet[last4digits].update_credit_card_company(new_company)
                #choice = self.update_card_in_wallet(last4digits)
            
            elif choice == "2":
                raw_input()
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                updated_last4digits = None  
                while None == updated_last4digits or len(updated_last4digits) != 4: 
                    updated_last4digits = raw_input("Enter the last 4 digits of the card: ")
                self.wallet[updated_last4digits] = self.wallet[last4digits]
                self.wallet[last4digits] = None
                #choice = self.update_card_in_wallet(updated_last4digits)
            
            elif choice == "3":
                raw_input()
                os.system('cls')
                new_expiration_date = None
                while None == new_expiration_date or len(new_expiration_date) != 5: 
                    new_expiration_date = raw_input("Enter the expiration date (mm/dd): ")
                self.wallet[last4digits].update_expiration_date(new_expiration_date)
                #choice = self.update_card_in_wallet(last4digits)
            
            elif choice == "4":
                raw_input()
                os.system('cls')
                new_bank = None
                if self.wallet[last4digits].credit_card_company != "American Express":
                    while None == new_bank: 
                        print """
                        Select the financial institution backing the credit:
                            1 - Chase
                            2 - Bank of America
                            3 - Wells Fargo
                            4 - HSBC
                            5 - CapitalOne
                            6 - Exit
                            """
                        new_bank = raw_input("Enter a choice and press enter:  ")
                        if new_bank == "1":
                            new_bank = "Chase"
                        elif new_bank == "2":
                            new_bank = "Bank of America"
                        elif new_bank == "3":
                            new_bank = "Wells Fargo"
                        elif new_bank == "4":
                            new_bank = "HSBC"
                        elif new_bank == "5":
                            new_bank = "CapitalOne"
                        elif new_bank == "6":
                            new_bank = None
                            raw_input("Press Enter to return to the menu:  ")
                            return self.update_card_in_wallet(last4digits)
                        else:
                            new_bank = None
                            print "ERROR ADDING RECORD!"
                self.wallet[last4digits].update_bank(new_bank)
                #choice = self.update_card_in_wallet(last4digits)
            
            elif choice == "5":
                os.system('cls')
                new_annualInterestRate = None
                while new_annualInterestRate < 0 or new_annualInterestRate > 1.00: 
                    new_annualInterestRate = raw_input("What is the yearly specified interest rate on the balance outstanding(enter data for 17.24% as 0.1724): ")
                    new_annualInterestRate = float(new_annualInterestRate)
                self.wallet[last4digits].update_annual_interest_rate(new_annualInterestRate)
                #choice = self.update_card_in_wallet(last4digits)   
            
            elif choice == "6":
                os.system('cls')
                new_credit_limit = None
                while new_credit_limit == None or new_credit_limit <= 0:
                    new_credit_limit = raw_input("What is the credit limit on the card ending in " + str(last4digits) + ": ")
                    new_credit_limit  = float(new_credit_limit)
                self.wallet[last4digits].update_credit_limit(new_credit_limit)
                #choice = self.update_card_in_wallet(last4digits)
            
            elif choice == "7":
                os.system('cls')
                new_min_monthly_payment_rate = None
                while new_min_monthly_payment_rate == None: 
                    new_min_monthly_payment_rate = raw_input("What is the minimum monthly payment rate on the balance outstanding(enter data for 5.24% as 0.0524): ")
                    new_min_monthly_payment_rate  = float(new_min_monthly_payment_rate)
                self.wallet[last4digits].update_credit_limit(new_min_monthly_payment_rate)
                #choice = self.update_card_in_wallet(last4digits)
                
            elif choice == "8":
                os.system('cls')
                new_balance = None
                while new_balance == None: 
                    new_balance = raw_input("What is the balance on the card (enter a positive number if there is debt outstanding on the card): ")
                    new_balance = float(new_balance)
                self.wallet[last4digits].update_balance(new_balance)
                #choice = self.update_card_in_wallet(last4digits)

            elif choice == "9":
                os.system('cls')   
                self.update_card_rewards(last4digits)                    
                #choice = self.update_card_in_wallet(next_4_digits)

            elif choice == "10":
                os.system('cls')   
                next_4_digits = None 
                while None == next_4_digits or len(next_4_digits) != 4 or next_4_digits not in self.wallet.keys(): 
                    next_4_digits = raw_input("Enter the last 4 digits of the card: ")
                #choice = self.update_card_in_wallet(next_4_digits)
                                        
            elif choice == "11":
                print "Update complete."
                '''                
                ICE_User_DBtest = {}
                fname = 'ICE_User_DBtest.pkl'
                try:
                    with open(fname, 'w') as fout:
                        pickle.dump(ICE_User_DBtest, fout)
                        print "printed to file "+ fname
                except IOError, e:
                    print "Error writing file: " + str(e)
                    print "Signed Out"
            '''
            else:
                print "ERROR ADDING RECORD!"
                #choice = self.update_card_in_wallet(last4digits)
            return self.user_menu()
            
                                    
    def display_cards_in_wallet(self):
        print """
        ============================================
        Credit Information Options:
        ============================================
        1 - Display a single card
        2 - Display all cards
        3 - Display cards filtered by credit company (stub)
        4 - Display cards filtered by credit bank (stub)
        5 - Display cards filtered by user (stub)
        6 - Display cards ordered by expiration date (stub)
        7 - Exit
        ====================================
        """
        choice = raw_input("Enter a choice and press enter:  ")
    
        while choice != "7":    
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                last4digits = None 
                
                while None == last4digits or len(last4digits) != 4: 
                    last4digits = raw_input("Please enter the last 4 digits of the card you'd like to view: ")
                #self.wallet[last4digits].get_card_info()
                self.wallet[last4digits].get_rewards_info()
                choice = self.display_cards_in_wallet()
            
            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                for key in self.wallet.keys(): 
                    self.wallet[key].get_rewards_info()
                    #self.wallet[key].get_card_info()
                choice = self.display_cards_in_wallet()
            
            elif choice == "3":
                os.system('cls')
                pass
                choice = self.display_cards_in_wallet()
            
            elif choice == "4":
                os.system('cls')
                if raw_input("Press Enter to return to the menu:  "):
                    return self.display_cards_in_wallet()
                else:
                    print "ERROR ADDING RECORD!"
                self.wallet[last4digits].update_bank()
                choice = self.display_cards_in_wallet()
            
            elif choice == "5":
                os.system('cls')
                pass
                choice = self.display_cards_in_wallet()  
            
            elif choice == "6":
                os.system('cls')
                new_credit_limit = None
                pass
                choice = self.display_cards_in_wallet()
            
            elif choice == "7":
                print "Exiting Card Display Menu."
                '''                
                ICE_User_DBtest = {}
                fname = 'ICE_User_DBtest.pkl'
                try:
                    with open(fname, 'w') as fout:
                        pickle.dump(ICE_User_DBtest, fout)
                        print "printed to file "+ fname
                except IOError, e:
                    print "Error writing file: " + str(e)
                    print "Signed Out"
                '''
                choice = 7
            else:
                print "ERROR VIEWING RECORD!"
                choice = self.display_cards_in_wallet()
            return self.user_menu()

    def display_financial_reports(self):
        print """
        =======================================================
        Credit Report Options:
        =======================================================
        1 - Display financial report for a single card
        2 - Display financial reports for all cards in account (card by card)
        3 - Display financial reports for all cards in account (aggregate report)
        4 - Display cards filtered by credit bank (stub)
        5 - Display cards filtered by issuing company (stub)
        6 - Display cards ordered by credit remaining (stub)
        7 - Exit
        ====================================
        """
        choice = raw_input("Enter a choice and press enter:  ")
    
        while choice != "7":    
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                last4digits = None 
                
                while None == last4digits or len(last4digits) != 4: 
                    last4digits = raw_input("Please enter the last 4 digits of the card's financials you'd like to view: ")
                self.wallet[last4digits].get_card_financial_report()
                choice = self.display_financial_reports()
                raw_input()
            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print '\n'*100
                for key in self.wallet.keys(): 
                    self.wallet[key].get_card_financial_report()
                choice = self.display_financial_reports()
                raw_input()
            elif choice == "3":
                os.system('cls')
                self.get_aggregate_card_financial_report()
                #choice = self.display_financial_reports()
                raw_input()
                
            elif choice == "4":
                os.system('cls')
                self.wallet[last4digits].update_bank(new_bank)
                choice = self.display_financial_reports()
                raw_input()
                
            elif choice == "5":
                os.system('cls')
                new_annualInterestRate = None
                while new_annualInterestRate < 0 or new_annualInterestRate > 1.00: 
                    new_annualInterestRate = raw_input("What is the yearly specified interest rate on the balance outstanding(enter data for 17.24% as 0.1724): ")
                    new_annualInterestRate = float(new_annualInterestRate)
                self.wallet[last4digits].update_annual_interest_rate(new_annualInterestRate)
                choice = self.display_financial_reports()   
                raw_input()
            elif choice == "6":
                os.system('cls')
                new_credit_limit = None
                while new_credit_limit == None or new_credit_limit <= 0:
                    new_credit_limit = raw_input("What is the credit limit on the card ending in " + str(last4digits) + ": ")
                    new_credit_limit  = float(new_credit_limit)
                self.wallet[last4digits].update_credit_limit(new_credit_limit)
                choice = self.display_financial_reports()
                raw_input()
            elif choice == "7":
                print "Exiting Financial Reporting Menu."
                '''                
                ICE_User_DBtest = {}
                fname = 'ICE_User_DBtest.pkl'
                try:
                    with open(fname, 'w') as fout:
                        pickle.dump(ICE_User_DBtest, fout)
                        print "printed to file "+ fname
                except IOError, e:
                    print "Error writing file: " + str(e)
                    print "Signed Out"
                '''
                choice = 7
            else:
                print "ERROR VIEWING RECORD!"
                #may need to remove this last line to limit # of exits required
                choice = self.display_cards_in_wallet()
            return self.user_menu()               
