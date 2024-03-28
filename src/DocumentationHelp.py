from colorama import Fore, Style

def new():
    return Fore.BLACK + """
This function it will create a user.
Receives 2 options the name and last name
what are: --name and --last
name: --name (a name) (is a option, is REQUIRED)
lastName: --last (a last name) (is a option, is REQUIRED)
""" + Style.RESET_ALL

def delete():
    return Fore.BLACK + """
this function it will delete a user
Receives 1 argument what is the ID
the user to delete.
""" + Style.RESET_ALL

def update():
    return Fore.BLACK + """
this function it will update the propertys of 
a user Receives 1 argument and 2 options
what are:
_id: Id OF USER (is a argument)
name: --name (a name) (is a option)
lastName: --last (a last name) (is a option)
the user to delete.
""" + Style.RESET_ALL

def user():
    return Fore.BLACK + """
this function it will show a user
Receives 1 argument what is the ID
the user to show.
""" + Style.RESET_ALL

def users():
    return Fore.BLACK +  "it will show all user of the table " + Style.RESET_ALL