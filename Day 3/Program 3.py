def dupli(str):
    duplistr = ""
    for x in str:
        if x not in duplistr:
            duplistr += x
    return duplistr

string = input("Enter str:-")
print("Removing after the duplicates is:", dupli(str))
