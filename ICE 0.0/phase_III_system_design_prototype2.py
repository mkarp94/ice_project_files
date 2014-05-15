from User_Class import user
from Purchase_Class import purchase
from Credit_Card_Class_w_Rwrds import credit_card
import datetime, os, pickle
from User_DB_Class import user_db

print "ice_prototype testing"
#print "testing_pickled_file"
#fname = 'ICE_User_DBtest.pkl'
ICE_User_DB = user_db()
ICE_User_DB.Main_Menu()