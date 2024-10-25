store_name_age = {}

#loop to input neccessary information
while True:
#auto retry if error occurs
    while True:
        try:
            name = str(input("Enter Your Name: "))
            age = int(input("Enter Your Age: "))
            
            store_name_age [name] = {
                "age" : age
            }
#ask to add more info
            retry = input("Retry? (y/n): ")
            break
        except ValueError:
            print ("Invalid Input")
            
#find oldest age
#print oldest