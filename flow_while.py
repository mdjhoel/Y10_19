keepgoing = True
while keepgoing:
    mystr = input("enter string to print (99 to quit): ")
    if (mystr == "99"):
        print("See you later")
        keepgoing = False
    else:
        print(mystr)
