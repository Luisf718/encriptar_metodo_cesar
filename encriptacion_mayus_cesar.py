def run():
    shift = 3
    text = input("Escribe el mensaje que quires cifrar en MAYUSCULA: ")
    encryption = ""
    for c in text:
        if c.isupper():
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encryption = encryption + new_character
        else:
            encryption += c
            
    print("Plain text:",text)
    print("Encrypted text:",encryption)

if __name__ == "__main__":
    run()