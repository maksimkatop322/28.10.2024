# Program to calculate the average of a list of numbers

def get_numbers():
    number_list = []
    while len(number_list) < 1:
        print("Enter numbers separated by spaces: ")
        numbers = input(">>> ")
        number_list = numbers.split(" ")
        try:
            number_list = [int(num) for num in number_list]
        except ValueError:
            print("Mēģini vēlreiz.")
            number_list = []
            continue
    return


def calculate_average(nums):
    total = sum(nums)
    avg = total / len(nums)
    return avg


def main():
    print("This program calculates the average of your input numbers.")
    numbers = get_numbers()

    average = calculate_average(numbers)

    print(f"The average is: {average}")


# Run the program
if __name__ == "__main__":
    main()
