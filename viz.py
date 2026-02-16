import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
from data import custom_colors, famous_peeps_heights

# function to generate a bar plot
def generate_chart():
    user_height = float(height_entry.get())
    # create a list of celebrities
    celebrities = list(famous_peeps_heights.keys())

    # create a list of celebrities' heights
    celebrity_heights = [famous_peeps_heights[celebrity] for celebrity in celebrities]

    # append user's input (height)
    celebrities.append("You")
    celebrity_heights.append(user_height)

    plt.figure(figsize=(8, 6))

    # use the custom_colors list for the bar colours
    ax = sns.barplot(y=celebrity_heights, x=celebrities, palette=custom_colors, hue=celebrities)
    ax.set(ylabel = 'Height (cm)', xlabel = 'Celebrities')
    plt.title('Height Comparison With celebrities')
    # rotate a-axis labels for better visibility
    plt.xticks(rotation=45) 

    plt.show()


# create the main window 
root = tk.Tk()
root.title("Height comparison App")
root.geometry("600x400")

# create input label and entry
lbl_height = tk.Label(root, text="please enter your height (in cm): ", font=('Arial', 20))
lbl_height.pack(pady=20)
height_entry = tk.Entry(root, font=('Arial', 20))
height_entry.pack(pady=20)
input_button = tk.Button(root, font=('Arial', 20),text="Generate Chart", command=generate_chart)
input_button.pack(pady=20)

root.mainloop()