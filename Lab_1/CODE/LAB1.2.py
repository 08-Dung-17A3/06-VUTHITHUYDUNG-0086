import json 
class JONReader:
    def __init__(self, file_path):
       self.file_path = file_path
       self.data = None
    def read_json(self):
        with open(self.file_path, 'r') as file:
           self.data = json.load(file)
    def display_data(self):
        if self.data:
           for user in self.data:
               print(f"Name: {user['name']}, Age: {user['age']},    Address:{user['address']}")
path = 'DATA//users.json'
reader = JONReader(path)
reader.read_json()
reader.display_data()