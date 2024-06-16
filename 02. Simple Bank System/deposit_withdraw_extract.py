from datetime import datetime
import os
import re

MENU_TEXT = """
=============================

[d] Deposit
[w] Withdraw
[e] Extract
[q] Quit

=============================
"""
THANK_YOU_MESSAGE = """-------------------------------------
Thank you for using our bank system.
-------------------------------------
"""
SUCCESS_COLOR = "\033[92m"
SUCCESS_SYMBOL = "√"
ERROR_SYMBOL = "[x]"
ERROR_COLOR = "\033[91m"
INPUT_COLOR = "\033[93m"
RESET_COLOR = "\033[0m"
INVALID_INPUT = "Ooops! Invalid option."

WITHDRAW_LIMIT = 500
WITHDRAWS_ALLOWED = 3

# Global values
balance = 0
extract = []
num_withdraws = 0

def success_message(message):
    return print(f"{SUCCESS_COLOR}\n{SUCCESS_SYMBOL} {message}\n{RESET_COLOR}")

def error_message(message):
    return print(f"{ERROR_COLOR}\n{ERROR_SYMBOL} {message}\n{RESET_COLOR}")

def input_message(message):
    return input(f"{INPUT_COLOR}{message} {RESET_COLOR}")

def show_extract():
  # rules
  # 1. build string that list all the extract history
  extract_history = ""
  global num_withdraws
  for i, transaction in enumerate(extract):
    extract_history += f"{transaction}\n"

  # 2. Print the full extract details
  print(f"""
        
=====================================
        
Balance: R$ {balance}
Number of extracts: {num_withdraws}

=====================================

Extract History:
{extract_history}

  """)
  return continue_or_quit()

def deposit(amount):
  # Only accept positive numbers
  if amount <= 0:
    error_message("The deposit amount must be greater than zero.")
    return
  # Update the balance
  global balance
  balance += amount
  # Update the extract identifying the transaction
  current_date = datetime.now().strftime("%y/%m/%d at %H:%M")
  extract.append(f"{current_date} -> Deposited: R$ {amount:,.2f}".replace('.', ','))

  os.system('clear')
  success_message(f"Deposited: R$ {amount:,.2f}".replace('.', ','))

def withdraw(amount):
  # Only accept positive numbers
  if amount <= 0:
    error_message("The withdraw amount must be greater than zero.")
    return
  # Only allow 3 withdraws per day
  global num_withdraws
  if num_withdraws >= WITHDRAWS_ALLOWED:
    error_message("You have reached the maximum number of withdraws allowed per day.")
    return
  # Only allow withdraws up to R$ 500
  if amount > WITHDRAW_LIMIT:
    error_message(f"The maximum withdraw amount is R$ {WITHDRAW_LIMIT:,.2f}".replace('.', ','))
    return
  # Only allow withdraws if the balance is enough
  global balance
  if amount > balance:
    error_message("Insufficient funds.")
    return
  # Update the balance
  balance -= amount
  # Update the number of withdraws
  num_withdraws += 1
  # Update the extract identifying the transaction
  current_date = datetime.now().strftime("%y/%m/%d at %H:%M")
  extract.append(f"{current_date} -> Withdrew: R$ {amount:,.2f}".replace('.', ','))
  
  os.system('clear')
  success_message(f"Withdrew: R$ {amount:,.2f}".replace('.', ','))

def continue_or_quit(show_extract_option=False):
    while True:
      if show_extract_option:
          prompt = "Please press 'e' to show extract, 'c' to continue, 'q' to quit:"
      else:
          prompt = "Please press 'c' to continue or 'q' to quit:"
      
      print(THANK_YOU_MESSAGE)
      option = input_message(prompt)
      
      if option == 'c':
          os.system('clear')
          return True
      elif option == 'q':
          return False
      elif option == 'e' and show_extract_option:
          show_extract()
          return True
      else:
          error_message(INVALID_INPUT)
          
def validate_amount(amount_str):
  return bool(re.match(r'^\d+\,\d{2}$', amount_str))

def convert_to_float(amount_str):
   return float(amount_str.replace(',', '.'))

def process_transaction(action):
  while True:
    amount_str = input_message("Enter the amount (e.g., 123,45) or 'q' to quit:")
    if amount_str == 'q':
      return False
    if validate_amount(amount_str) or amount_str.isdigit():
      # Convert whole numbers to have two decimal places
      if amount_str.isdigit():
        amount_str += ',00'
      amount = convert_to_float(amount_str)
      action(amount)
      break
    else:
      error_message("Invalid format. The system only accepts a number with two decimals like 123,45 or a whole number.")
  if not continue_or_quit(show_extract_option=True):
    return False
  return True

while True:
  print(MENU_TEXT)
  option = input_message("Select an option:")

  if option == 'd':
    if not process_transaction(deposit):
      break

  elif option == 'w':
    if not process_transaction(withdraw):
      break

  elif option == 'e':
    os.system('clear')
    show_extract()

  elif option == 'q':
    print(THANK_YOU_MESSAGE)
    print("Goodbye! :)")
    break

  else:
    error_message(INVALID_INPUT)
    if not continue_or_quit():
      break
