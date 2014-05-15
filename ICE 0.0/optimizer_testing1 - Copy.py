#create a user1
#create mix of credit cards: 2 pts. 1 cb, 1 none
#create a purchase to test optimizer

#create a user2
#create mix of credit cards: 1 pts. 2 cb, 1 none
#create a purchase to test optimizer

#create a user3
#create mix of credit cards: 1 pts. 2 cb, 1 none, 1 both
#create a purchase to test optimizer
from User_Class import *
from Purchase_Class import *
from Credit_Card_Class_w_Rwrds import *
import datetime, os, pickle
from User_DB_Class import *

print
print "testing_user_Class"  
user2 = user("joelle c", "jo11", "jk1")
#user2.add_card_to_wallet()
user2.wallet["0715"].get_card_info()
print user2.wallet["0715"].get_card_financial_report()
print user2.wallet
ICE_User_DB[user2.username] = user2
user2.user_menu()

usermk = user("Michael Karp", "mk94", "joelle")
usermk.user_menu()
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
print

usermk.apply_purchase_user_rewards(fuel_purchase)

raw_input()
if __name__ == '__main__':
    try:
        main()
    except BaseException as e:
        print('Error:')
        print(e)
        raise
    finally:
        raw_input('(Press <Enter> to close)')

main()
