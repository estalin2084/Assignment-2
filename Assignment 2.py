# Name: Arnold Store II.py
# Author: Estalin Peña
# Date Created: November 07, 2022
# Date Last Modified: November 09, 2022
# Purpose: To take the order of the clients, ask whether is pick up or delivery and print the receipt.





def total(): #This funcion calculates the total of price and meal quantity
    return float(order_data['MealQuantity']) * float(order_data['MealPrice'])

def subtotal(): #this function sets a list to print the subtotal
    print(float(order_data['MealPrice']) * float(order_data['MealQuantity'] - discount()))



def discount(): #this function calculates all the discounts and returns the percentages and quantiy in money.

    global percentage #this variable is set to be used globally
    global applied_disc #this variable is set to be used globally
    student_discount = .9 #this takes the .9% of the total
    global applied_student_disc #this applies the 10% to the student


    if total() < 100: #this calculates the 5% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.95
        percentage = "5%"
        applied_disc = total() *0.05 
        if order_data["Student"] == True: 
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
    
    elif total() >= 100 and total () <500: #this calculates the 10% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.90
        percentage = "10%"
        applied_disc = total() *0.10
        if order_data["Student"] == True:
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
    elif total() > 500: #this calculates the 15% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.85
        percentage = "15%"
        applied_disc = total() *0.15
        if order_data["Student"] == True:
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc

def deli_or_pickup(order_data):
    delivery = 0
    while delivery not in range(1,2):
        delivery = int(input('Please indicate if your order is pick up or delivery: 1) Delivery 2) Pick Up: '))
        if delivery == 1:
            order_data["Delivery"] = True
            if total() > 30:
                order_data["DeliveryCharge"] = 0
                print("Your order is free or delivery charge!")
            else:
                order_data["DeliveryCharge"] = 5
                print("Your order has a 5$ delivery fee")
            tips(order_data)

        elif delivery == 2:
            order_data["Delivery"] = False
            break
        else:
            print("Please write 1 or 2 only! ")
    
def tips(order_data):
    tip = 0
    while tip not in range(1,3):
        tip = int(input('Please select your tip: 1) 10% 2) 15% 3) 20%: '))
        if tip == 1:
            order_data['Tips'] = total() * 0.10
        elif tip == 2:
            order_data['Tips'] = total() * 0.15
        elif tip == 3:
            order_data['Tips'] = total() * 0.20
        else:
            print("Please only write numbers 1 to 3!")




meals_price = {
    "1" : {
        "Name" : "Poutine",
        "Price" : 10.99, },
    "2" : {
        "Name" : "French Fries",
        "Price" : 5.99,  },
    "3" : {
        "Name" : "Cheese Burger",
        "Price" : 13.99, },
    "4" : {
        "Name" : "Pumpkin Pie",
        "Price" : 7.99,  },
    "5" : {
        "Name" : "BLT Sandwich",
        "Price" : 9.99,  },
    "6" : {
        "Name" : "Chicken Salad",
        "Price" : 12.99, }
    }   

order_data = {
    'MealNumber' : "",
    'MealQuantity': "",
    'MealPrice': "",
    'Student': False,
    'Discount': "",
    'HST': "",
    'Delivery': False,
    'Instructions': "",
    'DeliveryCharge': 0.00,
    'Tips': " "}

customer_Data = {
    "FirstName" : "",
    "LastName" : "",
    "Address" : "",
    "City" : "",
    "Province" : "",
    "PostalCode" : "",
    "PhoneNumber" : ""
}


print("Calculating the Cost of Amazing Eats II!") #this is the name of the program
print(" ")
print(" ")
print("Welcome to Arnold's Amazing Eats II!") #this welcomes the client to the store
print("")

data = False
while not data:
    
    full_name = list(map(str,input("Please enter customer's fullname: ").split(" ")))
    customer_Data["FirstName"] = full_name[0].strip().capitalize() #this input takes the customer's name
    customer_Data["LastName"] = full_name[-1].strip().capitalize()
    customer_Data["Address"] = input("Please enter customer's full address: ").strip().split(" ") #this input takes the customer's street number
    customer_Data["City"] = input("Please enter customer's city: ").strip().capitalize() #this input takes the customer's city
    customer_Data["Province"] = input("Please enter customer's province: ").strip().capitalize() #this input takes the customer's province
    customer_Data["PostalCode"] = input("Please enter customer's postal code: ").strip() #this input takes the customer's postal code
    customer_Data["PhoneNumber"] = input("Please enter customer's phone number: ").strip() #this input takes the customer's phone number
     
    for key in customer_Data:
        if customer_Data[key] == "":
            print("All fields are mandatory!")
            break
        else:
            data = True

