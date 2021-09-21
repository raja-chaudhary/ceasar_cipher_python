from art import logo  # import the ASCII art from art.py
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# initial while loop condition set to true to run the program at least once
rerun_condition = True


def ceasar(text, shift, direction):
    ''' The main function with encoding and decoding logic. This function takes 3 parameters as input.

    Text: The original text that needs to be encoded or decoded

    Shift: The shift number is the amount by which to shift the letters

    Direction: Direction tells if the user wants to encrypt the inputted text or decrypt the inputted text '''

    if direction == 'encode' or direction == 'decode':  # checking direction
        # starting with empty string, this string will hold our encrypted or decrypted text
        cipher_text = ""
        if direction == 'decode':
            shift *= -1  # changing the shift number depending of direction
        for letter in text:
            # important to keep all the letters other than alphabets (symbols, numbers, spaces) intact
            if letter not in alphabet:
                cipher_text += letter
            else:  # only encoding or decoding the alphabets
                position = alphabet.index(letter)
                # new position will either have the shift added to it or subtracted to it depending on the direction. We also need the modulus of 26 in case the user input the shift number greater than 26
                new_position = position + (shift % 26)
                cipher_text += alphabet[new_position]
        print(f"The {direction}d text is '{cipher_text}'")
    else:  # if direction input is anything other than 'encode' or 'decode'
        print("Incorrect input, please chose either encode or decode!!")


while rerun_condition:
    print(logo)
    # below we are taking inputs from the users
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # calling the ceasar function
    ceasar(text=text, shift=shift, direction=direction)

    # checking if the user wants to abort or continue
    rerun = input(
        "Type 'yes' if you want to rerun the ceasar cipher again, to abort type 'no': ")
    if rerun != 'yes':
        rerun_condition = False
