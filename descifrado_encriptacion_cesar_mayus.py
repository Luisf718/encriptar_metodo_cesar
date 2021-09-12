def run():
    shift = 3 
    encrypted_text = input("Escribe el mensaje que quieres descifrar, en MAYUSCULA: ")
    plain_text = ""
    for c in encrypted_text:
        if c.isupper():
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index - shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            plain_text = plain_text + new_character
        else:
            plain_text += c
            
    print("Encrypted text:",encrypted_text)
    print("Decrypted text:",plain_text)

if __name__ == "__main__":
    run()