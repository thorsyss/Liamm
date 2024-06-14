import tkinter as tk
from tkinter import messagebox

def show_popup():
    messagebox.showinfo("Popup", "Coucou")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() 
    show_popup()
    root.mainloop()


#utiliser cette commande pour executer le script pyinstaller --onefile create_file_exe.py