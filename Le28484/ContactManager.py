#creating a contact list manager
#should contain name, phone and number
# Error Handling: Make sure your program handles errors like searching for a non-existing contact or deleting an already deleted contact.

#Interface
def interface():
    iNterface = input("Add contact: press 1 \nRemove contact: press 2 \nLook for contact: press 3 \nEnter number: ")
    print(iNterface)
    if iNterface == 1:
        add_contact()

        
    


#ading a contact
def add_contact():
    #name
    name = input("input a name")
    #phone number
    phone_value = None
    if len(phone_number) <= 9 and phone_number.isdigit():
        print("Valid phone number:", phone_number)
    else:
        print("Invalid phone number. Please enter a 9-digit number.")
        
    print(phone_value)
        
     
interface()