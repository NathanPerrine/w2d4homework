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
    pass

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
