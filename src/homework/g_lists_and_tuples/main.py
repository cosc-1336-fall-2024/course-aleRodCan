#
from lists import get_lowest_list_value, get_highest_list_value

def main():
    numbers = []
    while True:
        try:
            num = int(input("Enter a number (or type'stop' to finish): "))
            numbers.append(num)
        except ValueError:
            if input("Type 'stop' if you are done, or press Enter to continue: ").strip().lower() == 'stop':
                break

    while True:
        print("\nMenu:")
        print("1. Show the lowest value in the list")
        print("2. Show the highest value in the list")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            print("Lowest value:", get_lowest_list_value(numbers))
        elif choice == '2':
            print("Highest value:", get_highest_list_value(numbers))
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()