#A3,Chi Heng Jeffrey Hui,CIS 345, T TH 12:00 PM
import os
import json
import logger
import time

dataStructure=[['DateTime','Name','Old Balance','Transaction','New Balance']]

# Read customers data file into accounts
with open('customers.json', 'r') as file:
    accounts = json.load(file)

# Allow 3 invalid pin entries
tries = 1
maxTries = 3

while tries <= maxTries:
    # Print bank title and menu
    print(f'{"Cactus Bank":^30}\n')
    selection = input('Enter pin or x to exit application: ').casefold()

    # determine exit, pin not found, or correct pin found
    if selection == 'x':
        break
    # Verify entered pin is a key in accounts
    elif selection not in accounts.keys():
        # clear screen - cls for windows and clear for linux or os x
        os.system('cls')
        # os.system('clear') for mac users

        print(f'Invalid pin. Attempt {tries} of {maxTries}. Please Try again')
        if tries == maxTries:
            print('Locked out!  Exiting program')

        tries += 1
    else:
        # Successful pin entry. reset tries and save pin
        tries = 1
        pin = selection

        os.system('cls')
        # os.system('clear')

        # Welcome customer
        print(f"Welcome {accounts[pin]['Name']}")
        print(f'{"Select Account": ^20}')

        # Prompt for Checking or Savings
        while True:
            try:
                selection = input('Enter C or S for (C)hecking or (S)avings: ').upper()
                if selection != 'C' and selection != 'S':
                    raise ValueError('Incorrect selection.  You must enter C or S.')
            except ValueError as ex:
                print(ex)
            else:
                os.system('cls')
                print(f'Opening {selection} Account...\n')
                break
        # End Prompt Checking or Savings

        print('Transaction instructions:')
        print(' - Withdrawal enter a negative dollar amount: -20.00.')
        print(' - Deposit enter a positive dollar amount: 10.50')
        print(f'\nBalance:  ${accounts[pin][selection]: ,.2f}')


        beforeCalculation=logger.format_money(accounts[pin][selection])

        amount = 0.00
        try:
            amount = float(input(f'Enter transaction amount: '))
        except (TypeError, ValueError):
            print('Invalid Entry - No Transaction.')
            amount = 0.00

        # Verify enough funds in account
        if (amount + accounts[pin][selection]) >= 0:
            accounts[pin][selection] = round((accounts[pin][selection] + amount), 2)
            print(f'Transaction complete. New balance is {accounts[pin][selection]: ,.2f}')
        else:
            print('Insufficient Funds. Transaction Cancelled.')

        dataStructureTwo=[time.ctime(),accounts[pin]['Name'],beforeCalculation,logger.format_money(amount),logger.format_money(accounts[pin][selection])]
        dataStructure.append(dataStructureTwo)


# end of application loop

print('\n\nSaving data...')
# Write account data to file
with open('customers.json', 'w') as filePointer:
    json.dump(accounts, filePointer)

print('\nData Saved.\nExiting...')

logger.log_transactions(dataStructure)
