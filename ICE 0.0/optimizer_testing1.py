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
import User_DB_Class

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
print

usermk.apply_purchase_user_rewards(fuel_purchase)

raw_input()
