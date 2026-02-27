inventory = {}

while True:

    print("\n1.Add Item")
    print("2.View Inventory")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))

        inventory[item] = qty

        print("Item added")


    elif choice == "2":

        print("\nInventory:")

        for item in inventory:
            print(item, ":", inventory[item])


    elif choice == "3":
        break

    else:
        print("Invalid choice")