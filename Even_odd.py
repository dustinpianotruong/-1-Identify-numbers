"""
Program to check if numbers are even or odd.
Stores all entered numbers and stops when user types 'Stop'.
"""
# Initialize an empty list to store numbers
numbers = []
# Keep accepting user input until they choose to exit
while True:
    # Get user input for the number or exit command
    user_input = input("Enter a number (or type 'Stop' to exit): ")
    
    # Check if user wants to stop
    if user_input.lower() == "stop":
        # Exit the loop
        break 
    # Attempt to execute code that might cause an error
    try:
        # Convert input to integer
        number = int(user_input)
        # Add the number to the list
        numbers.append(number)
        
        # Determine if even or odd
        if number % 2 == 0:
            # Print message using f-string (Formatted string to insert variable values into text using curly brackets)
            print(f"{number} is even")
        #If the if statement condition is not met
        else:
            # Print message using f-string
            print(f"{number} is odd")
    # Handle the ValueError exception when input can't be converted to an integer
    except ValueError:
        print("Invalid input! Please enter a valid number or 'Stop' to exit.")

# Display results
print("\n--- Results ---")
if numbers:
    print(f"All numbers entered: {numbers}")
    """ Create a new list containing only even numbers from the numbers list using a list comprehension
    that filters by checking if each number is divisible by 2 """
    even_numbers = [n for n in numbers if n % 2 == 0]
    """ Create a new list containing only odd numbers from the numbers list using a list comprehension
    that filters by checking if each number isn't divisible by 2 """
    odd_numbers = [n for n in numbers if n % 2 != 0]
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Total numbers: {len(numbers)}")
else:
    print("No numbers were entered.")
