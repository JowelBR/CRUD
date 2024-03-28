import click
import DataClass as dc
import DocumentationHelp as documentation
from colorama import (Fore, Style)

@click.group() # is a collection of all commands
def cli(): #the function gives the name to group
    pass

nameG = "GroupTable" #The name of the table

#created a new user
@cli.command()
@click.option("--name", required=True, help="Name of the user")
@click.option("--last", required=True,  help="Last Name of the user")
@click.pass_context
@click.help_option(documentation.new())
def new(ctx, name, last):
    if name == "" or last == "":
        print(Fore.BLACK + "Last and nameare required !" + Style.RESET_ALL)
    else:
        dc.MethodsDB.InsertObject(nameG, name, last)
        print(Fore.LIGHTGREEN_EX + "The user were created succefully !" + Style.RESET_ALL)

#show a user
@cli.command()
@click.argument("_id", type=int)
@click.help_option(documentation.user())
def user(_id):
    userFound = dc.MethodsDB.ReadObject(nameG, _id)
    if(userFound == []):
        print(Fore.BLACK + "There's none any user with that ID !" + Style.RESET_ALL)
    else:
        for property in userFound:
            print(Fore.BLACK + f"User {property[0]}" + Fore.BLUE + " -> " + Fore.LIGHTGREEN_EX + f"{property[1]} " + Fore.GREEN + f"{property[2]}" + Style.RESET_ALL)


#show all users
@cli.command()
@click.help_option(documentation.users())
def users():
    usersFounds = dc.MethodsDB.ReadObjects(nameG)
    print(Fore.BLACK + "The Users: " + Style.RESET_ALL)
    for user in usersFounds:
        print(Fore.BLACK + f"User {user[0]}" + Fore.BLUE + " -> " + Fore.LIGHTGREEN_EX + f"{user[1]} " + Fore.GREEN + f"{user[2]}" + Style.RESET_ALL)

#updated a user
@cli.command()
@click.argument("_id", type=int)
@click.option("--name",  help="Name of the user")
@click.option("--last",  help="Last Name of the user")
@click.help_option(documentation.update())
def update(_id, name, last):
    userList = dc.MethodsDB.showAllIDs(nameG)
    find = False
    for ids in userList:
        if(ids[0] == _id):
            dc.MethodsDB.UpdateObject(nameG, _id, name, last)
            print(Fore.LIGHTGREEN_EX + "The user were updated succefully ! " + Style.RESET_ALL)
            find = True
    if find == False: print(Fore.BLACK + "There's none any user with that ID !" + Style.RESET_ALL)

#delete a user
@cli.command()
@click.argument("_id", type=int)
@click.help_option(documentation.delete())
def Delete(_id):
    userFound = dc.MethodsDB.ReadObject(nameG, _id)
    if(userFound == []):
        print(Fore.BLACK + "There's none any user with that ID !" + Style.RESET_ALL)
    else:
        dc.MethodsDB.RemoveObject(nameG, _id)
        print(Fore.LIGHTGREEN_EX + "The user were deleted succefully !" + Style.RESET_ALL)

if __name__ == "__main__":
    dc.MethodsDB.createTable(nameG)
    cli()
