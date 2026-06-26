from file_manager import read_data, save_data





def students_registration():

  students = read_data()
  student_id = input("Enter student id: ")
  student_name = str(input("Enter student name: "))
  student_address = str(input("Enter student address: "))
  print("Enter the qualifications")
  qualifications=[]
  while True:
    qualification = input("Enter your qualification: ")
    year=input("Please mention passing year: ")
    qualifications.append({
      "qualification":qualification,
      "passing year":year
    })

    exit=input("more qualifications Y/N: ")
    if exit.lower()=="n":
      break


  student = {
    "student_id": student_id,
    "student_name":student_name,
    "student_address":student_address,
    "qualifications":qualifications,
  }


  students.append(student)
  save_data(students)
  print("Student data saved successfuylly!")
  print("---------------------------------")
 
  

def update_student():
  
  students=read_data()
  student=input("Please enter student name for updating: ")



  for s in students:
    if s["student_name"].lower() == student.lower():
      print(f"The student with given name: {s["student_name"]}")
      for qualification in s:
        print(f"The previous qualifications: {s["qualifications"]}")
        break
        
      while True:
         new = input("Enter new qualification: ")
         year = input("Please mention passing year: ")
         s["qualifications"].append({
         "qualification":new,
         "Passing year":year
        })
         exit=input("more qualifications Y/N: ")
         if exit.lower()=="n":
          break
      break

      print("Your new qualifications updated successfully!")
    else:
      print("No student found")
      break
  save_data(students)
  




 
def students_details():
  print("--------stuents' Details--------")
  students=read_data()
  for student in students:
    print(student)
    print("-----------------")



def search_qualifications():
  students = read_data()
  query=input("Enter qualification to see all students: ")

  for student in students:
    for q in student["qualifications"]:
      if query.lower()==q["qualification"].lower():
       print(f"Student name: {student["student_name"]}")
  print("Above students have same qualification!")     
       
search_qualifications()