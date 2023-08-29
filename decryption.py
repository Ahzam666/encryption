import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

def decrypt_image():
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img_array = np.array(encrypted_img)
    decrypted_img2 = encrypted_img_array % 16
    decrypted_img_array = decrypted_img2 * 16
    
    decrypted_img = Image.fromarray(decrypted_img_array.astype('uint8'))
    
    # Display the decrypted image
    decrypted_photo = ImageTk.PhotoImage(decrypted_img)
    decrypted_label.config(image=decrypted_photo)
    decrypted_label.photo = decrypted_photo  # Prevent PhotoImage from being garbage collected

def browse_encrypted_image():
    global encrypted_image_path
    encrypted_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.bmp *.png *.jpg *.jpeg")])
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_photo = ImageTk.PhotoImage(encrypted_img)
    encrypted_label.config(image=encrypted_photo)
    encrypted_label.photo = encrypted_photo  # Prevent PhotoImage from being garbage collected

# Create the main application window
root = tk.Tk()
root.title("Image Decryption Tool")

# Browse button for encrypted image
encrypted_button = tk.Button(root, text="Browse Encrypted Image", command=browse_encrypted_image)
encrypted_button.pack()

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack()

# Label to display decrypted image
decrypted_label = tk.Label(root)
decrypted_label.pack()

# Label to display encrypted image
encrypted_label = tk.Label(root)
encrypted_label.pack()

# Start the GUI event loop
root.mainloop()

