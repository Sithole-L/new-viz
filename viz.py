import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
from data import custom_colors, famous_peeps_heights

# create the main window 
root = tk.Tk()
root.title("Height comparison App")
root.geometry("600x400")

# create input label and entry
lbl_height = tk.Label(root, text="please enter your height (in cm): ", font=('Arial', 20))
lbl_height.pack(pady=20)
height_entry = tk.Entry(root, font=('Arial', 20))
height_entry.pack()

root.mainloop()