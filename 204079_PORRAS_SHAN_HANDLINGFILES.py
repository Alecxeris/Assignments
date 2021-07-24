#Products Directory
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
#Get_product

# CODE CELL
def get_product(code):
    try:
        return(products[code])
    except:
        return("Sorry your item is not in the menu")
# PROBLEM 1
get_product("americano")

#Get_property

# CODE CELL
def get_property(code, property):
    try:
        return(products[code][property])
    except:
        return("Sorry your item is not in the menu")  
# PROBLEM 2
get_property("americano",'price')



#POS System
#Main Code

# CODE CELL
def main():
    order_data = []
    product_quantity = 0
    product_total = 0
    total_order = 0
    order_summary = dict()
    print_receipt = 0
    order_key = []
    receipt =""
    
    #System Interface
    print("Hi there! What's the order?" )
    print()
    order = ""
    order = input("Please input the product code and quantity of the item separated by a comma: ")

        #Order Input System
    try:
        while print_receipt == 0:
            #Receipt Checker
            if order == "/":
                print_receipt = 1
            #Order Taker System
            else:
                order_data = order.split(",")
                if order_data[0] not in products.keys(): #If user uses an invalid code
                    print("Sorry. You've entered an invalid code. Please try again")
                    order = input("Please input the product code and quantity of the item separated by a comma: ")
                else: 
                    product_quantity = int(order_data[1])
                    product_total = (get_property(order_data[0],"price"))*product_quantity
                    if order_data[0] in order_summary.keys(): #Checks if it's already in the summary
                        order_summary[order_data[0]][2] += product_quantity
                        order_summary[order_data[0]][3] += product_total
                        total_order += product_total
                        order = input("Please input the product code and quantity of the item separated by a comma: ")
                    else: 
                        order_summary[order_data[0]] = {1:get_property(order_data[0],"name"),2:product_quantity,3:product_total}
                        total_order += product_total
                        order = input("Please input the product code and quantity of the item separated by a comma: ")
    except:
        print("Sorry. You've entered an invalid code. Please try again")
        order = input("Please input the product code and quantity of the item separated by a comma: ")
    
    receipt = open("receipt.txt","w")
    receipt.write("==\nCODE\t\tNAME\t\tQUANTITY\t\tSUBTOTAL\n")
    receipt.close()
    for i in sorted(order_summary.keys()):
        receipt = open("receipt.txt","a")
        receipt.write(f"{i}\t\t{order_summary[i][1]}\t\t{order_summary[i][2]}\t\t{order_summary[i][3]}\n")
        receipt.close()
    receipt = open("receipt.txt","a")
    receipt.write(f"\nTotal:\t\t\t\t\t\t\t\t{total_order}\n==")
# PROBLEM 3
main()