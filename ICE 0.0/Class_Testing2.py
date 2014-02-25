import datetime, os, pickle
import User_Class 
import User_DB_Class
from Credit_Card_Class_w_Rwrds import credit_card
from Main_Menu import Menu


print "testing_pickled_file"
fname = 'ICE_User_DBtest.pkl'
ICE_User_DBtest = {}

try:
    ICE_User_DBtest = pickle.load( open( fname, "rb" ) )
    print "file "+ fname + " loaded"
except IOError, e:
    print "Error writing file: " + str(e)

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

