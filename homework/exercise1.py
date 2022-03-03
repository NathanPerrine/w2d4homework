# 1) Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book
# Steps

#     Create a function that will ask user for name and addresses and stores them in a dictionary
#     Define an empty dictionary with which to work (global or local variable?)
#     Begin a loop that will continue to ask a user for information until the user "quits"
#     If the user does not quit, ask for a name and address and store the variables into variables
#     Add information to the dictionary with name as the key and address as the value
#     If the user does quit, end the loop
#     Print out the information from the dictionary in a formatted way
#     Execute/Call the function

def add_to_address():
    while True:
        user_continue = input("Would you like to add a name to the address book? (Y/N) ")
        if user_continue.title() == "Y":
            first = input("Please enter the First Name: ")
            last = input("Please enter the Last Name: ")
            address = input("Please enter the address: ")
            number = input("Please enter the phone number: ")
            new_person = {"First Name": first, "Last Name": last, "Address": address, "Number": number}

            if first in address_book.keys():
                if address_book[first]["Last Name"] == last:
                    user_continue = input("Name already exists, do you wand to override? (Y/N) ")
                    if user_continue.title() == "Y":
                        address_book[first]['Address'] = address
                        address_book[first]['Number'] = number
                    else: 
                        continue
            else:    
                address_book[first] = new_person
        else:
            break

def print_address_book(book):
    for person in book:
        print(f"""        ================
        First name: {book[person]['First Name']}
        Last Name: {book[person]['Last Name']}
        Address: {book[person]['Address']}
        Number: {book[person]['Number']}""")


address_book = {}

add_to_address()
print_address_book(address_book)
