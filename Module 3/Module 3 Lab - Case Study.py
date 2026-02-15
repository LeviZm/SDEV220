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
    def __init__(self, year, make, model, doors, roof, type="car"):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle Type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nDoors: {self.doors}\nRoof Type: {self.roof}"

    def display_info(self):
        print(f"Vehicle Type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Roof Type: {self.roof}")

# Main function to execute the program

def main():
    print("Vehicle Information:\n")

    # Collect user intput for automobile attributes
    # Could also collect user input for the vehicle type here. 
    # I set the default to car in the constructor because the assignment states the v_type should be "car".
    
    # type = input("Enter the vehicle type: ")
    year = input("Enter the year of the automobile: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")

    # Validate user input for number of doors
    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        else:
            print("Invalid input. Please enter 2 or 4.")

    # Validate user input for roof type
    while True:
        roof = input("Enter the roof type (solid or sun roof): ")
        if roof.lower() in ["solid", "sun roof"]:
            break
        else:
            print("Invalid input. Please enter 'solid' or 'sun roof'.")
    
    print("\n")  # Add a newline for better readability before displaying information

# Create an instance of the Automobile class with user input
    car = Automobile(year, make, model, doors, roof)

# Display the automobile information
    car.display_info()

# Alternatively, you can use the __str__ method to display the information in a formatted string
    print("\nAutomobile Information:")
    print(car)

# Call the main function to execute the program.

if __name__ == "__main__":
    main()