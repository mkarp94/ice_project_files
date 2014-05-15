# -*- coding: utf-8 -*-
###
### User_DB.py
### DataBase to store user account information
### user_db = {dictionary of users}
### user_db = {username1: User_class1,
###        username2: User_class2}
### user_db key = username (string of username)
### user_db value = User_Class (class object representing a user)
###

import os, pickle
import Credit_Card_Class_w_Rwrds 
from User_Class import user

class user_db(object):
    """
    Represents the database containing user accounts.
    """

    def __init__(self, index = {}):
        self.index = index
        
    def add_user_to_index(self, new_user = None):
        """Add keyword to the index on url."""
        if new_user == None:
            new_user = user(raw_input("Enter your first and last name seperated by a space: "), raw_input("Enter your username: "), raw_input("Enter your password: "))    
        while new_user.username in self.index.keys():
            print "user name already exists"            
            new_user.username = raw_input("Enter a different username: ")
        self.index[new_user.username] = new_user
        self.index[new_user.username].set_reward_structure_preference()
        print "user created"

    def delete_user_from_index(self, username):
        if username in self.index.keys():
            self.index[username] = None
    
    def Main_Menu(self):  
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
                username = raw_input("Enter a username and press enter:  ")
                password = raw_input("Enter your password and press enter:  ")
                if username not in self.index.keys():
                    print "username doesn't exist, choose option 2 - Create Account from Main Menu"
                    return self.Main_Menu()
                else: 
                    while num_attempts < 6:
                        if password == self.index[username].password:
                            self.index[username].user_menu()
                            break
                        else: 
                            num_attempts += 1
                            print"locked_out, goodbye"
                #choice = Menu() 
            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                new_user = user(raw_input("Enter your first and last name seperated by a space: "), raw_input("Enter your username: "), raw_input("Enter your password: "))    
                while new_user.username in self.index.keys():
                    print "user name already exists"            
                    new_user.username = raw_input("Enter a different username: ")
                self.index[new_user.username] = new_user
                self.index[new_user.username].set_reward_structure_preference()
                self.index[new_user.username].user_menu() 
                return self.Main_Menu()
            elif choice == "3":
                os.system('cls')
                self.Help()
                #choice = Menu()
            elif choice == "4":
                break   
                
        return "Thanks for using your Intellegent Credit Engine"

    def _compute_ranks(self, d = 0.8, numloops = 10):
        """Compute page ranks for the input web index.  d is the damping factor."""
        self.ranks = {}
        pages = self.graph.get_nodes()
        npages = len(pages)
        for page in pages:
            self.ranks[page] = 1.0 / npages    

        for i in range(0, numloops):
            newranks = {}
            for page in pages:
                newrank = (1 - d) / npages
                for node in self.graph.get_inlinks(page):
                    newrank += d * (self.ranks[node] / len(self.graph.get_neighbors(node)))
                newranks[page] = newrank
            self.ranks = newranks
