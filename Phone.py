import json
import os
from Contact import *

##This the class that contain all contatct
class phonebooks:

   ##constructor
   def __init__(self):
       ##need for list of contact
       self.list = []

       ## see if database is empty or not
       if os.stat("data.txt").st_size != 0:

           ##access the database file for reading
           with open('data.txt') as json_file:
               ##use json library to have better data saving and accessing
               data = json.load(json_file)

          ## from file data are stored in class
           for e in data["list"]:
               con = contact(e["name"], e["surname"], e["birthday"], e["phone_numbers"])
               self.list.append(con)

   ## add contact function
   def add_contact(self, contact):
     ## we need to search name and surname because dublicates are not allowed
       i = True
       ##search if the contact exists using for loop
       for e in self.list:
           if contact.name == e.name and contact.surname == contact.surname:
               ##contact found, end the function
               i = False
               break

       ##contact not found
       if i:
           ## add the contact using .append() function
           self.list.append(contact)
           print("Added successfully!\n")

   ## remove a contact by entering name and surname
   def remove_contact(self, name, surname):
       ##search if name and surname can be found in the class
       for element in self.list :
          if (element.name == name and element.surname == surname):
               ##remove the contact
               self.list.remove(element)
               
   ## dictionary representation of the class needed to store data in file
   def dictionary(self):
       ls = []
       dict= {}
       i=1
       
       ##take each element and .append() , store at the end of the file
       for e in self.list:
           ls.append(e.__dict__)
           
       dict["list"] = ls
       return dict

   ## just store data in file unsing json library
   def save(self):
       with open('data.txt', 'w') as outfile:
           json.dump(self.dictionary(), outfile, indent=2)