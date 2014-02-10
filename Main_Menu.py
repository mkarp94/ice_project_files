#!/usr/bin/env python
# -*- coding: utf-8 -*-
#eco - engine for credit optimization 

import os, pickle
from User_Menu import user_menu
import credit_card_class
import User_Accounts_class

#import lookup_dvds
#import modify_dvd
#import delete_dvd
#import csvreport_dvd


#MAIN MENU
def Menu():
    '''
    CardIQ_User_DB = {}
    fname = 'CardIQ_User_DB.pkl'   
    try:
        CardIQ_User_DB = pickle.load( open( fname, "rb" ) )
        print "file "+ fname + " loaded"
    except IOError, e:
        print "Error writing file: " + str(e)
    '''
    os.system('cls')
    
    print """
    ========================================
    ICE – INTELLIGENT CARD ENGINE
    ========================================
    1 - Sign In                                             
    2 - Create Account
    3 - Help
    4 - Exit
    ================================
    """
    choice = None
    choice = raw_input("Enter a choice and press enter:  ")
    
    while None == choice or choice != "6":    
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\n'*100 #for now while non-windows executable
            #num_attempts = 0
            #while num_attempts < 6:
            #if username == username and password == password:
            user_menu()
            #else: num_attempt += 1
            #print"locked_out, goodbye"
            choice = Menu() 
        elif choice == "2":
            os.system('cls')
            lookup_dvds.LookupDVD()
            choice = Menu()
        elif choice == "3":
            os.system('cls')
            modify_dvd.ModifyDVD()
            choice = Menu()
        elif choice == "4":
            delete_dvd.DeleteDVD()
            choice = Menu()
        elif choice == "5":
            csvreport_dvd.WriteCSV()
            choice = Menu()
        elif choice == "6":
            print "Thanks for using your Intellegent Credit Engine"
            break
            
    '''
        CardIQ_User_DB = {}
        fname = 'CardIQ_User_DB.pkl'
        
	try:
            with open(fname, 'w') as fout:
                pickle.dump(CardIQ_User_DB, fout)
                print "printed to file "+ fname
        except IOError, e:
            print "Error writing file: " + str(e)
        '''
Menu()