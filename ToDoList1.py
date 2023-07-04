1def show_menu():
    print("Menu:")
    print("1. display to-do list")
    print("2. Add task to to-do list")
    print("3. Mark task as done")
    print("4. Quit")


def show_list(to_do_list):
    print("To-do list:")
    if len(to_do_list) == 0:
        print("No items in the list.")
    else:
        for i, item in enumerate(to_do_list, 1):
            print(f"{i}. {item}")


def add_item(to_do_list):
    item = input("Enter the item to add: ")
    to_do_list.append(item)
    print(f"Added '{item}' to the to-do list.")


def mark_item_done(to_do_list):
    show_list(to_do_list)
    if len(to_do_list) == 0:
        return

    try:
        item_number = int(input("Enter the number of the item to mark as done: "))
        if item_number < 1 or item_number > len(to_do_list):
            print("Invalid item number.")
        else:
            item = to_do_list.pop(item_number - 1)
            print(f"Marked '{item}' as done.")
    except ValueError:
        print("Invalid input.")


def main():
    to_do_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_list(to_do_list)
        elif choice == '2':
            add_item(to_do_list)
        elif choice == '3':
            mark_item_done(to_do_list)
        elif choice == '4':
            print("today tasks are over,goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
