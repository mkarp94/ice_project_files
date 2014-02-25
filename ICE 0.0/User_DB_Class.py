###
### User_DB.py
### DataBase to store user account information
### user_db = {dictionary of users}
### user_db = {username1: User_class1,
###        username2: User_class2}
### user_db key = username (string of username)
### user_db value = User_Class (class object representing a user)
###


import User_Class


class user_db(object):
    """
    Represents the database containing user accounts.
    """

    def __init__(self, db = None):
        self.index = {}
        if None != db : self.index = db
        

    def _add_to_index(self, username):
        """Add keyword to the index on url."""
        if username in self.index.keys():
            return "user name already exists"
        else:
            #self.index[User_Class.user.username]
            pass

    def add_user(self, url, content, outlinks):
        """Add the url, content, and outlinks to the index."""
        words = content.split()
        for word in words:
            self._add_to_index(word, url)
        self.graph.add_node(url)
        for target in outlinks:
            self.graph.add_node(target)
            self.graph.add_edge(url, target)

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
