#### task 1 ####

tv_shows = []

def add_show():
    title = input("Enter the title of the TV show to add: ")
    tv_shows.append(title)
    print(f"'{title}' has been added.")


def remove_show():
    title = input("Enter the title of the TV show to remove: ")
    if title in tv_shows:
        tv_shows.remove(title)
        print(f"'{title}' has been removed.")
    else:
        print(f"'{title}' not found in the list.")


def search_show():
    title = input("Enter the title of the TV show to search for: ")
    if title in tv_shows:
        print(f"'{title}' found in the list.")
    else:
        print(f"'{title}' not found in the list.")


def view_all_shows():
    if tv_shows:
        print("\n--- All TV Shows ---")
        for show in tv_shows:
            print(show)
        print("--------------------")
    else:
        print("No TV shows in the list.")


def display_menu():
    print("\n--- TV Show Manager Menu ---")
    print("1. Add a TV show")
    print("2. Remove a TV show")
    print("3. Search for a TV show")
    print("4. View all TV shows")
    print("5. Exit")
    print("----------------------------")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_show()
        elif choice == '2':
            remove_show()
        elif choice == '3':
            search_show()
        elif choice == '4':
            view_all_shows()
        elif choice == '5':
            print("Exiting TV Show Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if name == "main":
    main()
