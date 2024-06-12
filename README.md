# PASSWORD MANAGER

## Description

A password manager made with Python that allows you to add, edit, view and delete accounts from different plattforms, allowing you, with a master key, to not have the need to remember your passwords.

Project Structure:

- project.py
- test_project.py
- passwords.db
- requirements.txt
- README.md

## Demo

https://www.youtube.com/watch?v=Uxcm9s69X04

## Libraries

`requirements.txt`

**SQLITE3 :** This module implements a lightweight disk-based database that allows accessing the database using a nonstandard variant of the SQL query language.

**GETPASS :** Allows the user to insert the passwords in the program without showing them.

**OS :** Used to return the system's enviroment variables, to compare the master key with the user's input.

**TABULATE :** It involves the printing of tables, graphically displaying the database.

## Usage

`project.py`

```
----------------------------------------
PASSWORD MANAGER
all - GET ALL ACCOUNTS
search - GET SPECIFIC ACCOUNT BY SERVICE
add - ADD ACCOUNT
update - UPDATE PASSWORD OF AN ACCOUNT
delete - DELETE ACCOUNT
q - QUIT
----------------------------------------
SELECT AN OPTION:
```

After that, the user can select an option by typing the name written on the left (case-insensitive).

Every time the user finishes a process, is returned to the main menu, where he can type `q` and exit the program.

### Master Key

The master key to access the program its the System's Environment Variable `ADM_PWD`, which can be created like any other Enviromental Variable.

## Functioning

The project.py contains 7 functions including the main function.

### **checker(service)** **function** :

The function takes the service to analyze, it makes a call to the database and checks if the service its registered on it, then it returns `True` or `False` based on the result.

### **get_all()** **function** :

This function takes no arguments, it makes a call to the database by a query using `sqlite3` and returns all the results on a tuple inside of a list.

### **get_specific(service)** **function** :

This function prompts the user for the service, calls the **checker(service)** function and based on the boolean returned, prints or not the account registered with that service.

### **add_acc(service)** **function** :

The function prompts the user for the service, checks if its not in the database using **checker(service)** and then, it finish collecting the necessary information to insert the data into the database.

### **update_acc(service)** **function** :

This function prompts the user for the service, checks if it exists on the database using **checker(service)**, shows the user the actual password of the account and then asks for the new password.

### **delete_acc(service)** **function** :

Prompts the user for the service, checks if it exists on the database using **checker(service)** and then removes it from the database.

## Author

- [@valentin-correa](https://www.github.com/valentin-correa)
