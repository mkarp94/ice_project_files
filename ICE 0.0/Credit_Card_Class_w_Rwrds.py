from Purchase_Class import *
#card implementation

class credit_card(object):
    def __init__(self, credit_card_company, last4digits, expiration_date, bank, 
                annual_interest_rate, credit_limit, min_monthly_payment_rate, balance = 0, transactions = {},
                rewards_type = None, rewards_points = None, rewards_points_base_rate = None, rewards_special_items_points_rates = {},
                rewards_cash_back = None, rewards_cash_back_base_rate = None, rewards_special_items_cash_back_rates = {}):
        self.credit_card_company = credit_card_company #card issuing company
        self.last4digits = last4digits #last 4 digits of the card, used as card identifier in a users account 
        self.expiration_date = expiration_date #card expiration date mm/yy
        self.bank = bank #credit backng institution
        self.annual_interest_rate = annual_interest_rate # interest rate assigned by bank
        self.monthly_interest_rate = self.annual_interest_rate / 12.0 #monthly interest rate on a yearly compound model
        self.balance = balance #credit outstanding
        self.credit_limit = credit_limit #number to be determine by the bank
        self.min_monthly_payment_rate = min_monthly_payment_rate #%of credit_balance due as a minimum payment each month    
        self.rewards_type = rewards_type #Points, Cash and Cash & Points, None
        self.rewards_points = rewards_points #Points accumulate, initialized to none only set to 0 if "points" in self.rewards_type
        self.rewards_points_base_rate = rewards_points_base_rate #%of payment received in rewards for any non_special purchase initialized to 0
        self.rewards_special_items_points_rates = rewards_special_items_points_rates
        self.rewards_cash_back = rewards_cash_back
        self.rewards_cash_back_base_rate = rewards_cash_back_base_rate
        self.rewards_special_items_cash_back_rates = rewards_special_items_cash_back_rates

        
    '''
    def __str__(self):
        return self.credit_card_company +" "+ self.last4digits +" "+  self.expiration_date
    '''

    def get_credit_card_company(self):
        return self.credit_card_company 
    
    def update_credit_card_company(self, updated_credit_company):
        self.credit_card_company = updated_credit_company
    
    def get_last4digits(self):
        return self.last4digits 
    
    def update_last4digits(self, updated_last4digits):
        self.last4digits = updated_last4digits

    def get_expiration_date(self):
        return self.expiration_date     
    
    def update_expiration_date(self, new_expiration_date):
        self.expiration_date = new_expiration_date       

    def get_bank(self):
        return self.ban
    def update_bank(self, new_bank):
        self.bank = new_bank

    def get_min_monthly_payment(self):
        return 1.0*self.min_monthly_payment_rate*self.balance
    def update_min_monthly_payment(self, new_min_monthly_payment):
        self.min_monthly_payment = new_min_monthly_payment
               
    def get_annual_interest_rate(self):
        return self.annual_interest_rate
    def update_annual_interest_rate(self, new_annual_interest_rate):
        self.annual_interest_rate = new_annual_interest_rate
    def get_monthly_interest_rate(self):
        return self.monthly_interest_rate 
    def get_yearly_effective_rate(self):
        return (1+self.annual_interest_rate/12.)**12

    def get_balance(self):
        return round(self.balance, 2)
    def update_balance(self, new_balance):
        self.balance = new_balance
    
    def get_credit_limit(self):
        return self.credit_limit
    def update_credit_limit(self, new_limit):
        self.credit_limit = new_limit    

    def get_min_monthly_payment_rate(self):
        return self.min_monthly_payment_rate
    def update_min_monthly_payment_rate(self, new_monthly_payment_rate):
        self.min_monthly_payment_rate = new_monthly_payment_rate
        
    def card_expiration_reminder(self):
        reminder = "Reminder: Your card expires this year."
        expiration_year = self.expiration_date[-2]+self.expiration_date[-1]
        if expiration_year == "14": return reminder
        else: return ""
    
    def get_card_info(self):
        print
        print "credit card = " + self.credit_card_company
        print "last 4 Digits = " +self.last4digits
        print "expiration Date = " +self.expiration_date 
        print
        
    def get_rewards_type(self):
        return self.rewards_type 
    
    def update_rewards_type(self, updated_rewards_type):
        self.rewards_type = updated_rewards_type
    
    def get_rewards_points(self):
        if self.rewards_points != None:
            return round(self.rewards_points)

    def update_rewards_points(self, updated_rewards_points):
        self.rewards_points = updated_rewards_points
    
    def get_rewards_points_base_rate(self):
        return self.rewards_points_base_rate
    def update_rewards_points_base_rate(self, updated_rewards_points_base_rate):
        self.rewards_points_base_rate = updated_rewards_points_base_rate

    def get_rewards_cash_back(self):
        return self.rewards_cash_back 
    def update_rewards_cash_back(self, updated_rewards_cash_back):
        self.rewards_cash_back = updated_rewards_cash_back

    def get_rewards_cash_back_base_rate(self):
        return self.rewards_cash_back_base_rate
    def update_rewards_cash_back_base_rate(self, updated_rewards_cash_back_base_rate):
        self.rewards_cash_back_base_rate = updated_rewards_cash_back_base_rate
     
    def get_rewards_special_items_points_rates(self, purchase):
        if purchase.tag in self.rewards_special_items_points_rates():
            return self.rewards_special_items_points_rates[purchase.tag]
        else:
            return "No special rewards rate for " + str(purchase.tag)
    def update_rewards_special_items_points_rates(self, tag, updated_rewards_special_items_points_rates):
        if None == tag: 
            return "No special rewards rate for " + str(tag)    
        if None == self.rewards_special_items_points_rates:
            self.rewards_special_items_points_rates = {}
        self.rewards_special_items_points_rates[tag.lower()] = updated_rewards_special_items_points_rates
    
    def get_rewards_special_items_cash_back_rates(self, purchase):
        if purchase.tag in self.rewards_special_items_cash_back_rates.keys():
            return self.rewards_special_items_cash_back_rates[purchase.tag]
        else:
            return "No special rewards rate for " + str(purchase.tag)
    
    def update_rewards_special_items_cash_back_rates(self, tag, updated_rewards_special_items_cash_back_rates):
        if None == tag: 
            return "No special rewards rate for " + str(tag) 
        if None == self.rewards_special_items_cash_back_rates:
            self.rewards_special_items_cash_back_rates = {}
        self.rewards_special_items_cash_back_rates[tag.lower()] = updated_rewards_special_items_cash_back_rates     

    def theoretical_points_from_purchase(self, purchase):
        projected_points = 0
        if purchase.tag in self.rewards_special_items_points_rates.keys():
            projected_points = round(self.rewards_special_items_points_rates[purchase.tag]*1.*purchase.get_purchase_price())
            #print "Projected Rewards from this purchase under the category " + purchase.tag + " " + str(projected_points)
            return projected_points
        else:
            projected_points = round(self.rewards_points_base_rate*1.*purchase.get_purchase_price())
            #print "Projected Rewards from this purchase under the category " + purchase.tag + " " + str(projected_points)
            return projected_points
    
    def theoretical_cash_back_from_purchase(self, purchase):
        projected_cash_back = 0
        if purchase.tag in self.rewards_special_items_cash_back_rates.keys():
            projected_cash_back = round(self.rewards_special_items_cash_back_rates[purchase.tag]*1.*purchase.get_purchase_price(), 2)
            print "Projected cash back from this purchase under the category " + purchase.tag + " " + str(projected_cash_back)
            return projected_cash_back
        else:
            projected_cash_back = round(self.rewards_points_base_rate*1.*purchase.get_purchase_price(), 2)
            print "Projected cash back from this purchase under the category " + purchase.tag + " " + str(projected_cash_back)
            return projected_cash_back
       
    def theoretical_points_post_purchase(self, purchase):
        projected_points = self.theoretical_points_from_purchase(purchase)
        #print "Projected total points earned after making this purchase under the category " + purchase.tag + " :" + str(self.rewards_points + projected_points)
        return self.rewards_points + projected_points

    def theoretical_cash_back_post_purchase(self, purchase):
        projected_cash_back = self.theoretical_cash_back_from_purchase(purchase)
        print "Projected total cash back earned after making this purchase under the category " + purchase.tag + " : $" + str(self.rewards_cash_back + projected_cash_back)
        return self.rewards_cash_back + projected_cash_back
           
    def analyze_points_info_from_purchase(self, purchase):
        print "Current Rewards Pre-Purchase " + str(round(self.rewards_points, 2))
        print "Projected Rewards from this purchase " + str(self.theoretical_points_from_purchase(purchase))
        print "Rewards post purchase based on projection " + str(self.theoretical_points_post_purchase(purchase))
   
    def analyze_cash_back_info_from_purchase(self, purchase):
        print "Current Rewards Pre-Purchase " + str(round(self.rewards_points, 2))
        print "Projected Rewards from this purchase " + str(self.theoretical_cash_back_from_purchase(purchase))
        print "Rewards post purchase based on projection " + str(self.theoretical_cash_back_post_purchase(purchase))
    
    def print_rewards(self):
        if self.rewards_points != None: print "with " + str(round(self.rewards_points)) +" points"
        if self.rewards_cash_back != None: print "$"+str(round(self.rewards_cash_back, 2)) +" cash back"
        
    def print_rewards_special_items(self):
        if self.rewards_type == None: return
        if self.rewards_special_items_points_rates != None: 
            for key in self.rewards_special_items_points_rates.keys():
                print str(key) + " = " + str(self.rewards_special_items_points_rates[key])
        if self.rewards_special_items_cash_back_rates != None: 
            for key in self.rewards_special_items_cash_back_rates.keys():
                print str(key) + " = " + str(self.rewards_special_items_cash_back_rates[key])
        
    def get_rewards_info(self):
        #self.get_card_info()
        print "rewards_type = " + self.rewards_type
        print "rewards: ",
        self.print_rewards()
        self.print_rewards_special_items()
        print
    '''
    def apply_a_purchase(self, purchase):
        print "Current card balance = " + str(self.balance)
        print "Purchase Description: " + purchase.product_description
        self.update_balance(self.balance+purchase.get_purchase_price())       
        if None != self.rewards_type: 
            if "Points" in self.rewards_type:
                self.analyze_points_info_from_purchase(purchase)
                self.rewards_points = self.theoretical_cash_back_post_purchase(purchase)
            if "Cash Back" in self.rewards_type:
                self.analyze_cash_back_info_from_purchase(purchase)
                self.rewards_cash_back = self.theoretical_cash_back_post_purchase(purchase)
                self.update_balance(self.balance-self.theoretical_cash_back_from_purchase(purchase))
            self.print_rewards() 
        print "New card balance = " + str(self.balance)  
    '''
    def is_feasible_purchase(self, purchase):
        if purchase.get_purchase_price()+self.balance <= self.credit_limit:
            return True
        return False
    
