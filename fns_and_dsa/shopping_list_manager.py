def shopping_list_manager():
    shopping_list = []

    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':
            print("Shopping List:")
            for item in shopping_list:
                print(item)

        elif choice == '4':
            print("Exiting Shopping List Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

shopping_list_manager()