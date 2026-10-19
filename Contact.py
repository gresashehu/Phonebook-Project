## this a contact class that contain all details for a contact
class contact:

    ##constructor of the class
    def __init__(self, name, surname, birthday, phone_numbers=[]):
        self.name           = name
        self.surname        = surname
        self.birthday       = birthday
        self.phone_numbers  = phone_numbers

    ## here are all getters and setters of the class variables
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSurname(self, surname):
        self.surname = surname

    def getSurname (self):
        return self.surname

    def setBirthday(self, birthday):
        self.birthday = birthday

    ## here can add number in contact if it doesn't currently exist
    def add_number(self, number):
        ## numbers are unique, so we can not have dublicates
        ## condition to check if the number exists
        if number not in self.phone_numbers:
            ## .append() add element to the end
            self.phone_numbers.append(number)

    ## whith this funciton can remove last contact
    def remove_last_nr(self):
        ## .pop() deletes last element
        self.phone_numbers.pop()