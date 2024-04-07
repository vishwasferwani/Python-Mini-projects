alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caeser_text(text,shift,direction):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:

        if char in alphabet:
            x= alphabet.index(char)
            x += shift%26
            cipher_text += alphabet[x]
        else:
            cipher_text += char

    print(f"the {direction}d text is {cipher_text}")
again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caeser_text(text,shift,direction)

    choice = input("do you want to continue yes no: ")
    if choice == "no":
        again = False
        print("goodbye")


    
 