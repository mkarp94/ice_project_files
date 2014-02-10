#card implementation
class credit_card(object):
    def __init__(self, credit_card_company, last4digits, expiration_date, bank, annual_interest_rate, credit_limit, min_monthly_payment_rate, balance = 0, rewards = None):
        self.credit_card_company = credit_card_company
        self.last4digits = last4digits
        self.expiration_date = expiration_date
        self.bank = bank
        self.annual_interest_rate = annual_interest_rate
        self.monthly_interest_rate = self.annual_interest_rate / 12.0
        self.balance = balance
        self.credit_limit = credit_limit
        self.min_monthly_payment_rate = min_monthly_payment_rate
        self.rewards = rewards  

    def __str__(self):
        return str(self.credit_card_company) +" "+ str(self.last4digits) +" "+  str(self.expiration_date) + "\n" +  self.card_expiration_reminder()
    def get_credit_card_company(self):
        return self.credit_card_company 
    
    def update_credit_card_company(self)
    
    def get_min_monthly_payment(self):
        return 1.0*self.min_monthly_payment_rate*self.balance

    def get_credit_card(self):
        return self.credit_card_company
    
    def get_bank(self):
        return self.bank
    def update_bank(self, new_bank):
        self.bank = new_bank
        
    def get_expiration_date(self, new_expiration_date):
        return self.expiration_date     
    def update_expiration_date(self, new_expiration_date):
        self.expiration_date = new_expiration_date   
            
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
    
    #allows a credit card holder to determine the balance after x_months of a fixed monthly_payment amount without applying the payment
    def get_theoretical_balance_after_x_payments(self, x_months = None, monthly_payments = None):
        if x_months == None: x_months = 1
        if monthly_payments == None: monthly_payments = self.get_min_monthly_payment()      
        if x_months < 1: raise ValueError        
        balance = self.balance
        for i in range(x_months):
            balance -= monthly_payments
            balance*= (1+self.monthly_interest_rate)
        return round(balance, 2)
    
    #will calculate the number of months and years to pay off the remaining balance
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

    def get_credit_limit(self):
        return self.credit_limit
    def update_credit_limit(self, new_limit):
        self.credit_limit = new_limit    
    
    def get_percent_credit_remaining(self):
        return 1.*self.get_credit_remaining()/self.credit_limit
    def get_percent_credit_used(self):
        return 1.*self.balance/self.credit_limit 

    def get_min_monthly_payment_rate(self):
        return self.min_monthly_payment_rate
    def update_min_monthly_payment_rate(self, new_monthly_payment_rate):
        self.min_monthly_payment_rate = new_monthly_payment_rate
        
    def get_credit_remaining(self):
        return round(self.credit_limit - self.balance, 2)
    
    def card_expiration_reminder(self):
        reminder = "Reminder: Your card expires this year."
        expiration_year = self.expiration_date[-2]+self.expiration_date[-1]
        if expiration_year == "14": return reminder
        else: return ""

    def get_card_type(self):
        return self.rewards

    '''
    #allows a credit card holder to determine the fixed monthly payment required to clear debts on this card
    def get_required_fixed_payment_to_clear_debt_after_x_months(self, x_months = None, monthly_payment = None):
        if x_months == None: x_months = 12
        if monthly_payment == None: monthly_payment = self.get_min_monthly_payment()     
        new_balance = self.balance
        low = new_balance/12
        high = (new_balance*(1+self.monthly_interest_rate)**12)/12.
        monthly_payment = (high + low)/2.0
        while self.get_theoretical_balance_after_x_payments(x_months, monthly_payment) != 0:
            print self.get_theoretical_balance_after_x_payments(x_months, monthly_payment)
            if self.get_theoretical_balance_after_x_payments(x_months, monthly_payment) > 0:
                low = monthly_payment
            else:
                high = monthly_payment
            monthly_payment = (high + low)/2.0        
        return ("Lowest Payment:", round(monthly_payment,2))

    #will calculate the number of months and years to pay off the remaining balance
    def time_to_clear_debt_min_current_payment(self):
        num_months = 0
        num_months = 0
        initial_min_payment = myvisa.get_min_monthly_payment()
        while myvisa.get_balance()-initial_min_payment > 0:
            myvisa.advance_x_months_payments()
            print myvisa.get_balance()
            print myvisa.get_credit_remaining()
            num_months+=1
        num_years = num_months/12
        return str(num_years) + " years, " + str(num_months%12) + " months"
    '''
    
