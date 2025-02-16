# project_stegno
Cybersecurity Project on Steganography using Python.

# **🖼️ Secure Data Hiding in Image using Steganography**

A **steganography-based project** that allows users to **encrypt and hide secret messages inside images** and retrieve them later using a password. Unlike traditional steganography methods, this project **maps ASCII values directly into RGB pixel values**, ensuring **fast, efficient, and lossless encryption**.

## **📌 Features**

✅ **Pixel-Based Character Encoding** – Directly stores ASCII values in image pixels instead of using LSB techniques.  
✅ **RGB Channel Cycling** – Distributes the message across **Red, Green, and Blue** channels for improved security.  
✅ **Password-Protected Decryption** – Ensures only authorized users can retrieve hidden messages.  
✅ **Lossless Image Format (PNG)** – Prevents pixel distortions that occur with JPEG compression.  
✅ **Metadata Persistence** – Stores encryption details (message length & password) in `metadata.txt` for accurate decryption.  
✅ **Standalone Encryption & Decryption** – Works as separate Python scripts for flexibility.  

---

## **🚀 How It Works?**

### **1️⃣ Encryption Process (encrypt.py)**  
- Loads the input image (`mypic.jpg`).  
- Takes a **secret message** and **password** from the user.  
- Encodes message characters into the **pixel values** of the image.  
- Saves the **encrypted image (`encryptedImage.png`)**.  
- Stores message length and password in `metadata.txt` for decryption.  

### **2️⃣ Decryption Process (decrypt.py)**  
- Loads the **encrypted image**.  
- Reads metadata (message length & password) from `metadata.txt`.  
- Asks for the **decryption password**.  
- Extracts the original **hidden message** from pixel values.  

---

## **📂 Project Structure**

```
📁 Image-Encryption
│── encrypt.py        # Encryption script
│── decrypt.py        # Decryption script
│── mypic.jpg         # Original image (replace with your own)
│── encryptedImage.png # Encrypted image output
│── metadata.txt      # Stores passcode & message length
│── README.md         # Project documentation
```

---

## **⚡ Installation & Usage**

### **🔹 Prerequisites**
Ensure you have **Python 3.x** and **OpenCV** installed:
```sh
pip install opencv-python
```

### **🔹 Run Encryption**
```sh
python encrypt.py
```
- **Rename your input image as mypic.jpg and ensure that it is in the same directory as these scripts before running them.**
- Enter your **secret message** and **passcode** when prompted.  
- The **encrypted image** will be saved as `encryptedImage.png`.
  
### **🔹 Run Decryption**
```sh
python decrypt.py
```
- Enter the **correct passcode** to decrypt the hidden message.  

---

## **🛡️ Security Considerations**
- This project uses **simple pixel value modification**, so it's not resistant to **advanced cryptanalysis**.  
- For stronger encryption, consider integrating **AES encryption** before embedding the message.  
- Always use **lossless PNG images** for encryption to prevent pixel distortions.  

---

## **🛠️ Future Enhancements**
🚀 Implement **AES encryption** for stronger security.  
🚀 Use **LSB-based encoding** for more subtle data hiding.  
🚀 Convert this into a **GUI-based web app** for ease of use.  
🚀 Add support for **embedding images inside images**.  

---

## **🤝 Contributing**
Want to improve this project? Feel free to fork and submit a pull request!  

---

## **📩 Contact**
For suggestions, feel free to reach out or open an issue! 🚀  

---

### **🌟 If you find this useful, don’t forget to ⭐ star the repo!** 😃✨

