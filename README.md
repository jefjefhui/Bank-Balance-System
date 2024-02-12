# Bank-Balance-System


Bank Balance System
The bank balance system is an application which simulates how the bank account works in real life.
The flow of the bank balance system is quite simple. When the program starts, it will ask for the password. When the password is entered, the system will compare the password with all the passwords in the system. If there is a match, it means the system can identify the account owner successfully.
Once the identity is verified, the system will ask the user to select the account. Users can type “C” for checking or “S” for saving. Afterwards, the corresponding account balance will be displayed to the user.
Users can deposit and withdraw money to the selected account. To withdraw, the user can enter a minus sign with the amount. For instance, if you want to withdraw 10 dollars, then you can enter -10. Conversely, if the user wants to deposit money to the account, he/she needs to enter the amount only. For instance, if you want to deposit 10 dollars, then you can enter 10 to the system. 
After deposit or withdrawal, the system will show the new account balance to the user. Afterwards, the system will start over. Users can enter a valid password to continue or enter “x” to exit the application.
The application stores password, name, and account balances in a JSON file. In addition, transaction records will be stored in a CSV file, which allows administrators to track transaction history. The bank balance system will perform read and write operations on the files, which ensure data won't be lost even if the program terminates. This is very important, since a bank system should display up to date information to their clients, and there should not be any mistakes.
