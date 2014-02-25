from Credit_Card_Class import credit_card
from User_Class import user
myvisa = credit_card("visa", "0714", "06/14", "Chase", 0.18, 10000.00, 0.03)


print myvisa.get_dollar_credit_remaining()
print myvisa.get_balance()
myvisa.update_balance(2350.25)
print myvisa.get_dollar_credit_remaining()
print myvisa.get_balance()
print myvisa.monthly_interest_rate
print myvisa.annual_interest_rate
print myvisa.monthly_interest_rate
print myvisa.min_monthly_payment_rate
print myvisa.get_min_monthly_payment()
print myvisa.get_balance()

print myvisa.get_theoretical_balance_after_x_payments()
print myvisa.get_theoretical_balance_after_x_payments(12)
#print myvisa.get_required_fixed_payment_to_clear_debt_after_x_months(10)
print myvisa.get_balance()
print myvisa.advance_x_months_payments(2)
print myvisa.get_balance()
print myvisa.get_card_info()
print myvisa.get_card_financial_report()


#print myvisa.time_to_clear_debt_min_payment()
myvisa2 = myvisa

print "testing_pickled_file"
import pickle
'''
fname = 'User_DB.pkl'

Test_User_DB = {"MK":myvisa, "JK":myvisa2}
pickle.dump( Test_User_DB, open( "save.p", "wb" ) )

try:
    with open(fname, 'w') as fout:
        pickle.dump(Test_User_DB, fout)
        print "printed to file "+ fname
except IOError, e:
    print "Error writing file: " + str(e)
'''
fname = 'Test_User_DB1.pkl'
Test_User_DB1 = {}

try:
    Test_User_DB1 = pickle.load( open( fname, "rb" ) )
    print "file "+ fname + " loaded"
except IOError, e:
    print "Error writing file: " + str(e)


#print Test_User_DB1["MK"].get_balance()
#print Test_User_DB1["JK"].get_balance()
#print Test_User_DB1["MK"].advance_x_months_payments(2)

print Test_User_DB1["jo11"].wallet["0715"].get_card_info()
print Test_User_DB1["mk94"].wallet["0714"].get_card_financial_report()
 
print
print "testing_user_Class"  
user2 = user("joelle c", "jo11", "jk1")
user2.add_card_to_wallet()
user2.wallet["0715"].get_card_info()
print user2.wallet["0715"].get_card_financial_report()
print user2.wallet
Test_User_DB1[user2.username] = user2

user1 = user(raw_input("Enter your name: "), raw_input("Enter your username: "), raw_input("Enter your password: "))
print user1
print user1.getLastName()
user1.add_card_to_wallet()
print user1.wallet
print user1.wallet["0714"].get_card_info()
print user1.wallet["0714"].get_card_financial_report()
Test_User_DB1[user1.username] = user1

try:
    with open(fname, 'w') as fout:
        pickle.dump(Test_User_DB1, fout)
        print "printed to file "+ fname
except IOError, e:
    print "Error writing file: " + str(e)


