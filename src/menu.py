
from students_handler import (students_registration,students_details,
                              update_student, search_qualifications
                              )

def show_menu():

  while True:
    print("1. For entering students details")
    print("2. For updating students details")
    print("3. For viewing students details")
    print("4. Fort searching student")
    print("5. DONE for quit")
    query = input("Enter your query: ")
    if query.isdigit():
      query = int(query)
      
      if query== 1:
       students_registration()
      elif query == 2:
       update_student()
      elif query == 3:
       students_details()
      elif query == 4:
       search_qualifications()
      elif query == 5:
       print("Students' details saved successfully")
      
    else:
     print("please enter valid input")


