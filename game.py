from random import randint

try:
    while True:
        bulls = 0
        cows = 0

        menu_select = int(input("Number guessing!\n1. Start\n2. Exit\n"))

        if menu_select > 2 or menu_select < 1:
            print("Invalid select! try again correct.\n")
            continue

        elif menu_select == 2:
                    print("Exiting programm...")
                    break

        random_num = str(randint(1000, 9999))

        guess = input("Enter a number, you think's correct: ")

        for a in random_num:
              for b in guess:
                    if b == a:
                          bulls += 1

                    elif b in random_num:
                          cows += 1

        if bulls == 4:
              print("You've winned! Collected all of 4 bulls!")

        else:
              print(f"{bulls} bulls, {cows} cows!\n")

except ValueError:
      print("\nInput must be valid!")

except KeyboardInterrupt:
      print("\nExiting Programm...")
