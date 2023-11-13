# caesar.py

# libraries/modules
import string
import sys


# Casesar Cipher class
class Caesar:
    # method to initally prompt user
    def get_input():
        # prompt check
        while True:
            print("Please select an option:")
            print("1) Encode plaintext")
            print("2) Decode ciphertext")
            print("3) Run hard-code example")
            print("0) Exit Program")

            choice = input("\nEnter > ")
            if choice in ["1", "2", "3", "0", 1, 2, 3, 0]:
                break
            else:
                print("\nSelection invalid, try again.\n")

        # checks user input choice
        if choice in ["1", 1]:
            Caesar.encrypt()
        elif choice in ["2", 2]:
            Caesar.decrpyt()
        elif choice in ["3", 3]:
            Caesar.example()
        elif choice in ["0", 0]:
            Caesar.exit_program()

    # hard-code example method
    def example():
        print("\nThis is a hard-coded example of using Caesar Cipher.")
        input("Press enter to continue...\n")
        P = "Hello, World!"
        k = 3

        print(f'When encoding a plaintext "{P}" with a shift amount (key) of "{k}".')
        print(f'Each character in the plaintext will be shifted to the right by "{k}".')
        input("Press enter to continue...\n")

        encrypted_text = ""
        for index, c in enumerate(P.upper()):
            if c.isalpha():
                encrypted_text += string.ascii_uppercase[
                    (string.ascii_uppercase.index(c) + k) % 26
                ]
                print(
                    f"Character \u0332{c} is shifted to \u0332{encrypted_text[index]} by {k}."
                )
            elif c.isdigit():
                encrypted_text += str((int(c) + k) % 26)
                print(
                    f"Character \u0332{c} is shifted to \u0332{encrypted_text[index]} by {k}."
                )
            else:
                encrypted_text += c
                print(f"Character \u0332{c} is not affected by shift.")

        print(f'\nThe encoded plaintext is now: "{encrypted_text}"')
        input("Press enter to continue...\n")

        C = encrypted_text
        print(f'When decoding a ciphertext "{C}" with a shift amount (key) of "{k}".')
        print(f'Each character in the plaintext will be shifted to the left by "{k}".')
        input("Press enter to continue...\n")

        decrypted_text = ""
        for index, c in enumerate(C.upper()):
            if c.isalpha():
                decrypted_text += string.ascii_uppercase[
                    (string.ascii_uppercase.index(c) - k) % 26
                ]
                print(
                    f"Character \u0332{c} is shifted to \u0332{decrypted_text[index]} by {k}."
                )
            elif c.isdigit():
                decrypted_text += str((int(c) - k) % 26)
                print(
                    f"Character \u0332{c} is shifted to \u0332{decrypted_text[index]} by {k}."
                )
            else:
                decrypted_text += c
                print(f"Character \u0332{c} is not affected by shift.")

        print(f'\nThe decoded ciphertext is now: "{decrypted_text}"')
        input("Press enter to continue...\n")

        Caesar.try_again()

    # method to exit program
    def exit_program():
        print("\nExiting program now...\n")
        sys.exit()

    # method to prompt user to try the program again
    def try_again():
        # prompt check
        while True:
            user_in = input("\nWould you like to run the program again? (y/n) > ")
            if user_in.lower() in ["y", "n", "yes", "no"]:
                break
            else:
                print("\nInvalid input, try again.\n")

        # checks user input
        if user_in.lower() in ["y", "yes"]:
            Caesar.get_input()
        elif user_in.lower() in ["n", "no"]:
            Caesar.exit_program()

    # method to get user text input
    def get_text():
        # prompt check
        while True:
            text = input("Enter a text (ASCII only): ")
            if text.isascii():
                text = text.upper()  # convert input to uppercase
                break
            else:
                print("Text is not valid, try again.")

        # return value
        return text

    # method to get user shift amount input
    def get_shift():
        # checks and prompts user for shift amount input
        while True:
            shift = input("Enter a shift amount (integer): ")
            try:
                shift = int(shift)  # convert input to integer
                break
            except ValueError:
                print("Shift amount is not valid, try again.")

        # return value
        return shift

    # encoding method
    def encrypt():
        print("\nEncrypting plaintext...\n")

        # prompt user for inputs
        P = Caesar.get_text()  # plaintext
        k = Caesar.get_shift()  # key

        print(f'\nEncrypting "{P}" with shift amount "{k}"')

        encrypted_text = ""  # create empty encrypted text

        # iterate each character in plaintext with shift amount
        # store end result as encrypted text
        for c in P:
            if c.isalpha():  # alphabetic characters
                encrypted_text += string.ascii_uppercase[
                    (string.ascii_uppercase.index(c) + k) % 26
                ]
            elif c.isdigit():  # numbers
                encrypted_text += str((int(c) + k) % 10)
            else:  # everything else
                encrypted_text += c

        # output
        print(f'\nEncrypted text: "{encrypted_text}"')
        Caesar.try_again()

    # decoding method
    def decrpyt():
        print("\nDecrypting ciphertext...")

        # prompt user for inputs
        C = Caesar.get_text()  # ciphertext
        k = Caesar.get_shift()  # key

        print(f'\nDecrypting "{C}" with shift amount "{k}"')

        decrypted_text = ""  # create empty decrypted text

        # iterate each character in ciphertext with shift amount
        # store end result as decrypted text
        for c in C:
            if c.isalpha():  # alphabetic characters
                decrypted_text += string.ascii_uppercase[
                    (string.ascii_uppercase.index(c) - k) % 26
                ]
            elif c.isdigit():  # numbers
                decrypted_text += str((int(c) - k) % 10)
            else:  # everything else
                decrypted_text += c

        # output
        print(f'\nDecrypted text: "{decrypted_text}"')
        Caesar.try_again()
