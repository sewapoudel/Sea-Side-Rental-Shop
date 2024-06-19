import tabulate

def dataequipment():
    #dictionary to store data of every equipment of the Sea Side Rental Shop
    storeequipment = {}
    with open("equipment_data.txt", "r") as rentalfile:
        for order in rentalfile:
            item =order.strip().split(", ")
            if len(item)==4:
                equipmentid= len(storeequipment) + 1
                storeequipment[equipmentid] = {
                    "Equipment ID" :equipmentid,
                    "Name": item[0],
                    "Brand": item[1],
                    "Price": item[2],
                    "Quantity": int(item[3]),
                }
        return storeequipment

def allequipment(equipment1):
    #list to hold the updated data of equipment_data.txt file with Equipment ID
    equipmentdata = []
    for equipmentid, item in equipment1.items():
        equipmentdata.append([equipmentid, item['Name'], item['Brand'], item['Price'], item['Quantity']])
    equipmenttable = tabulate.tabulate(equipmentdata, headers=["Equipment ID", "Name","Brand","Price","Quantity"], tablefmt="grid")
    print(equipmenttable)
    
