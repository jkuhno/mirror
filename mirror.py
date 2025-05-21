import os
import cv2

from tkinter import ttk, filedialog, StringVar
from tkinter import *

root = Tk()
root.title("Mirror Image Creator")


def process_images(input_dir):

    mirror_dir = os.path.join(input_dir, 'mirror')
    if not os.path.exists(mirror_dir):
        os.makedirs(mirror_dir)

    err_list = []

    for f in os.listdir(input_dir):
        if f.endswith('.jpg') or f.endswith('.png'):
            img_path = os.path.join(input_dir, f)
            img = cv2.imread(img_path)

            if img is not None:
                status_var.set(f"Processing {f}...")
                root.update()

                flipped_img = cv2.flip(img, 1)
                flipped_img_path = os.path.join(mirror_dir, f)
                cv2.imwrite(flipped_img_path, flipped_img)
    
            else:
                status_var.set(f"Failed to read {f}")
                root.update()
                
                err_list.append(f)


    if err_list:
        status_var.set(f"Errors occurred with the following files: {', '.join(err_list)}")
    else:
        status_var.set(f"Processing complete! Check the {mirror_dir} folder.")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        root.directory = directory
        print(f"Selected directory: {directory}")
        process_images(directory)



# ChatGPT UI
root.geometry("600x250")

status_var = StringVar()
status_var.set("Please select a directory to begin.")

frm = ttk.Frame(root, padding=20)
frm.grid(sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(frm, text="Click the button below to select a directory to process:").grid(column=0, row=0, columnspan=2, pady=(0, 10))


ttk.Button(frm, text="Select Directory", command=select_directory).grid(column=0, row=1, padx=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1, padx=5)

status_label = ttk.Label(frm, textvariable=status_var, foreground="blue")
status_label.grid(column=0, row=2, columnspan=2, pady=(15, 0))

root.mainloop()


