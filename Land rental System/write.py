import operation
import datetime

def rent(lands_data):
    print("All available lands to rent: ")
    for land in lands_data:
        if land['status'].strip() == 'Available':
            print(f"kitta_number: {land['kitta_number']} ,city: {land['city']} ,direction: {land['direction']} , area: {land['area']} , price: {land['price']} ,status: {land['status']}")
    
    kitta = int(input("Enter the kitta number you want to rent: "))
    name = input("Enter your name: ")
    duration = int(input("Enter the duration (in months): "))
    phone = input("Enter your phone number: ")
    status = 'Land rented successfully'
    print("\nCongratulations! You rented a land.Please Check the invoice.")
    # preparing the invoice by calling the invoice function
    generate_invoice(kitta,lands_data,name,duration,phone,status)
    # passing lands-data to the change status function to change the status of the rented land to unavailable
    change_status(kitta)
    


def return_land(lands_data):
    # printing all the unavailable lands
    for land in lands_data:
        if land['status'] == 'Not Available':
            print(f"kitta number:{land['kitta_number']},City: {land['city']},direction: {land['direction']},Area: {land['area']},Price: {land['price']},Status: {land['status']}")

    # Asking the user for input to return the land
    kitta = int(input("Enter the kitta number of the land you want to return: "))
    name = input("please enter your name: ")
    duration = int(input("Please enter  the duration you rented the land for(in months): "))
    phone = input("Enter your phone number: ")
    status = 'Land returned successfully'
    print("Successfully returned the leased land.")
    
    generate_invoice(kitta,lands_data,name,duration,phone,status)
    change_status(kitta)
 

def generate_invoice(kitta,lands_data,name,duration,phone,status):
    for item in lands_data:
        price = operation.calculate_price(item['price'],duration)
        
        if item['kitta_number'] == kitta:
            data = f'name: {name}\nPhone Number: {phone}\nkitta number: {item['kitta_number']}\nCity: {item['city']}\nDirection: {item['direction']}\nArea: {item['area']}\nPrice: {price}\nStatus: {status}'
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime('%Y-%M-%d_%H-%M-%S')
            file_name = f"file_{formatted_time}.txt"

            with open(file_name,'w') as file:
                print("\n",data,"\n")#printing in the terminal
                file.write(data)
            break 

# Changing the status of the rented land
def change_status(kitta):
     with open('land.txt','r') as file:
        content = file.read().splitlines()
        landstatus = []
        
        for line in content:
            eachline = line.strip().split(',')
            if eachline[0] == str(kitta) and eachline[5] == 'Available':
                eachline[5] = 'Not Available'
            elif eachline[0] == str(kitta) and eachline[5] == 'Not Available':
                    eachline[5] = 'Available'
            landstatus.append(",".join(eachline))
            

        with open('land.txt','w') as file:
            file.write('\n'.join(landstatus))