from art import logo
from replit import clear
print(logo)
def add(n1, n2):
  return n1 + n2
def substract(n1, n2):
  return n1 - n2
def divide(n1, n2):
  return n1 / n2
def multiply(n1, n2):
  return n1 * n2
def exponent(n1, n2):
  return n1**n2
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
  "**": exponent,
}
def calculator():
  num1 = float(input("Enter the first number.\n"))
  for symbols in operations:
    print(symbols)
  should_continue = True
  while should_continue:
    invalid=True
    while invalid:
      operation_symbol = input("Choose an operation.\n")
      if operation_symbol!="+" or operation_symbol!="-" or operation_symbol!="*" or operation_symbol!="/" or operation_symbol!="**":
        invalid=False
        for symbols in operations:
          print(symbols)
        print("Invalid input. Please only use the operations from above. Try again.")
    operation_symbol = input("Choose an operation.\n")
    num2 = float(input("Enter the next number.\n"))
    calculation = operations[operation_symbol]
    result = calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    another_input = input(f"Type 'yes' to continue calculating with {result}, type 'no' to start a new calculation, type 'exit' to exit out of the calculator.\n").lower()
    if another_input == "yes":
      num1 = result
    elif another_input == "no":
      should_continue = False
      clear()
      calculator()
    elif another_input == "exit":
      should_continue = False
      clear()
      print("Adios")
    else:
      should_continue = False
      print("Invalid input")
calculator()
