import json
import os

file_name= "students_details.json"

def create_file():
  if not os.path.exists(file_name):
    with open(file_name,"w") as file:
      json.dump([],file)

def read_data():
  with open(file_name, "r") as file:
   return json.load(file)

def save_data(students):
  with open(file_name, "w") as file:
    json.dump(students, file, indent=4)
