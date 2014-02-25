#!/usr/bin/env python
# -*- coding: utf-8 -*-
#eco - engine for credit optimization 

import os, pickle
import User_Class 
import Credit_Card_Class
import User_DB_Class
from Main_Menu import Menu

#import lookup_dvds
#import modify_dvd
#import delete_dvd
#import csvreport_dvd


#MAIN MENU
def user_menu(User_Class):
    ICE_User_DBtest = {}
    fname = 'ICE_User_DB.pkl'   
    try:
        ICE_User_DBtest = pickle.load( open( fname, "rb" ) )
        print "file "+ fname + " loaded"
    except IOError, e:
        print "Error writing file: " + str(e)    

    
    os.system('cls')
    print """
    ========================================
    ICE – INTELLIGENT CARD ENGINE
    ========================================
    1 - Add a credit card to your account
    2 - Update a credit card in your account
    3 - Display Credit Cards
    4 - Display Credit Usage Report
    5 - Delete a credit card from your account
    6 - Export listing to CSV
    7 - Exit
    ================================
    """
    choice = raw_input("Enter a choice and press enter:  ")

    while choice != "7":    
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\n'*100
            User_Class.add_card_to_wallet()
            choice = self.user_menu()
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\n'*100
            User_Class.update_card_in_wallet()
            choice = self.user_menu()
        elif choice == "3":
            os.system('cls')
            modify_card.ModifyCard()
            choice = self.user_menu()
        elif choice == "4":
            delete_card.DeleteCard()
            choice = self.user_menu()
        elif choice == "5":
            csvreport_reports.Write_Card_to_CSV()
            choice = self.user_menu()
        elif choice == "7":
            try:
                with open(fname, 'w') as fout:
                    pickle.dump(ICE_User_DBtest, fout)
                    print "printed to file "+ fname
            except IOError, e:
                print "Error writing file: " + str(e)
            print "Signed Out"
        return Menu()
