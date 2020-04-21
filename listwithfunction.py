'''This is list '''
'''In the list we have update this list via CURD option'''
'''We can add, update, show, and delete this list using varius function the. this will be all like we are updating our small data base inside list'''
productlist = []
def listview():
    print(productlist)

def deletelist():
    deleteno = int(input("Which you want to delete, Select Index Position:- "))
    del productlist[deleteno]

def updatelist():
    updateno = int(input("Which entry you want to update, Select Index Position:- "))
    updatename = input("Enter Name - ")
    productlist[updateno] = updatename


def addinlist():
    # addno = int(input("Where you want to add the new entry, Select Index Position:- "))
    addname = (input("What entry you want to add in above location:- "))
    productlist.append(addname)


print("Please enter the no to perform action")
print("1 - Show the List")
print("2 - Delete the Entry")
print("3 - Update the Entry")
print("4 - Add New Entry")
print("5 - For Exit the Program")

try:
    while True:
        x = int(input("Select Your choise:- "))
        if x == 1:
           listview()
        elif x == 2:
            deletelist()
        elif x == 3:
            updatelist()
        elif x == 4:
            addinlist()
        elif x == 5:
            input("Do you want to exit from program, press any key to exit ")
            break
except IndexError:
    print("Enter valid no, there is no name with that index ")

except ValueError:
    print("Invalid Input")