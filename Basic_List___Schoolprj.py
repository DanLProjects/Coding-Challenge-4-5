def inputChoice(list):
    Num_nums = int(input("How many names do you want to input: "))
    for num in range(Num_nums):
        temp = input("What name do you want to input: ")
        list.append(temp) # adds names to the list
    print("This is the current list", list)
    return list
def printlist(list):
    choice = input("Do you want to print the list in original order or reverse: ")
    if choice.lower() == "original":
        print("The list is",list)
    elif choice.lower() == "reverse":
        list.reverse() # reverses the list
        print("The reversed list is",list)
    else:
        print("Not defined")
#main
main_list = []
while True:
    print("\n\n##################\n",
        "1. Input items\n",
        "2. Choose index to print out\n",
        "3. Print a slice of list\n",
        "4. Print entire list\n",
        "5. Clear a certian index\n",
        "6. Exit"
        )
    choice = input("What would you like to choose: ")
    if choice == "1":
        main_list = inputChoice(main_list) # calls func 1
    elif choice == "2":
        choice = int(input("What index do you want to print: "))
        indexprint = lambda index, list : list[index] # prints the name at the index as a lambda
        print("You have chosen",indexprint(choice, main_list))
    elif choice == "3":
        firstIndex = int(input("First index to start the slice: "))
        lastIndex = int(input("Last index to end the slice: "))
        sliceprint = lambda first, last, list : list[first:last] # prints the list of names at the indexes as a lambda
        print("You have chosen",sliceprint(firstIndex, lastIndex, main_list))
    elif choice == "4":
        printlist(main_list)
    elif choice == "5":
        indexClear = int(input("What index to clear: "))
        index_to_clear = lambda index, list : list.pop(index)
        print("Index",indexClear, "has been emptied", index_to_clear(indexClear, main_list))
    elif choice == "6":
        print("Exiting program...")
        break # exits program
    else:
        print("Please choose an option...")
