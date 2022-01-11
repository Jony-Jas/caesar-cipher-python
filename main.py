alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            cipher_text+= alphabet[(alphabet.index(letter)+shift)%26]
        else:
            cipher_text+= letter            
    print(f"The encoded text is {cipher_text}\n")
    
def decrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            cipher_text+= alphabet[(alphabet.index(letter)-shift)%26]
        else:
            cipher_text+= letter
    print(f"The decoded text is {cipher_text}\n")


from art import logo
print(logo)

should_end = False

while not should_end:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
