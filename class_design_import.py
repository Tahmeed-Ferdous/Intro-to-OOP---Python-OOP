class Python:
    year=2024
    number_of_programs=0
    def __init__(self, name, inventor, speciality):
        self.name=name
        self.inventor=inventor
        self.speciality=speciality
        Python.number_of_programs+=1

    def code(self):
        print(f"Code: {self.name}")

    def stop(self):
        print(f"Stop: {self.name}")
        
    def description(self):
        print(f"Its is an easy coding language")
