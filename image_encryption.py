from PIL import Image


# methode 1:  By Mathematical Operation
def math_process(image_path, key, mode):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            if mode == 'encrypt':
                # add the key to encrypt
                new_r = (r + key) % 256
                new_g = (g + key) % 256
                new_b = (b + key) % 256
            else:
                # subtract the key to decrypt
                new_r = (r - key) % 256
                new_g = (g - key) % 256
                new_b = (b - key) % 256

            pixels[x, y] = (new_r, new_g, new_b)

    output_name = f"{mode}_math_result.png"
    img.save(output_name)
    print(f"  Success ! The image has been saved as:   '{output_name}' ")
    img.show()  # see the result


# methode 2: By XOR
def xor_process(image_path, key):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR is the same for both (Enc/dec)
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    output_name = "xor_result.png"
    img.save(output_name)
    print(f" Success ! The image has been saved as: '{output_name}' ")
    img.show()


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    print("--- Image Encryption Tool ---")
    path = input("insert the file name (e.g: input.jpg): ")
    secret_key = int(input("put the secret key: "))

    print("\n choose your method:")
    print("1. Mathematical (Encryption)")
    print("2. Mathematical (Decryption)")
    print("3. XOR Method (Encryption & Decryption)")

    choice = input("chose(1/2/3): ")

    if choice == '1':
        math_process(path, secret_key, 'encrypt')
    elif choice == '2':
        math_process(path, secret_key, 'decrypt')
    elif choice == '3':
        xor_process(path, secret_key)
    else:
        print(" invalid choice !!!")