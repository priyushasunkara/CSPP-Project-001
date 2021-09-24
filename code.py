def getFirstName(fullName):
    for i in range(len(fullName)):
        if fullName[i]==" ":
            index=i
            print(index)
            break
    firstName=fullName[0:index]
    return firstName
name="Donald Knuth"
print(getFirstName(name))
