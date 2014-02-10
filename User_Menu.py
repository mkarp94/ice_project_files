#!/usr/bin/env python
# -*- coding: utf-8 -*-
#eco - engine for credit optimization 

import os, pickle
from add_card import AddCard
import credit_card_class
import User_Accounts_class

#import lookup_dvds
#import modify_dvd
#import delete_dvd
#import csvreport_dvd


#MAIN MENU
def user_menu():
    os.system('cls')
    print """
    ========================================
    ICE – INTELLIGENT CARD ENGINE
    ========================================
    1 - Add a credit card to your account
    2 - Display Credit Cards
    3 - Display Credit Usage Report
    4 - Delete a credit card from your account
    5 - Export listing to CSV
    6 - Exit
    ================================
    """
    choice = raw_input("Enter a choice and press enter:  ")

    while choice != "6":    
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\n'*100
            AddCard()
            choice = user_menu()
        elif choice == "2":
            os.system('cls')
            lookup_card.LookupCard()
            choice = user_menu()
        elif choice == "3":
            os.system('cls')
            modify_card.ModifyCard()
            choice = user_menu()
        elif choice == "4":
            delete_card.DeleteCard()
            choice = user_menu()
        elif choice == "5":
            csvreport_reports.Write_Card_to_CSV()
            choice = user_menu()
    
        CardIQ_User_DB = {}
        fname = 'CardIQ_User_DB.pkl'
    
        try:
            with open(fname, 'w') as fout:
                pickle.dump(CardIQ_User_DB, fout)
                print "printed to file "+ fname
        except IOError, e:
            print "Error writing file: " + str(e)
    '''        
        try:
            User_Accounts = pickle.load( open( fname, "rb" ) )
            print "file "+ fname + " loaded"
        except IOError, e:
            print "Error writing file: " + str(e)
    '''