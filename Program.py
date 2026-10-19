from Phone import *
from Contact import *

##this is the function that prints list of contact in phone book
def con_list(book):
    i=1
    
    ##get every element
    for e in book.list :
        print("{}) {}".format(i, e.__dict__))
        i+=1

## this function add contact to phone book
def add(book):
    ## get input from the user
    name            = str (input("Name: "))
    surname         = str (input("Surname: "))
    birthday        = str (input("Birthday: "))
    phone_contacts  = [str(x) for x in input("Phone numbers: ").split()]

    ##initializes the variables
    c               = contact(name, surname, birthday, phone_contacts)
    
    ##get the contact and add it
    book.add_contact(c)
    book.save()

## delete contact if exist such a contact
def delete(book):
    ##print all the contacts in the json file
    con_list(book)
    print()

    ##get name and surname as inputs and than split to 2 strings
    ls = [str(x) for x in input("Enter name and surname: ").split()]

    ##call remove_contact method with 2 parameters
    book.remove_contact(ls[0], ls[1])

    ##save the changes in json file
    book.save()

    print("Deleted successfully!\n")

## make the program better visible for the user
def space():
    input("Press enter to continue!")
    print("\n"*100)

## here is the combination of all function as an entire program
def program():
    ##initialize
    book = phonebooks()
    
    ##print 4 options
    while True :
        print("1) List of contacts.")
        print("2) Add contact.")
        print("3) Remove contact.")
        print("4) Exit.")

        ##get the input from user
        x = int(input("Enter a number: "))

        ##invalid input
        while x>4 or x<1 :
            ##get input again
            x = int(input("Enter again a number given above: "))

        ##call specific method

        ##if user chooses 1, print list of contacts
        if x==1 :
            con_list(book)

        ##if user chooses 2, add contact
        if x==2 :
            add(book)

        ##if user chooses 3, delete contact
        if x==3 :
            delete(book)
        
        ##if user chooses 4, exit the program
        if x==4 :
            break
        
        ##print space
        space()