from credit_card_class import Credit_Card
from user_class import user_Class
myvisa = Credit_Card("visa", "0714", "06/14", "Chase", 0.18, 10000.00, 0.03)


print myvisa.get_credit_remaining()
print myvisa.get_balance()
myvisa.update_balance(2350.25)
print myvisa.get_credit_remaining()
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



#print myvisa.time_to_clear_debt_min_payment()
myvisa2 = myvisa

print "testing_pickled_file"
import pickle
fname = 'User_DB.pkl'
'''
Test_User_DB = {"MK":myvisa, "JK":myvisa2}
#pickle.dump( User_Accounts, open( "save.p", "wb" ) )

try:
    with open(fname, 'w') as fout:
        pickle.dump(Test_User_DB, fout)
        print "printed to file "+ fname
except IOError, e:
    print "Error writing file: " + str(e)
'''   
try:
    Test_User_DB1 = pickle.load( open( fname, "rb" ) )
    print "file "+ fname + " loaded"
except IOError, e:
    print "Error writing file: " + str(e)


print Test_User_DB1["MK"].get_balance()
print Test_User_DB1["JK"].get_balance()
print Test_User_DB1["MK"].advance_x_months_payments(2)

try:
    with open(fname, 'w') as fout:
        pickle.dump(Test_User_DB1, fout)
        print "printed to file "+ fname
except IOError, e:
    print "Error writing file: " + str(e)
    

 
print
print "testing_user_Class"      
user1 = user_Class(raw_input("Enter your name: "))
print user1
print user1.getLastName()



