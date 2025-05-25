# Basic ToDo list console application
# Siphuma Thendo
"""
Github: thendoshane
Instagram: thendoshane
"""

"""
Inspiration: During one of my learning of the numpy library, i spent two minutes recalling some of the projects i have
had to do as a Web Developer which was the ToDO list using the placeholder API and in split second i just though, why not?
let me use these basic principles of python to create a ToDo list and boom here we are

- This is basic, watch out for more advanced todo list
"""
"""
This application utilizes the following Python concepts:
1. Data type: List
2. Functions
3. Comments
4. Syntax and Indentations
5. Try, Except concept
6. Repetition (for loop)
7. Conditional (if else)
8. Input and output
"""
todo_list = []
def options():
    print("___Welcome___")
    print("1. View to do list")
    print("2. Add to list")
    print("3. delete list")
    print("4. Exit")
    try:
        option = int(input("Select an option: "))
        
        if option == 1:
            view()
        elif option == 2:
            add()
        elif option == 3:
            delete()
        elif option == 4:
            print("Goodbye...")
            exit()
        else:
            print("Invalid option")
            options()
    except:
        print("Option not allowed")
        options()

def view():
    if not todo_list:
        print("___The list is Empty___")
    else:
        print("\n__To do list__")
        for a in todo_list:
            print(a)
    options()

def add():
    value = input("Enter text to add or type 'main' to go to main menu: ")
    if value == "main":
        print("Going to main menu...\n")
        options()
    else:
        try:
            todo_list.append(value)
            added = int(input(value+ ", Added to list, \n press 1 to go to main menu or 2 to add again: "))
            if added == 1:
                options()
            elif added == 2:
                add()
            else:
                print("Invalid Option")
                options()
        except:
            print("Can not add "+value+ " to list, try again...")
            add()
def delete():
    if not todo_list:
        print("__List is empty__ \n add items: ")
        add()
    print("__Select an Option__")
    try:
        print("1. Delete item")
        print("2. Clear list")
        item = input()
        if item == "1":
            print("\n__Check item to delete__")
            for i, item in enumerate(todo_list, start=1):
                print(f"{i}. {item}")
            try:
                dele = input("\n Enter the intem to delete: ")
                position = todo_list.index(dele)
                try:
                    todo_list.pop(position)
                    print(dele+ " deleted... \n going to main menu")
                    options()
                except:
                    print("Not found, try again\n")
                    delete()
            except:
                app = input("Could not delete item {dele},\n do you want to add it to list ? Yes/No")
                if app.lower() == "yes":
                    todo_list.append(dele)
                    print("__New List__\n")
                    for a in todo_list:
                        print(a +"\n")
                        options()
                else:
                    options()
        elif item == 2:
            print("__clearing the list...")
            todo_list.clear(all)
            options()
    except:
        print("__something went wrong__")
        options()
options()