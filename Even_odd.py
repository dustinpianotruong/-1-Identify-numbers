#Instruction: Write a simple program asking for a number and identify whether the number is even or odd. Keep the record of those numbers.
print("Type a number")
#Ask user to type in number
num = int(input())
#Checking whether even or odd
if num % 2 == 0:
  print("Even")
else:
  print("Odd")
#Store the number
