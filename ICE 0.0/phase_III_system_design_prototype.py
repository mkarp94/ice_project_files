#create a user1
#create mix of credit cards: 2 pts. 1 cb, 1 none
#create a purchase to test optimizer

#create a user2
#create mix of credit cards: 1 pts. 2 cb, 1 none
#create a purchase to test optimizer

#create a user3
#create mix of credit cards: 1 pts. 2 cb, 1 none, 1 both
#create a purchase to test optimizer
from User_Class import user
from Purchase_Class import purchase
from Credit_Card_Class_w_Rwrds import credit_card
import datetime, os, pickle
from User_DB_Class import user_db

print "ice_prototype testing"
#print "testing_pickled_file"
#fname = 'ICE_User_DBtest.pkl'
ICE_User_DB = user_db()

'''
try:
    ICE_User_DBtest = pickle.load( open( fname, "rb" ) )
    print "file "+ fname + " loaded"
except IOError, e:
    print "Error writing file: " + str(e)
'''
print
print "testing_user_Class"  
user2 = user("joelle c", "jo11", "jk1")
user2.add_card_to_wallet()
user2.wallet["0715"].get_card_info()
print user2.wallet["0715"].get_card_financial_report()
print user2.wallet
ICE_User_DB[user2.username] = user2

user1 = user(raw_input("Enter your name: "), raw_input("Enter your username: "), raw_input("Enter your password: "))
print user1
print user1.getLastName()
user1.add_card_to_wallet()
print user1.wallet
print user1.wallet["0714"].get_card_info()
print user1.wallet["0714"].get_card_financial_report()
ICE_User_DB[user1.username] = user1

#print ICE_User_DBtest["MK"].get_balance()
#print ICE_User_DBtest["JK"].get_balance()
#print ICE_User_DBtest["MK"].advance_x_months_payments(2)
print ICE_User_DBtest["jo11"].wallet["0715"].get_card_info()
print ICE_User_DBtest["mkarp94"].wallet["0714"].get_card_financial_report()
print ICE_User_DBtest["mkarp94"].wallet["0714"].get_rewards_info()
print ICE_User_DBtest["mkarp94"].user_menu()
print ICE_User_DBtest["mkarp94"].wallet["0914"].get_rewards_info()


print "testing_user_Class"  
#user2 = User_Class.user("joelle c", "jo11", "jk1")
#user2.add_card_to_wallet()
#user2.wallet["0715"].get_card_info()
#print user2.wallet["0715"].get_card_financial_report()
#print user2.wallet
#ICE_User_DBtest[user2.username] = user2
#user1 = User_Class.user(raw_input("Enter your name: "), raw_input("Enter your username: "), raw_input("Enter your password: "))
#print user1
#print user1.getLastName()
#user1.add_card_to_wallet()
#print user1.wallet
#print user1.wallet["0714"].get_card_info()
#print user1.wallet["0714"].get_card_financial_report()
#ICE_User_DBtest[user1.username] = user1

try:
    with open(fname, 'w') as fout:
        pickle.dump(ICE_User_DBtest, fout)
        print "printed to file "+ fname
except IOError, e:
    print "Error writing file: " + str(e)



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
 


try:
    with open(fname, 'w') as fout:
        pickle.dump(Test_User_DB1, fout)
        print "printed to file "+ fname
except IOError, e:
    print "Error writing file: " + str(e)




usermk = user("Michael Karp", "mk94", "joelle")
#usermk.user_menu()
usermk.reward_structure_preference = "minimize interest paid"

usermk.wallet["0714"] = credit_card("American Express", "0714", "08/16", None, 
                .1655, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.05, "restaurants":.03, "groceries":.025},
                None, None, {})
usermk.wallet["0715"] = credit_card("American Express", "0714", "08/16", None, 
                .1955, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.055, "restaurants":.04, "groceries":.03},
                None, None, {})
 
usermk.wallet["0813"] = credit_card("American Express", "0714", "08/16", None, 
                .1455, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.045, "restaurants":.04, "groceries":.03},
                None, None, {})
                                               
usermk.wallet["0716"] = credit_card("American Express", "0714", "08/16", None, 
                .1555, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.065, "restaurants":.04, "groceries":.03},
                None, None, {})

fuel_purchase = purchase("gas", 3.59, 12, "shell", "shell gasoline for car")

print usermk.wallet["0714"].is_feasible_purchase(fuel_purchase)
print usermk.choose_optimal_card(fuel_purchase)

usermk.reward_structure_preference = "maximize points"
print usermk.choose_optimal_card(fuel_purchase)

raw_input()
