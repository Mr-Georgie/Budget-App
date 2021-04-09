# create the class
class Budget:
    
    # initialize its attributes
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    # This method handles deposit within a category
    def deposit(self, amount):
        
        # add the credit to the category balance
        self.balance = amount
        feedback = "********Deposit Result********\n"
        feedback += f"Your new balance is ${self.balance} in {self.name} budget\n"
        feedback += "_________________________________"
        return feedback
        
    # this method handles withdrawal within a category    
    def withdraw(self, amount):
        
        # check if the balance is low
        if self.balance < amount:
            feedback = "********Withdrawal Result********\n"
            feedback += "Insufficient Funds\n"
            feedback += "_________________________________"
            return feedback
        else:
            # subtract the debit from the category balance
            self.balance = self.balance - amount
            
            feedback = "********Withdrawal Result********\n"
            feedback += "Transaction was successful\n"
            # feedback += f"Your new balance is ${self.balance} in {self.name} budget"
            feedback += "_________________________________"
            
            return feedback
        
    # this method returns the balance of a category
    def get_balance(self):
        # give a reasonable feedback to user
        feedback = "********Balance Information********\n"
        feedback += f"The balance for {self.name} is ${self.balance}\n"
        feedback += "_________________________________"
        
        return feedback
    
    # this method handles transfer across other categories only
    def transfer(self, amount, category_object):
        
        # check if the user enters a category object into itself
        if self.name == category_object.name:
            feedback = "ERROR!\n"
            feedback += "You can not transfer within the same category\n"
            feedback += "You can only deposit within a category"
            return feedback
        
        # check if the balance is low
        if self.balance < amount:
            return "Insufficient Funds"
        else:
            # transfer the money
            self.balance -= amount
            category_object.balance += amount
            
            feedback = "********Transaction Result********\n"
            feedback += "Transfer was successful\n"
            feedback += f"The balance for {self.name} is ${self.balance}\n"
            feedback += f"The balance for {category_object.name} is ${category_object.balance}\n"
            feedback += "_________________________________"
            
            return feedback 
            



# instantiating 2 objects from the budget class
food_budget = Budget("food")
clothing_budget = Budget("clothing")
entertainment_budget = Budget("entertainment")

# deposit money into budget categories
print(food_budget.deposit(2000))
print(clothing_budget.deposit(5000))
print(entertainment_budget.deposit(3000))

print(food_budget.withdraw(2500)) # this should return insufficient funds
print(clothing_budget.withdraw(1000)) # this should return transaction successful

# get balances for both categories
print(food_budget.get_balance()) 
print(clothing_budget.get_balance())

# transfer between categories
print(entertainment_budget.transfer(200, food_budget))
print(clothing_budget.transfer(1500, food_budget))
print(food_budget.transfer(200, clothing_budget))

