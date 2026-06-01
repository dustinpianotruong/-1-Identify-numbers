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
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    
    except ValueError:
        print("Invalid input! Please enter a valid number or 'Stop' to exit.")

# Display results
print("\n--- Results ---")
if numbers:
    print(f"All numbers entered: {numbers}")
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Total numbers: {len(numbers)}")
else:
    print("No numbers were entered.")
