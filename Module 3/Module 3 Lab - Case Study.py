''' Module 3 Lab - Case Study: Functions and Classes
    Levi Melangton
    Module 3 Lab - Case Study.py
    This program defines a Vehicle superclass and an Automobile class. The Automobile class inherits from the Vehicle class and includes
    additional attributes specific to automobiles. The program collects user input to create an instance of the Automobile class and
    displays the information about the automobile.

    v_type = vehicle type
    year = year of the automobile
    make = make of the automobile
    model = model of the automobile
    doors = number of doors (2 or 4)
    roof = roof type (solid or sun roof)
'''

class Vehicle:
    def __init__(self,type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle Type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Roof Type: {self.roof}")

# Create an instance of the Automobile class with user input
def main():
    print("Vehicle Information:\n")
    v_type = "car"

    # Collect user intput for automobile attributes
    year = input("Enter the year of the automobile: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")

    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        else:
            print("Invalid input. Please enter 2 or 4.")

    while True:
        roof = input("Enter the roof type (solid or sun roof): ")
        if roof.lower() in ["solid", "sun roof"]:
            break
        else:
            print("Invalid input. Please enter 'solid' or 'sun roof'.")
    
    print("\n")  # Add a newline for better readability before displaying information

# Create an instance of the Automobile class with user input
    car = Automobile(v_type, year, make, model, doors, roof)

# Display the automobile information
    car.display_info()

if __name__ == "__main__":
    main()