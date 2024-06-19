import datetime
import Display
import random

#current date and time
date_time = datetime.datetime.now()
cdate_ctime = date_time.strftime("%m/%d/%Y")

#function to update the equipment_data.txt file when returning equipment
def updateequipmentfile(equipments):
    with open("equipment_data.txt", "w") as updatefile:
        for equipmentid, info in equipments.items():
            updatefile.write(f"{info['Name']}, {info['Brand']}, {info['Price']}, {info['Quantity']}\n")

#function for the customer to input their details which then create receipt according to their name
def customer():
    global Fname
    global match
    match = False
    print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                   !!CUSTOMER RETURN RECEIPT DETAILS!!")
    print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    while not match:
        print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
        Fname = input("                                        Enter the customer first name: ") .strip()
        if Fname == "":
            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Please try again by enter valid name of the customer!!")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        elif Fname.isalpha():
            numreturn = random.choice(range(1, 500))
            with open(f"{Fname}_Return_Receipt.txt", "w") as returnreceiptfile:
                returnreceiptfile.write(f"""\n\t\t\t\t\t\t\t\t!-!-!-!-!-!-!-!-!-!-*RETURN RECEIPT*-!-!-!-!-!-!-!-!-!-!""")
                returnreceiptfile.write(f"""\n\t\t\t\t\t\t\t\t*********************Sea Side Rental Shop***************""")
                returnreceiptfile.write(f"""\n\t\t\t\t\t\t\t\t!-!-!-!-!-!-!-!-!-!-*RETURN RECEIPT*-!-!-!-!-!-!-!-!-!-!\n""")
                returnreceiptfile.write(f"\n\t\t\t\tReturn No: {numreturn}\n")
                returnreceiptfile.write(f"\n\t\t\t\tFirst Name: {Fname}\n")
                returnreceiptfile.write("\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\t")
                returnreceiptfile.write("{:<31} {:<17} {:<10} {:<10} {:} {:}".format("\t\t\t\tName","Brand", "Price", "Quantity", "Total","Fine"))
                returnreceiptfile.write("\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\t")
                match = True
        else:
            print("\n\n                               !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                               !!Please try again by entering valid name of the customer without space!! ")
            print("                               !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return match
         
#function for customer to return equipment that they rented
def returningequipment(match):
    box = Display.dataequipment()
    Display.allequipment(box)
    print("\n") 
    global totalamount
    totalamount= 0
    returned=False
    print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
    daysreturn = int(input("                                        Enter the number of return day: "))
    while match:
        try:
            print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
            equipmentid= int(input("                                        Enter the equipmentid you want to return: "))
            if equipmentid in box.keys():
                returncontinue = True
                while returncontinue:
                    try:
                        print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
                        quantity= int(input("                                        Enter the quanitity you want to return: "))
                        if quantity < 0:
                            print("\n\n                                 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("                                   !!Please try again by entering the positive quantity integer!!")
                            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        elif box[equipmentid]["Quantity"] >= quantity:
                            returncontinue=False
                            returned=True
                            price = int(box[equipmentid]['Price'].replace("$", "").replace(",", ""))
                            price1 = price * quantity
                            totalamount += price1
                            fine = calculatingfine(daysreturn)
                            with open(f"{Fname}_Return_Receipt.txt", "a+") as quantityreturnfile:
                                quantityreturnfile.write("\t\t\t\t{:<31} {:<17} {:<10} {:<10} {:} {:}".format(box[equipmentid]['Name'],
                                                                                       box[equipmentid]['Brand'], box[equipmentid]['Price'], quantity, price1,fine))
                                quantityreturnfile.write("\n\t")
                               
                            box[equipmentid]["Quantity"] += quantity
                            updateequipmentfile(box)
                            returncontinue = False
                        else:
                            returncontinue = False  
                    except ValueError:
                        print("\n\n                                 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("                                   !!Please try again by entering the positive quantity integer!!")
                        print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("                                   !!Please try again by entering valid equipment id!!")
                print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        except ValueError:
            print("\n\n                                 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Please try again by entering the positive equipment id integer!!")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if returned:
            while True:
                print("\n\n                           !!!!!!!!!!                                                            !!!!!!!!!!")
                returnml=input("                                      Do you want to return more products? (yes/ no):    ").lower()
                if returnml == "yes":
                    break
                elif returnml == "no":
                    match = False
                    returncontinue= False
                    break
                else:
                    print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("                                   !!Please try again by entering 'yes' or 'no'!!")
                    print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#function for calculating the price for each equipment quantity with fine charge
def total():
    global totalamount
    fine=totalamount+10
    with open(f"{Fname}_Return_Receipt.txt", "a+") as customerfile:
        customerfile.write( """\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n""")
        customerfile.write(f"\t\t\t\t\t\t\t\tTotal Amount: ${totalamount}\n")
        customerfile.write(f"\t\t\t\t\t\t\t\tFine: $10\n")
        customerfile.write(f"\t\t\t\t\t\t\t\tTotal Amount including fine: ${totalamount + fine}")
        customerfile.write("""\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n""")
        customerfile.write("""\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
        customerfile.write("""\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Thank you for returning our equipment!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
    print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                   !!Thank you for returning our equipment!!")
    print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#function to calculate fine if the return day is greater than 5  
def calculatingfine(daysreturn):
    fine = 0
    if daysreturn > 5:
        dayslate = daysreturn - 5
        fine = dayslate * 10 
    return fine

def returnprocess():
    match=customer()
    if match:
        returningequipment(Fname)
        total()
    

if __name__ == "__main__":
    returnprocess()