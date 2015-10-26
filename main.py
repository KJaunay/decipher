import sys

alphabet = {}   # used to represent key:letter pairs (a=1, b=2 ... z=26)
main_menu = {1: {"banner": "Shift cipher", "method": "self.shiftcipher"},
             2: {"banner": "Caesar cipher", "method": "self.caesarcipher"},
             3: {"banner": "Option 2", "method": "self.option2"},
             4: {"banner": "Option 3", "method": "self.option2"},
             9: {"banner": "EXIT"}}

class Decipher():

    def cipherword(self, word, shift):

    # TODO: Apply shift

        #print("Plaintext is \"{}\", the shift key is {}\n".format(word, shift))


    def shiftcipher(self):
        print("you chose shift cipher")
        # TODO filter input
        while True:
            try:
                # Get word/sentence
                choice = input("What would you like to encrypt?\n")
                if choice.isalpha():
                    print("Is Alpha")
                    # Get shift integer
                    shift = int(input("please enter shift value between 0-25\n"))
                    # TODO: Check validity

                else:
                    print("Incorrect input. Please enter a word or sentence that you would like to encrypt")

                # Call method to apply cipher and print return valu.
                decipher.cipherword(choice, shift)
            except ValueError as err:
                print(err)


    def caesarcipher(self):
        print("you chose caesar cipher")

    def option2(self):
        print("you chose option2")

    def main(self):

        for key in main_menu:
            print(key, main_menu[key]["banner"])
        while True:
            try:
                choice = int(input("Please choose from the above main menu\n"))
                if choice in main_menu:
                    if choice == 9:
                        sys.exit()
                    eval(main_menu[choice]["method"] + "()")
                else:
                    print("An error has occurred, please try again")
            except ValueError:
                print("Incorrect input. Please select an option from the menu above")

if __name__ == "__main__":  # allows program to be imported as a module by not automatically running

    # fill global constant alphabet with key:value pairs (a=1, b=2 ... z=26)
    for v,l in enumerate("abcdefghijklmnopqrstuvwxyz"):
        alphabet[v + 1] = l

    decipher = Decipher()
    decipher.main()