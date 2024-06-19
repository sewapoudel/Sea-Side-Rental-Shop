#importing the modules 
import tabulate
import Display
import Rent
import Return
import sys

#function to display the welcome message of the Sea Side Rental Shop
def main():
    print("                     !-!-!-!-!-!-!-!-!-!-*******************************-!-!-!-!-!-!-!-!-!-!")
    print("                     ********************Welcome to Sea Side Rental Shop********************")
    print("                     !-!-!-!-!-!-!-!-!-!-*******************************-!-!-!-!-!-!-!-!-!-!")

    while True:
        option = [
            ["1", "Display all the available equipments"],
            ["2", "Display the items for renting"],
            ["3", "Display the items for returning"],
            ["4", "Exit"]
        ]

        #Display the value stored in option variable in a table format
        optiontable = tabulate.tabulate(option, headers=["!", "Sea Side Rental Shop"], tablefmt="grid")
        print(optiontable)

        try:
            print("\n\n                           !!!!!!!!!!                                            !!!!!!!!!!")
            choice = int(input("                                        Enter the number of your  choice: "))
            if choice == 1:
                storeequipment = Display.dataequipment()
                Display.allequipment(storeequipment)
                again()
            elif choice == 2:
                Rent.rentprocess()
                again()
            elif choice == 3:
                Return.returnprocess()
                again()
            elif choice == 4:
                print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("                                   !!Thank you for reaching out to our Sea Side Rental Shop!!")
                print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                sys.exit()
            #message for user if they enter choice that are not available 
            else:
                print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("                                   !!Please try again by only entering the above option integer!!")
                print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
            #message for user if they enter other than integer value  
        except ValueError:
            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Please try again by entering the positive integer!!")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
           

#function for user to again choose other option after already choosing one of the option
def again():
    print("\n\n                           !!!!!!!!!!                                                            !!!!!!!!!!")
    while True:
        ans = input("                                        Do you want to check out other options? (yes/no):  ").lower()
        if ans == 'yes':
            return 
        elif ans == 'no':
            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Thank you for reaching out to our Sea Side Rental Shop!!")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            sys.exit()  
        else:
            print("\n\n                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("                                   !!Please try again by entering 'yes' or 'no'!!")
            print("                                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    main()
