def add_to_address():
    while True:
        user_continue = input("Would you like to add a name to the address book? (Y/N) ")
        if user_continue.title() == "Y":
            first = input("Please enter the First Name: ")
            last = input("Please enter the Last Name: ")
            address = input("Please enter the address: ")
            number = input("Please enter the phone number: ")
            new_person = {"First Name": first, "Last Name": last, "Address": address, "Number": number}
            address_book[first] = new_person
        else:
            break
    pass

def print_address_book(book):
    for person in book:
        print(f"First name: {book[person]['First Name']} \nLast Name: {book[person]['Last Name']} \nAddress: {book[person]['Address']} \nNumber: {book[person]['Number']}")
    pass


address_book = {}

add_to_address()
print_address_book(address_book)
