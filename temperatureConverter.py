print()

user_choice = ' '

while user_choice != '3':
    
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")
    user_choice = input("Select an Option: ")

    if user_choice == '1':
        fahrenheit = int(input("\nEnter the Temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * (5 / 9)
        print(f"{fahrenheit} Degrees Fahrenheit is Equal to {celsius} Degrees Celsius.\n")

    elif user_choice == '2':
        celsius = int(input("\nEnter the Temperature in Celsius: "))
        fahrenheit = (9 / 5) * celsius + 32
        print(f"{celsius} Degrees Celsius is Equal to {fahrenheit} Degrees Fahrenheit.\n")

    elif user_choice == '3':
        print("\nThank You. Goodbye.\n")
        break

    else:
        print("Please Enter a Valid Option.\n")

