#!/usr/bin/env python
# -*- coding: utf-8 -*-
#eco - engine for credit optimization 
import os, pickle
import Credit_Card_Class_w_Rwrds 
import User_DB_Class
import User_Class
#from Class_Testing2 import ICE_User_DBtest
#import lookup_dvds
#import modify_dvd
#import delete_dvd
#import csvreport_dvd


#MAIN MENU
def Menu():
    
    ICE_User_DBtest = {}
    fname = 'ICE_User_DBtest.pkl'   
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
    1 - Sign In                                             
    2 - Create Account
    3 - Help
    4 - Exit
    ================================
    """
    choice = None
    choice = raw_input("Enter a choice and press enter:  ")
    
    while None == choice or choice != "4":    
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\n'*100 #for now while non-windows executable
            num_attempts = 0
            while num_attempts < 6:
                username = raw_input("Enter a username and press enter:  ")
                password = raw_input("Enter your password and press enter:  ")
                if username not in ICE_User_DBtest.keys():
                    print "username doesn't exist, choose option 2 - Create Account from Main Menu"
                else: 
                    if password == ICE_User_DBtest[username].password:
                        ICE_User_DBtest[username].user_menu()
                        break

                    else: 
                        num_attempts += 1
                        print"locked_out, goodbye"
            #choice = Menu() 
        elif choice == "2":
            os.system('cls')
            lookup_dvds.LookupDVD()
            #choice = Menu()
        elif choice == "3":
            os.system('cls')
            modify_dvd.ModifyDVD()
            #choice = Menu()
        elif choice == "4":
            break   
                 
    try:
        with open(fname, 'w') as fout:
            pickle.dump(ICE_User_DBtest, fout)
            print "printed to file "+ fname
    except IOError, e:
        print "Error writing file: " + str(e)
    
    return "Thanks for using your Intellegent Credit Engine"
        
#Menu()