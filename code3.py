def getFirstName(fullName):
    firstName=fullName.split()
    return firstName[0]
name=input("Enter full name")
print(getFirstName(name))