############WORK ON THIS##################
    def apply_a_payment(self, payment = None):
        if payment == None: payment = self.get_min_monthly_payment()
        self.update_balance(self.balance - 1.*payment)

    def advance_x_months_payments(self, x_months = None, payment = None):
        if x_months == None: x_months = 1
        if payment == None: payment = self.get_min_monthly_payment()
        if x_months < 1: raise ValueError        
        for i in range(x_months):
            self.apply_a_payment(payment)
            self.update_balance(self.balance*(1+self.monthly_interest_rate))
        return round(self.balance, 2)
    
    ############WORK ON THIS##################
    def get_dollar_credit_used(self): 
        return str(round(self.balance, 2)) 
    def get_percent_credit_used(self): 
        return str(round(100.*(1.0*self.balance / self.credit_limit), 2))
    def get_decimal_credit_used(self):
        return str(round((1.*self.balance / self.credit_limit), 2))
    def get_fractional_credit_used(self): 
        return str(round(self.balance, 2)) + "/" + str(round(self.credit_limit, 2))
    
    def get_dollar_credit_remaining(self): 
        return str(round(self.credit_limit - self.balance, 2))
    def get_percent_credit_remaining(self): 
        return str(round(100.*(1.*self.credit_limit - self.balance) / self.credit_limit, 2))
    def get_decimal_credit_remaining(self):
        return str(round(((1.*self.credit_limit - self.balance) / self.credit_limit), 2))
    def get_fractional_credit_remaining(self): 
        return str(round(1.*self.credit_limit - self.balance, 2)) + "/" + str(round(self.credit_limit, 2))

    #update this function
    ############WORK ON THIS##################
    def get_card_financial_report(self):
        print
        print "financial report for card ending in " + self.last4digits
        print "credit used in dollars = $" + self.get_dollar_credit_used()
        print "% of credit used = " + self.get_percent_credit_used() + "%"
        print "decimal fraction of credit used = " +self.get_decimal_credit_used()
        print "fraction of credit used = " + self.get_fractional_credit_used()
        print "credit remaining in dollars = $" + self.get_dollar_credit_remaining()
        print "% of credit credit remaining = " + self.get_percent_credit_remaining() + "%"
        print "decimal fraction of credit remaining = " +self.get_decimal_credit_remaining()
        print "fraction of credit remaining = " + self.get_fractional_credit_remaining()
        print

    #allows a credit card holder to determine the balance after x_months of a fixed monthly_payment amount without applying the payment
    ############WORK ON THIS##################
    def get_theoretical_balance_after_x_payments(self, x_months = None, monthly_payments = None):
        if x_months == None: x_months = 1
        if monthly_payments == None: monthly_payments = self.get_min_monthly_payment()      
        if x_months < 1: raise ValueError        
        balance = self.balance
        for i in range(x_months):
            balance -= monthly_payments
            balance *= (1+self.monthly_interest_rate)
        return round(balance, 2)
    
    #will calculate the number of months and years to pay off the remaining balance
    ############WORK ON THIS##################
    def time_to_clear_debt_min_current_payment(self):
        num_months = 0
        balance = self.get_balance()
        initial_min_payment = self.get_min_monthly_payment()
        while balance-initial_min_payment > 0:
            balance -= self.get_min_monthly_payment()
            balance*= (1+self.monthly_interest_rate)
            num_months+=1
        num_years = num_months/12
        return str(num_years) + " years, " + str(num_months%12) + " months"

