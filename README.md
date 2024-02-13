# Bank-Balance-System


Bank Balance System
The bank balance system is an application which simulates how the bank account works in real life.
The flow of the bank balance system is quite simple. When the program starts, it will ask for the password. When the password is entered, the system will compare the password with all the passwords in the system. If there is a match, it means the system can identify the account owner successfully.
Once the identity is verified, the system will ask the user to select the account. Users can type “C” for checking or “S” for saving. Afterwards, the corresponding account balance will be displayed to the user.
Users can deposit and withdraw money to the selected account. To withdraw, the user can enter a minus sign with the amount. For instance, if you want to withdraw 10 dollars, then you can enter -10. Conversely, if the user wants to deposit money to the account, he/she needs to enter the amount only. For instance, if you want to deposit 10 dollars, then you can enter 10 to the system. 
After deposit or withdrawal, the system will show the new account balance to the user. Afterwards, the system will start over. Users can enter a valid password to continue or enter “x” to exit the application.
The application stores password, name, and account balances in a JSON file. In addition, transaction records will be stored in a CSV file, which allows administrators to track transaction history. The bank balance system will perform read and write operations on the files, which ensure data won't be lost even if the program terminates. This is very important, since a bank system should display up to date information to their clients, and there should not be any mistakes.


![pinFromJSON](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/3161db5f-8b9e-43e0-afd2-231106b22043)

In the image above, it shows how information is displayed in the JSON file. The key is the password, and the value cnotains name, "C", and "S". "C" stands for checking account, and "S" stands for saving account. In this case, we have 9999 as the password, Jill Jones as the name, 10358.78 as the checking account balance and 3062.31 as the saving account balance.


![AfterEnteringpin](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/b8d8cd24-da5c-4018-b913-5cf8d85a5f98)

In the image above, it shows the password is entered and the enter button is pressed. Afterwards, you will see the name of the account holder. The system will ask you to enter "C" or "S". "C" means checking and "S" means saving. You need to select the account before heading to the next step.


![AfterSelectingChecking](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/772e193d-1195-4e69-99b1-129f3f942feb)

In the image above, it shows I entered "C", which means checking account is selected. The program provides instructions on how to withdraw or deposit money to the account. Also, it shows the balance of the selected account. Lastly, it will ask for the transaction amount.


![withdraw100](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/7cecd398-1dcd-4026-bf1a-92f4f8e94d19)

In the image above, it shows 100 dollars is being withdrawn from the account. Afterwards, the program will print out the updated balance, and the operation will end. Following, the program will ask for a pin or you can enter "X" to exit the application.


![pressXToTerminate](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/a7b14176-9832-4141-a774-3a5c94ba3a33)

In the image above, it shows "X" is being entered into the entry. After entering "X", the program will save the data and exit the program.


![JSONCheckingBalUpdated](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/1a078f6a-17e3-4594-b396-8385a0e62470)

In the image above, it shows the balance is updated. I withdrew 100 dollars previously, and the balance is updated as well.When comparing the after withdrawal balance and the updated balance in the JSON file, you can see they are the same, so it tells us the balance is updated correctly.


![TransactionRecord](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/b66902fd-721a-4956-9c24-a4bf5c46c9f5)

In the image above, it shows the transaction record of the withdrawal operation I did above. The transation record is saved in a CSV file. The record clearly shows date,time, name, old balance, transaction, and new balance. It records the account activity, which is an important feature for the bank, since it allows the bank to trace the past activities and investigate when necessary.


![AddMoney30dollar](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/7f26f727-01ab-4f89-887d-495c8f44778b)

In the image above, it shows I deposit 30 dollars to the account. The application prints out the updated balance. Afterwards, the application will ask for a pin or you can enter "x" to exit the application.


![ExitAfterAddMoney](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/adf26f4f-f1ec-4b63-a3b1-1ee58b17b3dc)

In the image above, I entered "X" to the entry. After entering "X", the application will save all the data. Following, it will exit the application.


![CheckingBalUpdatedAfterAddMoney](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/3669401f-0b02-4377-b2db-39ba3df6eac9)

In the image above, it shows the checking balance is updated. In addition, the balance is updated correctly, since the updated balance has the same value as the after desposit balance I got above.


![TransactionRecordAfterAddMoney](https://github.com/jefjefhui/Bank-Balance-System/assets/73283123/188a987c-2177-4447-b2ae-435bdfa4513d)

In the image above, it shows the transaction record. This transaction record has the same format as the previous one I displayed above. In the second last column of this transaction record, you can see "$30", which means deposit 30 dollars, and it is exactly what I did above.


The images above demonstrate how withdraw and deposit works on the checking account. For the saving account account, it works totally the same as the checking account, you can apply the same method to withdraw and deposit funds to the account. The only difference between the checking account and the saving account is the account type. Otherwise, everything on these accounts will be the same. As the operations between these two accounts are exactly the same, so I won't demonstrate the same operations all over again, as it will make it too repetitive.
