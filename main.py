import defines
import utilities

#UI Utilities
def CreateCostumerPrompt(prompt):
    print(prompt, end='')
    temp = input()
    temp = temp.lower()
    temp = temp.strip()
    defines.input_buffer = temp
    return temp
#Catalogue Validation
def validate_choice(_choice):
    if not _choice.isdigit(): return False
    if int(_choice) > len(catalogue): return False
    if int(_choice) < 0: return False
    return True

#Change
def print_change(_value): #returns False if there are not enough notes.
    return False

def update_catalogue_ids():
    for i in range(0, len(catalogue)):
        catalogue[i].productId = i + 1

def print_catalogue(_catalogue):
    update_catalogue_ids()
    for i in range(0, len(_catalogue)):
        _catalogue[i].print_drink()
    print('\n')


class Bill:
    display_name = str("Buck")
    value = 10
    available = 0

    def define_bill(self, _display_name,_value, _available):
        display_name = _display_name
        value = _value
        available = _available

class Product:
    name = str("default")    
    price = 0
    stock = 0
    productId = 0
    def insert_data(self, _name, _price, _stock):
        self.name = _name
        self.price = _price
        self.stock = _stock
    def print_drink(self): 
        print('\n', self.productId, ' - ',  self.name, ' for just', self.price, '! we have', self.stock, ' unit(s) available.\n', end='')
    
    def modify_product_prompt(self):
        print("Use x in the product name to delete it, or x in the other parameters to keep them.")
        name = CreateCostumerPrompt("Enter Product Name: ")
        if name != "x":
            self.name = name
        else:
            if catalogue.__contains__(self):
                catalogue.remove(self)
            return False
        price = CreateCostumerPrompt("Enter Product Price: ")
        if price != "x" and price.isdigit:
            self.price = float(price)
        
        stock = CreateCostumerPrompt("Enter Product Stock: ")
        if price != "x" and price.isdigit:
            self.price = int(stock)
        return True

#Money Section
available_bills = []

#Catalogue Section
catalogue = []
for i in range(0, 5):
    catalogue.append(Product())
update_catalogue_ids()
catalogue[0].insert_data("Coca-Cola", 3.75, 2)
catalogue[1].insert_data("Pepsi", 3.67, 5)
catalogue[2].insert_data("Monster", 9.96, 1)
catalogue[3].insert_data("Café", 1.25, 100)
catalogue[4].insert_data("Redbull", 13.99, 2)



current_mode = 0 #0 - costumer area; 1 - admin area

#Main Execution Area
#Init
print("Loading...")
while True:
    #utilities.clear_console()
    if current_mode == 0:
        print("Welcome! take a look at our catalogue!")
        print(defines.ascii_vending_machine)
        print_catalogue(catalogue)
        CreateCostumerPrompt("Enter the ID of the Product you wish to buy\n>")

        #Check in any mode
        if defines.input_buffer == 'admin':
            current_mode = 1
            continue

        deposited_amount = 0
        #Buying logic
        if validate_choice(defines.input_buffer):
            ref = catalogue[int(defines.input_buffer) - 1]
            print("Now Buying", ref.name)
            print("The Product Price is", ref.price)
            print("What quantity is gonna be deposited?")
            deposited_amount = int(CreateCostumerPrompt('>'))

            #Check for valid purchase
            if deposited_amount >= ref.price:
                print("Congratulations on buying", ref.name,'!')
                print_change(deposited_amount)
            else:
                print('\n' * 5)
                print("I am sorry but that is not enough to afford our product! perhaps try something cheaper?")
                continue

            if valid:
                print("Thanks for buying with us. \nEnjoy!")
            else:
                print("Sorry but we are out of change notes, your purchase has been refunded.")
            print('\n')
        else:
            print('\n', defines.input_buffer, "is not a valid Product Id! please try again.")
    
    elif current_mode == 1:
        utilities.clear_console()
        print("You are now entering admin mode...")
        while defines.input_buffer != defines.admin_mode_password:
            print("Please enter the Administrator Password to Continue or use X to go back to costumer mode.")
            if CreateCostumerPrompt('>') == 'x':
                current_mode = 0
                break
        while defines.input_buffer == defines.admin_mode_password:
            print(defines.ascii_admin_area_header)
            print("\nWelcome to admin mode!\n")
            print("What would you like to modify?")
            print("1.(B)anking Actions")                
            print("2.(C)hange admin password")
            print("3.(M)odify product catalogue")
            print("4.(R)eturn")

            CreateCostumerPrompt('\n>')
            print("You can go back to the Admin index by typing x at any time.")
            if defines.input_buffer == '1' or defines.input_buffer == "b":
                while True:
                    print("\n Banking screen enabled!")
                    print("Available commands:")
                    print("d <billid> <amount> to deposit bills")
                    print("w <billid> <amount> to withdraw bills")
                    CreateCostumerPrompt(">")
                    if defines.input_buffer == 'x':
                        break
                    #elif defines.input_buffer[0] == w:

            elif defines.input_buffer == '2' or defines.input_buffer == "c":
                print('password')
                while True:
                    if defines.input_buffer == 'x':
                        break
                    else:
                        defines.admin_mode_password = CreateCostumerPrompt("Type in the new password: ")
                        print("New admin password sucesfully defined!")
                        break
            elif defines.input_buffer == '3' or defines.input_buffer == "m":
                while True:
                    selected = 0
                    print_catalogue(catalogue)
                    CreateCostumerPrompt("\n Which product would you like to modify? (use a greater number to add a new product)\n>")
                    if defines.input_buffer == "x":
                        break
                    if defines.input_buffer.isdigit:
                        selected = int(defines.input_buffer) - 1
                    else:
                        continue
                    if selected < len(catalogue):
                        print("Modying", catalogue[selected].name)
                        catalogue[selected].modify_product_prompt()
                    else:
                        selected = len(catalogue) + 1
                        print("Creating new product with Id", selected)
                        tempProd = Product()
                        valid_item = tempProd.modify_product_prompt()
                        if valid_item:
                            catalogue.append(tempProd)
                    
            elif defines.input_buffer == '4' or defines.input_buffer == "r":
                current_mode = 0 #Return
                break

