import defines
import utilities

#UI Utilities
def CreateCostumerPrompt(prompt, _force_capital = True):
    print(prompt, end='')
    temp = input()
    if(_force_capital):
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
    #print("value:", _value)
    print("Have your change: \n")
    #temp = int(_value * 100)
    temp = _value
    availability_change = []

    for i in range(0, len(bills)):
        availability_change.append(bills[i].available)
    #print("bills: ", len(bills))
    for i in range(0, len(bills)):
        #print(bills[i].value, '\n')
        while availability_change[i] > 0 and bills[i].value <= temp:
            #print(temp)
            temp -= int(bills[i].value)
            availability_change[i] -= 1
    print('\n')
    #print(temp)
    if(temp != 0):
            return False
    else:
        for j in range(0, len(bills)):
            if availability_change[j] < bills[j].available:
                prints = bills[j].available - availability_change[j]
                for count in range(0, prints):
                    bills[j].print_bill()
        for z in range(0, len(bills)):
            bills[z].available = availability_change[z]
    return True

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
    bill_scii = ""

    def define_bill(self, _display_name,_value, _available, _scii = ""):
        self.display_name = _display_name
        self.value = _value
        self.available = _available
        if _scii != "":
            self.bill_scii = _scii
        else:
            self.bill_scii = _display_name
    def print_bill(self):
        if self.bill_scii != "":
            print(self.bill_scii)
        else:
            print(self.display_name)

bills = []
for i in range(0, 13):
    bills.append(Bill())
#Moedas
bills[12].define_bill("Um Centavo", 0.01 * 100, 10)
bills[11].define_bill("Cinco Centavos", 0.05 * 100, 10)
bills[10].define_bill("Dez Centavos", 0.1 * 100, 10)
bills[9].define_bill("Vinte e Cinco Centavos", 0.25 * 100, 10)
bills[8].define_bill("Cinquenta Centavos", 0.5 * 100, 10)
bills[7].define_bill("Um Real", 1 * 100, 10)
#Notas
bills[6].define_bill("Dois Reais", 2 * 100, 10)
bills[5].define_bill("Cinco Reais", 5 * 100, 10)
bills[4].define_bill("Dez Reais", 10 * 100, 10)
bills[3].define_bill("Vinte Reais", 20 * 100, 10)
bills[2].define_bill("Cinquenta Reais", 50 * 100, 10)
bills[1].define_bill("Cem Reais", 100 * 100, 10)
bills[0].define_bill("Duzentos Reais", 200 * 100, 10)

def deposit_bill(_value, _quantity):
    for i in range(0, len(bills)):
        if bills[i].value == _value * 100:
            bills[i].available += _quantity

def withdraw_bill(_value, _quantity):
    for i in range(0, len(bills)):
        if bills[i].value == _value * 100:
            if bills[i].available > _quantity:
                bills[i].available -= _quantity
                return True
    return False
                


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
        print("Use x in the product name to delete it, leave parameters empty to not change them.")
        name = CreateCostumerPrompt("Enter Product Name: ", False)
        if name != "":
            if name != "x":
                self.name = name
            else:
                if catalogue.__contains__(self):
                    catalogue.remove(self)
                return False
        price = CreateCostumerPrompt("Enter Product Price: ")
        if price != "" and price.isdigit:
            self.price = float(price)
        
        stock = CreateCostumerPrompt("Enter Product Stock: ")
        if stock != "" and price.isdigit:
            self.stock = int(stock)
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
            buying_target = int(defines.input_buffer) - 1
            ref = catalogue[buying_target]
            print("Now Buying", ref.name)
            print("The Product Price is", ref.price)
            print("What quantity is gonna be deposited?")
            deposited_amount = int(int(CreateCostumerPrompt('>')) * 100)
            valid = False
            #Check for valid purchase
            if deposited_amount >= ref.price and catalogue[buying_target].stock > 0:
                print("Congratulations on buying", ref.name,'!')
                dep = int(int(deposited_amount))
                #print(ref.price)
                pr = int(float(ref.price) * 100)
                #print(dep, pr)
                valid = print_change(dep - pr)
            else:
                print('\n' * 5)
                print("I am sorry but that is not enough to afford our product or we are out of stock! perhaps try something cheaper?")
                continue

            if valid:
                print("Thanks for buying with us. \nEnjoy!")
                catalogue[buying_target].stock -= 1
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
                    print("d <value> <amount> to deposit bills")
                    print("w <value> <amount> to withdraw bills")
                    print("v to view the bills available.")
                    CreateCostumerPrompt(">")
                    if defines.input_buffer == 'x':
                        break
                    if defines.input_buffer == 'v':
                        print('=' * 20)
                        for i in range(0, len(bills)):
                            print(bills[i].display_name, bills[i].available, "Available")
                        print('=' * 20)
                        continue
                    split = defines.input_buffer.split(' ')
                    allowed = False
                    if defines.input_buffer[0] == 'w':
                        allowed = withdraw_bill(float(split[1]), int(split[2]))
                        utilities.clear_console()
                    elif defines.input_buffer[0] == 'd':
                        deposit_bill(float(split[1]), int(split[2]))
                        allowed = True
                        utilities.clear_console()
                    if allowed:
                        print("The values were sucesfully changed!")
                    else:
                        print("You are not allowed to do that!")


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