while True:
    print(" ") 
    print("What do you wish to order?")
    print(" ")

    for key in meals_price.keys():
        print(key, meals_price.get(key, {}).get("Name"), meals_price.get(key,{}).get("Price") )
            
    print(" ") #this creates a speace between the order and the menu

    order_data['MealNumber'] = input("Please select your food: " )
    while not((int(order_data['MealNumber']) >= 1) and (int(order_data['MealNumber']) <= 6)): 
                    order_data['MealNumber'] = str(input("Please select a valid option: ")).strip()

    order_data['MealQuantity'] = input("Please enter the quantity: ").strip()
    print(order_data['MealQuantity'] + " " + meals_price.get(order_data['MealNumber'], {}).get("Name"))
    confirmation = input("Please confirm your order [Yes/No]: ") #this confirms the order
    if confirmation.upper().strip() == "NO" or confirmation.upper().strip() == "N":
            continue
    elif confirmation.upper().strip() == "YES" or confirmation.upper().strip() =="Y":
            break
order_data['MealPrice'] = meals_price.get(order_data['MealNumber'], {}).get("Price")
correct_letter = False
while correct_letter == False:
    student_confirmation = input("Are you a student? [Y/N] ") #this asks if the customer is a student or no
    
    if student_confirmation.upper() == "YES" or student_confirmation.upper() == "Y": #this confirms if the customer is a student or no
         order_data['Student'] = True
         print("You have an extra ten percent discount! ")
         correct_letter = True            
    elif student_confirmation.upper() == "NO" or student_confirmation.upper() == "N":
        order_data['Student'] = False
        print("Sorry no student discount for you! ")
        correct_letter = True
    else:
        print("Please only enter Y or N")


deli_or_pickup(order_data)



print("") #this creates a space 
print("") #this creates a space
discount()

print("{0} {1}." .format(customer_Data["FirstName"], customer_Data["LastName"])) #this prints the customer first and last name before the receipt
print("{0}" .format(customer_Data["Address"])) #this print the address of the customer
print("{0}, {1}, {2}. " .format(customer_Data["City"], customer_Data["Province"], customer_Data["PostalCode"])) #this prints the city, province and postal code of the customer
print("{0}." .format(order_data['Delivery']) if order_data['Delivery'] ==True else"") #this prints the instructions in case of needing them
print("{0}." .format(customer_Data["PhoneNumber"]))
print(" ") #this creates an space between the customer info and the recepit

print("-" *75) #this creates the format of my recepit and the first line between the information in it
print("Order \t \t Quantity \t Item Price \t \t " " Total\t ")#this adds the headings of the recepit
print("-" *75) #this creates the format of my recepit and the second line 
print(("{}").format(meals_price.get(order_data['MealNumber'], {}).get("Name") + "\t" + ("{}").format(order_data["MealQuantity"]) + "\t" + "\t"+ " " + "\t" + " " + ("${:.2f}").format(order_data.get('MealPrice'))+ "\t"+ "\t" +("${:.2f}").format(total()))) #this prints the name, quantity, the price and the total
print("Discount",percentage,"\t" "\t" "\t" "\t" "\t" "\t",("${:.2f}").format(applied_disc)) #this prints the percentage discounted of the order
if order_data["Student"] == True: #if the student status is true it will print the 10% aditional discount
    print("10%" " Student savings","\t" "\t" "\t"  "\t", " ", " ", " ", ("- ${:.2f}").format(applied_student_disc))  #if the student status is true it will print the 10% aditional discount
print("\t" "\t" "\t" "\t","Subtotal" ," ", "\t", "\t", ("${:.2f}").format(discount())) #this prints the subtotal of the recepit
print("\t" "\t" "\t" "\t", "HST 13% ","\t" "\t",("${:.2f}").format(discount() * .13)) #this prints the tax
if order_data['Delivery'] == True:
    print("\t" "\t" "\t" "\t" " " "Delivery Fee",  " \t"  "\t", ("${:.2f}").format(order_data['DeliveryCharge']) )
    print("\t" "\t" "\t" "\t" " " "Tips",  " \t" "\t" "\t", ("${:.2f}").format(order_data['Tips']))
    print("\t" "\t" "\t" "\t" " " "Grand Total",  " \t"  "\t", ("${:.2f}").format(discount() * 1.13 + order_data["DeliveryCharge"] + float(order_data["Tips"]), "CAD")) #this prints the grand total of the recepit
else:
     print("\t" "\t" "\t" "\t" " " "Grand Total",  " \t"  "\t", ("${:.2f}").format(discount() * 1.13))
print("-" *75) #this creates the format of my recepit and is the last line 