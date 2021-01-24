import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()
# c.execute(
#     "CREATE TABLE info (name TEXT, password TEXT)")


def create():
    name = input("Enter name:")
    password = input("Enter password:")
    c.execute("INSERT INTO info VALUES (?, ?)", (name, password))
    conn.commit()


def delete():
    del_name = input("Enter name to delete record:")
    c.execute(
        "DELETE FROM info WHERE name = ?",
        (del_name,)
    )
    conn.commit()


def update():
    selected_name = input("Enter name you want to edit:")
    choice = int(input("Enter 1 to change name, 2 to change password:"))

    if choice == 1:
        new_name = input("Enter new name:")
        c.execute(
            "UPDATE info SET name = ? WHERE name = ?",
            (new_name, selected_name)
        )
        conn.commit()

    elif option == 2:
        new_password = input("Enter new password:")
        c.execute(
            "UPDATE info SET password = ? WHERE name = ?",
            (new_password, selected_name)
        )
        conn.commit()

    else:
        print("ERROR")


def view():
    rows = c.execute(
        "SELECT * FROM info").fetchall()
    print(*rows)


def menu():
    run = 'y'
    while run.lower() == 'y':
        print("1.View \n2.Create \n3.Update \n4.Delete \n5.Quit")
        opt = int(input("Select Option:"))
        if opt == 1:
            view()
        elif opt == 2:
            create()
        elif opt == 3:
            update()
        elif opt == 4:
            delete()
        elif opt == 5:
            exit()
        else:
            print("ERROR - wrong input")
        run = input("Do you want to run again?(y/n)")
        if run == "n":
            break


menu()
