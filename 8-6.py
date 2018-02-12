mlist = []
while True:
    test = input("Enter a number: ")
    if test == "done" : 
        break
    try:
        num = float(test)
    except:
        print("Invalid input")
        continue
    x = mlist.append(num)
print("Maximum:", max(mlist))
print("Minimum:", min(mlist))