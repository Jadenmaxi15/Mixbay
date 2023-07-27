import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from itertools import cycle

# Pixabay API key - Replace 'YOUR_PIXABAY_API_KEY' with your actual API key
API_KEY = '27065965-6f3403037cd82e39462f07a37'

def fetch_images(keyword):
    url = f'https://pixabay.com/api/?key={API_KEY}&q={keyword}&image_type=photo'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['hits']
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error', f"Failed to fetch images: {e}")
        return []

def show_images(keyword):
    images_data = fetch_images(keyword)
    if not images_data:
        return

    image_urls = [image_data['webformatURL'] for image_data in images_data]
    image_cycle = cycle(image_urls)

    def navigate(forward=True):
        nonlocal current_image, photo_label
        current_image = next(image_cycle) if forward else prev_image()
        response = requests.get(current_image)
        image = Image.open(response.content)
        photo = ImageTk.PhotoImage(image)

        photo_label.config(image=photo)
        photo_label.image = photo

    def prev_image():
        nonlocal current_image
        prev_image = current_image
        current_image = next(image_cycle)
        return prev_image

    def close_window():
        image_window.destroy()

    # Create a new window to display the images
    image_window = tk.Toplevel(root)
    image_window.title(f"Images for '{keyword}'")

    current_image = next(image_cycle)
    response = requests.get(current_image)
    image = Image.open(response.content)
    photo = ImageTk.PhotoImage(image)

    photo_label = tk.Label(image_window, image=photo)
    photo_label.pack(pady=10)

    prev_button = tk.Button(image_window, text="Previous", command=lambda: navigate(forward=False))
    prev_button.pack(side=tk.LEFT, padx=10)

    next_button = tk.Button(image_window, text="Next", command=navigate)
    next_button.pack(side=tk.RIGHT, padx=10)

    close_button = tk.Button(image_window, text="Close", command=close_window)
    close_button.pack(pady=10)

    # Keep a reference to the PhotoImage object to avoid garbage collection
    photo_label.image = photo

# Create the main application window
root = tk.Tk()
root.title("Pixabay Image Viewer")

# Create widgets
label = tk.Label(root, text="Enter keyword to search images on Pixabay:")
label.pack(pady=10)

keyword_entry = tk.Entry(root, width=30)
keyword_entry.pack(pady=5)

search_button = tk.Button(root, text="Search Images", command=lambda: show_images(keyword_entry.get()))
search_button.pack(pady=10)

# Start the main event loop
root.mainloop()

