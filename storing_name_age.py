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
if store_name_age:
    oldest_person = max(store_name_age, key=lambda person: store_name_age[person]["age"])
    oldest_age = store_name_age[oldest_person]["age"]
  
# Print the result
    print(f"The oldest person is {oldest_person}, who is {oldest_age} years old.")
