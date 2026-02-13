# Module 3 - Code Review
# User.py

class User():
    def __init__(self, first_name, last_name, DOB, username, location, occupation, email):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.username = username
        self.location = location
        self.occupation = occupation
        self.email = email

    def describe_user(self): # This method prints a summary of the user's information
        print(f"User's name: {self.first_name} {self.last_name}")
        print(f"User's date of birth: {self.DOB}")
        print(f"User's location: {self.location}")
        print(f"User's occupation: {self.occupation}")
        print(f"User's email: {self.email}")

    def greet_user(self): # This method prints a personalized greeting to the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")


# Create instances of the User class

user1 = User("John", "Doe", "4/15/1990", "johndoe", "New York", "Software Engineer", "john.doe@example.com")
user2 = User("Jane", "Smith", "8/22/1985", "janesmith", "Los Angeles", "Graphic Designer", "jane.smith@example.com")
user3 = User("Bob", "Johnson", "12/5/1978", "bobjohnson", "Chicago", "Marketing Manager", "bob.johnson@example.com")
user4 = User("Ethan", "Hunt", "3/10/1982", "ethanhunt", "San Francisco", "Data Analyst", "ethan.hunt@example.com")
user5 = User("Alice", "Williams", "6/30/1995", "alicewilliams", "Seattle", "Product Manager", "alice.williams@example.com")

users = [user1, user2, user3, user4, user5]

for user in users:
    user.describe_user()
    print("\n") # add a newline for better readability between descriptions and greetings
    user.greet_user()
    print("\n")  # Add a newline for better readability between users