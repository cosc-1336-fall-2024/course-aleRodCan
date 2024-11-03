#
from dictionary import get_p_distance_matrix

def main():
    dna_list = [
        "TTCCTTT",
        "ATTTCGT",
        "GTATTCA",
        "TTATTCA"
    ]

    while True:
        print("Menu:")
        print("1 - Get p distance matrix")
        print("2 - Exit")

        choice = input("Chose an option: ")

        if choice == '1':
            matrix = get_p_distance_matrix(dna_list)
            for row in matrix:
                print(" ".join(f"{value:.3f}" for value in row))
        elif choice == '2':
            print("exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
        
    if __name__ == '__main__':
        main()