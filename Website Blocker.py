
from tkinter import*
import customtkinter as ck
from tkinter import messagebox
from PIL import ImageTk, Image
from elevate import elevate
elevate()

root = Tk()
root.title('Website Blocker')
# LOCALHOST REDIRECT & PATH OF THE HOST FILE IN WINDOWS
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def websites():
    website_lists = entry.get()
    Website = list(set(website_lists.split(",")))
    return Website
    

def block():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in websites():
            if website in content:
                pass
            else:
                # MAPING WEBSITE NAMES TO THE HOST FILE
                file.write(redirect + " " + website + "\n")

def unblock():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites()):
                file.write(line)
            # REMOVING THE WEBSITES FROM THE HOST FILE
        file.truncate()

def unblock_diag():
    messagebox.showinfo(" ", "Websites Unblocked !")

def block_diag():
    messagebox.showinfo(" ", "Websites Blocked !")

def websiteadd_diag():
    messagebox.showinfo(" ", "Websites Added !")

def exit():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites()):
                file.write(line)
            # REMOVING THE WEBSITES FROM THE HOST FILE
        file.truncate()
        root.destroy()
 

frame = Frame(root, width=100 , height=100)
frame.pack()
img = ImageTk.PhotoImage(Image.open('ad-blocker (3).png'))
label1 = Label(frame, image = img)
label1.pack()

entry = ck.CTkEntry(root, placeholder_text="Enter Domain names...",
                                        width=300,height=50,)
entry.pack(padx=20, pady=10)

button1 = ck.CTkButton(root, text="Add",height=40,width=120,
                            command=lambda: [websites(), websiteadd_diag()])
button1.pack(padx=20, pady=10)

button1 = ck.CTkButton(root, text="Block websites",
                height=40,width=120,command=lambda: [block(), block_diag()])
button1.pack(padx=20, pady=10)

button2 = ck.CTkButton(root, text="Unblock websites",
                height=40,width=120,command=lambda: [unblock(), unblock_diag()])
button2.pack(padx=20, pady=10)

button2 = ck.CTkButton(root, text="Exit",height=40,width=120,command=exit)
button2.pack(padx=20, pady=10)

root.protocol("WM_DELETE_WINDOW", unblock)
root.mainloop()






