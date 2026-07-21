#initializing functions
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mult(a,b):
  return a*b
def div(a,b):
  if b == 0:
    return "Division with zero is not possible"
  return a/b

#select the operation
while True:
  print("Choose the operation to be performed")
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")
  print("5.Exit the program")

#input the operation
  choice=int(input("Enter your choice:")
  if choice == 5:
             print("Exiting the program...")
             break

  if choice in 1, 2, 3, 4:
      #input numbers
      num1=float(input("Enter the first number:")
      num2=float(input("Enter the second number:")

      if choice == 1:
                 print("Result = ",add(num1,num2))
      elif choice == 2:
                  print("Result = ",sub(num1,num2))
      elif choice == 3:
                  print("Result = ",mult(num1,num2))
      elif choice == 4:
                  print("Result = ",div(num1,num2))
      else:
                  print("Please enter the valid choice(between 1 - 5)")
