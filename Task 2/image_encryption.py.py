from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (img_array + key) % 256
    
    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (img_array - key) % 256
    
    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'")

def swap_pixels(img_array):
    # Swap pixels: simple example, swap (0, 0) with (1, 1)
    img_array[0, 0], img_array[1, 1] = img_array[1, 1], img_array[0, 0]
    return img_array

def encrypt_with_swap(image_path):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Apply pixel swap
    swapped_array = swap_pixels(img_array)
    
    # Save the swapped image
    swapped_image = Image.fromarray(swapped_array.astype('uint8'))
    swapped_image.save('swapped_image.png')
    print("Image pixel-swapped and saved as 'swapped_image.png'")

def decrypt_with_swap(image_path):
    # Open the swapped image
    img = Image.open(image_path)
    img_array = np.array(img)
    
    # Revert the pixel swap
    swapped_array = swap_pixels(img_array)
    
    # Save the reverted image
    swapped_image = Image.fromarray(swapped_array.astype('uint8'))
    swapped_image.save('unswapped_image.png')
    print("Swapped image reverted and saved as 'unswapped_image.png'")

# Main program
print('*** SIMPLE IMAGE ENCRYPTION TOOL ***')
print()
print('Do you want to encrypt or decrypt?')
user_input = input('e/d/s/rs: ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    image_path = input('Enter the path to the image to encrypt: ')
    key = int(input('Enter the encryption key (an integer): '))
    encrypt_image(image_path, key)

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    image_path = input('Enter the path to the image to decrypt: ')
    key = int(input('Enter the decryption key (an integer): '))
    decrypt_image(image_path, key)

elif user_input == 's':
    print('SWAP ENCRYPTION MODE SELECTED')
    print()
    image_path = input('Enter the path to the image to swap and encrypt: ')
    encrypt_with_swap(image_path)

elif user_input == 'rs':
    print('REVERSE SWAP DECRYPTION MODE SELECTED')
    print()
    image_path = input('Enter the path to the swapped image to revert: ')
    decrypt_with_swap(image_path)
else:
    print('Invalid selection!')
