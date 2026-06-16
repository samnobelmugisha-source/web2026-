def main():
    print("Enter positive integers only.")
    print("Press Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) to stop.\n")
    largest = None
    smallest = None
    while True:
        try:
            user_input = input("Enter a positive integer: ")
            number = int(user_input)

            if number <= 0:
                print("Only positive integers are allowed. Try again.")
                continue

            if largest is None and smallest is None:
                largest = number
                smallest = number
            else:
                if number > largest:
                    largest = number
                if number < smallest:
                    smallest = number

        except ValueError:
            
            print("Invalid input. Please enter a positive integer.")
        except EOFError:
           
            print("\nInput stopped.")
            break

    if largest is None:
        print("No valid positive integers were entered.")
    else:
        print("Largest integer:", largest)
        print("Smallest integer:", smallest)

main()
