import cv2
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Load encrypted image
img_path = os.path.join(script_dir, 'encryptedImage.png')
img = cv2.imread(img_path)

if img is None:
    raise ValueError("Image not found or unable to read")

# Read metadata
metadata_path = os.path.join(script_dir, 'metadata.txt')
with open(metadata_path, 'r') as f:
    stored_password = f.readline().strip()
    msg_length = int(f.readline().strip())


# Ask user for passcode
pas = input("Enter passcode for Decryption: ")

# Dictionary for ASCII conversion
c = {i: chr(i) for i in range(255)}

# Variables to track pixel positions
n = 0
m = 0
z = 0
message = ""

# Check password & decrypt
if pas == stored_password:
    for i in range(msg_length):
        if n >= img.shape[0] or m >= img.shape[1]:
            raise ValueError("Message length exceeds image dimensions")
# Extract pixel values
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    print("Decrypted Message:", message)
else:
    print("Incorrect passcode. Access denied!")
