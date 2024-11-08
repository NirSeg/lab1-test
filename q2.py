def greet_user(name):
    message = "Hello " + name + "!"
    return name

# Get name input from the user
user_name = input("Enter your name: ")

# Call the function to greet the user
greeting = greet_user(user_name)

# Display the greeting message
print("Greeting:", user_name)