#implementation of a purchase for the purposes of evaluating categories of rewards
class purchase(object):
    def __init__(self, tag = None, unit_price = None, quantity = 0, company = None, product_description = None):
        self.tag = tag
        self.unit_price = unit_price
        self.quantity = quantity
        self.producer_company = company
        self.product_description = product_description
        self.purchase_id = None
        
    def get_tag(self):
        return self.tag
    
    def update_tag(self, updated_tag):
        self.tag = updated_tag
    
    def get_unit_price(self):
        return self.unit_price
    
    def update_unit_price(self, updated_unit_price):
        self.unit_price = updated_unit_price

    def get_quantity(self):
        return self.quantity     
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity   

    def get_producer_company(self):
        return self.producer_company     
    
    def update_producer_company(self, updated_producer_company):
        self.producer_company = updated_producer_company  

    def get_product_description (self):
        return self.product_description     
    
    def update_product_description (self, new_product_description ):
        self.product_description  = new_product_description     

    def get_purchase_price(self):
        return self.unit_price*1.*self.quantity

    def get_purchase_info(self):        
       print
       print "This product is made by " + self.producer_company
       print "It has been labeled under the rewards category of " + self.tag
       print "Its possible to get a discount wether your card's rewards are determined by the its product tag or the specific company"
       print "This purchase includes " + str(self.quantity) + " " + self.product_description
       print "The purchase price is " + str(round(self.get_purchase_price(), 2))
       print
'''
Apple_Ipad = purchase("consumer electronics", 499.00, 1, "apple", "top rated tablet computer")
print 2*Apple_Ipad.get_purchase_price()
print Apple_Ipad.get_purchase_info()
Google_Nexus = purchase(Apple_Ipad.get_tag(),Apple_Ipad.get_unit_price(),Apple_Ipad.get_quantity(),Apple_Ipad.get_producer_company(),Apple_Ipad.get_product_description())
Google_Nexus.update_producer_company("Google")
Google_Nexus.update_unit_price(399.00)
print Google_Nexus.get_purchase_info()
print Apple_Ipad.get_purchase_info()
'''