import cv2
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Load Image
# Use relative path for better portability
img_path = os.path.join(script_dir, 'mypic.jpg')
img = cv2.imread(img_path)


msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Store ASCII mapping
d = {chr(i): i for i in range(255)}

# Message Length Storage
msg_length = len(msg)

# Variables to iterate over pixels
m = 0
n = 0
z = 0

# Embed message into image pixels
for i in range(msg_length):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Save encrypted image (PNG format to avoid distortion)
encrypted_img_path = os.path.join(script_dir, 'encryptedImage.png')
cv2.imwrite(encrypted_img_path, img)

# Save metadata (password & message length)
metadata_path = os.path.join(script_dir, 'metadata.txt')
with open(metadata_path, 'w') as f:
    f.write(f"{password}\n{msg_length}")  # Save password and length


print("Encryption complete! Image saved as 'encryptedImage.png'")
