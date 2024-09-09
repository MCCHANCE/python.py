"""
creating a simple password validator
# using a data type - str.
# concept: validate a password based on basic rules (e.g length, presence of number)
"""

password = input("Enter your password: ")

if len(password) < 8:
  print("password is invalid")
  
elif not any(char.isdigit() for char in password):
  print("password must contain a number")

else:
  print("password is valid")
  
