from User_Class import user
from Purchase_Class import purchase
from Credit_Card_Class_w_Rwrds import credit_card
import datetime, os, pickle
from User_DB_Class import user_db

print "optimizer testing"
usermk = user("Michael Karp", "mk94", "joelle")
#usermk.user_menu()

usermk.reward_structure_preference = "minimize interest paid"

usermk.wallet["0214"] = credit_card("American Express", "0214", "08/15", None, 
                .1655, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.05, "restaurants":.03, "groceries":.025},
                None, None, {})
usermk.wallet["0315"] = credit_card("American Express", "0315", "08/17", None, 
                .1955, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.055, "restaurants":.04, "groceries":.03},
                None, None, {})
 
usermk.wallet["0413"] = credit_card("American Express", "0413", "08/18", None, 
                .1455, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.045, "restaurants":.04, "groceries":.03},
                None, None, {})
                                               
usermk.wallet["0516"] = credit_card("American Express", "0516", "08/19", None, 
                .1555, 10000, .05, 100, None,
                "Points", 0, .01, {"gas":.065, "restaurants":.04, "groceries":.03},
                None, None, {})

for key in usermk.wallet.keys():
    print
    print "last 4 digits: " + key
    print "interest_rate: " + str(usermk.wallet[key].annual_interest_rate)
    print
    usermk.wallet[key].get_rewards_info()
 
fuel_purchase = purchase("gas", 3.59, 12, "shell", "shell gasoline for car")

print usermk.wallet["0214"].is_feasible_purchase(fuel_purchase)
print usermk.choose_optimal_card(fuel_purchase)



usermk.reward_structure_preference = "maximize points"
print usermk.choose_optimal_card(fuel_purchase)
print

usermk.apply_purchase_user_rewards(fuel_purchase)

raw_input()



print "ice_prototype testing"
#print "testing_pickled_file"
#fname = 'ICE_User_DBtest.pkl'
ICE_User_DB = user_db()
ICE_User_DB.Main_Menu()
