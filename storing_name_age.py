store_name_age = {}

#loop to input neccessary information
while True:
#auto retry if error occurs
    while True:
        try:
            name = input("Enter Your Name: ")
            age = int(input("Enter Your Age: "))
            
            store_name_age [name] = {
                "age" : age
            }
#ask to add more info
            retry = input("Retry? (yes/no): ")
            break
        except :
            print ("Invalid Input")
#will retry or not  
    if retry == "no":
        break
    elif retry != "yes":
        print("Input Invalid, please enter 'yes' or 'no'.")
#find oldest age
#print oldest