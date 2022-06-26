# import module sys to get the type of exception

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", dir(e))
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)