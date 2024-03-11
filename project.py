import sqlite3
from getpass import getpass
import os
from tabulate import tabulate

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

def main():
    ADM_PWD = os.environ["ADM_PWD"]
    connect_key = ''

    while connect_key != ADM_PWD:
        connect_key = getpass("What's the master key? ")    

    conn.execute("CREATE TABLE IF NOT EXISTS STORE (SERVICE TEXT PRIMARY KEY NOT NULL, USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL)")

    while True:
        print("-" * 40)
        print(
            "PASSWORD MANAGER\nall - GET ALL ACCOUNTS\nsearch - GET SPECIFIC ACCOUNT BY SERVICE\nadd - ADD ACCOUNT\nupdate - UPDATE PASSWORD OF AN ACCOUNT\ndelete - DELETE ACCOUNT\nq - QUIT"
        )
        print("-" * 40)

        option = input("SELECT AN OPTION: ").upper()

        match option:
            case "ALL":
                data = get_all()
                print("\n",tabulate(data, tablefmt='grid', headers=['SERVICE', 'USERNAME', 'PASSWORD']), "\n")
            case "SEARCH":
                service = input("What's the service? ")
                acc = get_specific(service)
                if acc != "\nSERVICE NOT FOUND\n":
                    print("\n",tabulate(acc, tablefmt='grid', headers=['SERVICE', 'USERNAME', 'PASSWORD']), "\n")
                else:
                    print(acc)
            case "ADD":
                service = input("What's the service of the account? ").capitalize()
                print(add_acc(service))
            case "UPDATE":
                service = input("What's the service that you want to update? ").capitalize()
                print(update_acc(service))
            case "DELETE":
                service = input("What's the service that you want to delete? ").capitalize()
                print(delete_acc(service))
            case "Q":
                exit()  
            case _:
                print("Invalid choice")

def get_all():
    data = cursor.execute('SELECT * FROM STORE')
    return data.fetchall()

def get_specific(service):
    if checker(service):
        data = conn.execute(f'SELECT * FROM STORE WHERE SERVICE = "{service.capitalize()}"')
        return data.fetchall()
    else:
        return("\nSERVICE NOT FOUND\n")

def add_acc(service):
    if not checker(service):
        username = input("What's the username/email? ")
        password = getpass("What's the password? ")
        conn.execute(f"INSERT INTO STORE(SERVICE, USERNAME, PASSWORD) VALUES ('{service}', '{username}', '{password}')")
        conn.commit()
        return('\nACCOUNT ADDED SUCCESSFULLY\n')
    else:
        return("\nSERVICE ALREADY EXISTS\n")

def update_acc(service):
    if checker(service):
        cursor.execute(f'SELECT PASSWORD FROM STORE WHERE SERVICE = "{service}"')
        print(f"The current password of {service} is", str(cursor.fetchone()[0]))
        new_pwd = getpass("What's the new password? ")
        update_query = conn.execute(f"UPDATE STORE SET PASSWORD = '{new_pwd}' WHERE SERVICE = '{service}'")
        conn.commit()
        return(f"\n{service.upper()} PASSWORD WAS SUCCESSFULLY UPDATED\n")
    else:
        return("\nSERVICE NOT FOUND\n")
        
def delete_acc(service):
    if checker(service):
        query = conn.execute(f'DELETE FROM STORE WHERE SERVICE = "{service}"')
        choice = input("Are you sure you want to delete this account? y/n ").lower()
        conn.commit()
        return "\nACCOUNT SUCCESSFULLY DELETED\n"
    else:
        return("\nSERVICE NOT FOUND\n")

def checker(service):
    cursor.execute(f"SELECT SERVICE FROM STORE WHERE SERVICE = '{service}'")
    query = cursor.fetchall()
    if len(query) == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    main()