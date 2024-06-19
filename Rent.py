import datetime
import random
import Display

#current date and time
date_time = datetime.datetime.now()
cdate_ctime = date_time.strftime("%m/%d/%Y")

#function to update the equipment_data.txt file when renting equipment
def updateequipmentfile(equipments):
    with open("equipment_data.txt", "w") as updatefile:
        for equipmentid, info in equipments.items():
            updatefile.write(f"{info['Name']}, {info['Brand']}, {info['Price']}, {info['Quantity']}\n")

#function for the customer to input their details which then create receipt according to their name
def customer():
    global Fname
    global match
    match = False
    print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                   !!CUSTOMER RENT RECEIPT DETAILS!!")
    print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    while not match:
        print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
        Fname = input("                                        Enter the customer first name: ") .strip()
        if Fname == "":
            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Please try again by enter valid name of the customer!! ")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        elif Fname.isalpha():
            numrent = random.choice(range(1, 500))
            with open(f"{Fname}_Rent_Receipt.txt", "w") as rentreceiptfile:
                rentreceiptfile.write(f"""\n\t\t\t\t\t\t\t\t!-!-!-!-!-!-!-!-!-!-****RENT RECEIPT****-!-!-!-!-!-!-!-!-!-!""")
                rentreceiptfile.write(f"""\n\t\t\t\t\t\t\t\t********************Sea Side Rental Shop*********************""")
                rentreceiptfile.write(f"""\n\t\t\t\t\t\t\t\t!-!-!-!-!-!-!-!-!-!-****RENT RECEIPT****-!-!-!-!-!-!-!-!-!-!\n""")
                rentreceiptfile.write(f"\n\t\t\t\tRent No: {numrent}\n")
                rentreceiptfile.write(f"\n\t\t\t\tRent Date: {cdate_ctime}\n")
                rentreceiptfile.write(f"\n\t\t\t\tFirst Name: {Fname}\n")
                rentreceiptfile.write("\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\t")
                rentreceiptfile.write("{:<31} {:<17} {:<15} {:<15}{:}".format("\t\t\t\tName","Brand", "Price", "Quantity", "Total"))
                rentreceiptfile.write("\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\t")
                match = True
        else:
            print("\n\n                               !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                               !!Please try again by entering valid name of the customer without space!! ")
            print("                               !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return match

#function for customer to renting equipment according to their requirement
def rentingequipment(match):
    box = Display.dataequipment()
    Display.allequipment(box)
    print("\n")
    global totalamount
    totalamount= 0
    rented = False
    while match:
        try:
            print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
            equipmentid= int(input("                                        Enter the equipmentid you want to rent: "))
            if equipmentid in box.keys():
                rentcontinue = True
                while rentcontinue:
                    try:
                        print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
                        quantity= int(input("                                        Enter the quanitity you want to rent: "))
                        if quantity <= 0:
                            print("\n\n                                 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("                                   !!Please try again by entering the positive quantity integer!!")
                            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        elif box[equipmentid]["Quantity"] >= quantity:
                            rentcontinue = False
                            rented = True
                            price = int(box[equipmentid]['Price'].replace("$", "").replace(",", ""))
                            price1 = price * quantity
                            totalamount += price1
                            with open(f"{Fname}_Rent_Receipt.txt", "a+") as quantityreceiptfile:
                                quantityreceiptfile.write("\t\t\t\t{:<31} {:<17} {:<15} {:<15}{:}".format(box[equipmentid]['Name'],
                                                                                       box[equipmentid]['Brand'], box[equipmentid]['Price'], quantity, price1))
                                quantityreceiptfile.write("\n\t")
                            box[equipmentid]["Quantity"] -= quantity
                            updateequipmentfile(box)
                        else:
                            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("                                   !!Sorry, the quantity you want to rent is insufficient!!")
                            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            rentcontinue = False
                    except ValueError:
                        print("\n\n                                 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("                                   !!Please try again by entering the positive quantity integer!!")
                        print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("                                   !!Please try again by entering valid equipment id!!")
                print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        except ValueError:
            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Please try again by entering the positive equipment id integer!!")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if rented:
            while True:
                print("\n\n                           !!!!!!!!!!                                                            !!!!!!!!!!")
   
                rentml=input("                                      Do you want to rent more products? (yes/ no):    ").lower()
                if rentml == "yes":
                    break
                elif rentml == "no":
                    match = False
                    rentcontinue = False
                    break
                else:
                    print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("                                   !!Please try again by entering 'yes' or 'no'!!")
                    print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

#function for calculating the price for each equipment quantity with delivery charge
def total():
    global totalamount
    delivery = totalamount + 100
    with open(f"{Fname}_Rent_Receipt.txt", "a+") as customerfile:
        customerfile.write(
            """\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n""")
        customerfile.write(f"\t\t\t\t\t\t\t\tTotal Amount: ${totalamount}\n")
        customerfile.write(f"\t\t\t\t\t\t\t\tDelivery Charge: $100\n")
        customerfile.write(f"\t\t\t\t\t\t\t\tTotal Amount including Delivery charge: ${delivery}")
        customerfile.write(
            """\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n""")
        customerfile.write(
            """\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
        customerfile.write("""\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Thank you for renting our equipment!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
        customerfile.write(
            """\n\t\t\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
    print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                   !!Thank you for renting our equipment!!")
    print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def rentprocess():
    match = customer()
    if match:
        rentingequipment(match)
        total()

if __name__ == "__main__":
    rentprocess()
