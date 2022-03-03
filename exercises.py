# Given the list address_book, create a function that accepts a name (first or last or both) and returns the phone number of that name in the address_book. If the name is not in address_book, return -1.

# Ex. 1
# name = 'Hank'
# Expected Output: '(555) 555-1234'

# Ex. 2
# name = 'Tevin'
# Expected Output: '(333) 333-3245'

# Ex. 3
# name = 'Brian'
# Expected Output: -1

def name_number(book, *name):
    for first, last, address, number in book:
        # print(first, last, address, number)
        for names in name:
            if first == names or last == names:
                return number
    return -1

            

address_book = [
    ('Hank', 'Mardukas', '123 Real Street', '(555) 555-1234'),
    ('Peter', 'Klaven', '321 Fake Street', '(555) 555-4321'),
    ('Sydney', 'Fife', '555 Santa Monica Drive', '(222) 222-6789'),
    ('Tevin', 'Downey', '100 Rodeo Blvd', '(333) 333-3245')
]

# print(name_number(address_book, "Mardukas"))
# print(name_number(address_book, "Peter"))


# In-Class Exercise #1 - Print a formatted statement from the dictionary below 
# The output should be 'My favorite car is a 2018 Chevrolet Silverado'
truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}

# print(f"My favorite car is a {truck['year']} {truck['make']} {truck['model']}")


# In-Class Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format() 
# Output should be:
# Max has blue eyes
# Lilly has brown eyes
# Barney has blue eyes
# etc. 

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}

def eye_color(person):
    for k, v in person.items():
        print("{} has {} eyes.".format(k, v))

eye_color(people)
