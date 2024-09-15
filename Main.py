
import customtkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog as fd
import csv
import matplotlib.pyplot as plt

# create the w1 window
w1 = customtkinter.CTk()
w1.title('Main Menu')
w1.resizable(False, False)
w1.geometry('540x300')


#line plot stuff

def open_file():

    global file_path

    file_path = fd.askopenfilename()

    if file_path:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Extract column headers
            for header in headers:
                x_variable['menu'].add_command(label=header, command=tk._setit(x_var, header))
                y_variable['menu'].add_command(label=header, command=tk._setit(y_var, header))



def bargraph():

    root = customtkinter.CTkToplevel()
    root.title("Bar Graph")
    root.resizable(False, False)
    root.geometry('370x200')

    global x_var,y_var,x_variable,y_variable

    x_var = tk.StringVar(root)
    y_var = tk.StringVar(root)

    x_label = customtkinter.CTkLabel(root, text="X Variable:",fg_color="transparent")
    x_label.grid(row=0, column=0, padx=10, pady=10)

    x_variable = tk.OptionMenu(root, x_var, "Select X")
    x_variable.grid(row=0, column=1, padx=10, pady=10)

    y_label = customtkinter.CTkLabel(root, text="Y Variable:",fg_color="transparent")
    y_label.grid(row=1, column=0, padx=10, pady=10)

    y_variable = tk.OptionMenu(root, y_var, "Select Y")
    y_variable.grid(row=1, column=1, padx=10, pady=10)
    

    open_button = customtkinter.CTkButton(root, text="Open CSV File", command=open_file)
    open_button.grid(row=2, column=0, columnspan=2, pady=10)

    show_button = customtkinter.CTkButton(root, text="Show Graph", command=show_bar)
    show_button.grid(row=3, column=0, columnspan=2, pady=10)

    open_button = customtkinter.CTkButton(root,text='Exit',command=root.destroy)
    open_button.grid(row=3, column=5, columnspan=2, pady=10)


def show_bar():

    x_value = x_var.get()
    y_value = y_var.get()

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    x_data = [row[x_value] for row in data]
    y_data = [float(row[y_value]) for row in data]

    plt.figure(figsize=(8, 6))

    plt.bar(x_data, y_data)
    plt.xlabel(x_value)
    plt.ylabel(y_value)
    plt.title(f'{y_value} vs {x_value}')
    plt.show() 

def lineplot():
    
    root = customtkinter.CTkToplevel()
    root.title("Line Plot")
    root.geometry('370x200')

    global x_var,y_var,x_variable,y_variable

    x_var = tk.StringVar(root)
    y_var = tk.StringVar(root)

    x_label = customtkinter.CTkLabel(root, text="X Variable:",fg_color="transparent")
    x_label.grid(row=0, column=0, padx=10, pady=10)

    x_variable = tk.OptionMenu(root, x_var, "Select X")
    x_variable.grid(row=0, column=1, padx=10, pady=10)

    y_label = customtkinter.CTkLabel(root, text="Y Variable:",fg_color="transparent")
    y_label.grid(row=1, column=0, padx=10, pady=10)

    y_variable = tk.OptionMenu(root, y_var, "Select Y")
    y_variable.grid(row=1, column=1, padx=10, pady=10)

    open_button = customtkinter.CTkButton(root, text="Open CSV File", command=open_file)
    open_button.grid(row=2, column=0, columnspan=2, pady=10)

    show_button = customtkinter.CTkButton(root, text="Show Graph", command=show_graph)
    show_button.grid(row=3, column=0, columnspan=2, pady=10)

    open_button = customtkinter.CTkButton(root,text='Exit',command=root.destroy)
    open_button.grid(row=3, column=5, columnspan=2, pady=10)

def show_graph():
    x_value = x_var.get()
    y_value = y_var.get()

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    x_data = [row[x_value] for row in data]
    y_data = [float(row[y_value]) for row in data]

    plt.plot(x_data,y_data)
    plt.xlabel(x_value)
    plt.ylabel(y_value)
    plt.title(f'{y_value} vs {x_value}')
    plt.show()

def scplot():
    
    root = customtkinter.CTkToplevel()
    root.title("Scatter Plot")
    root.geometry('370x200')

    global x_var,y_var,x_variable,y_variable

    x_var = tk.StringVar(root)
    y_var = tk.StringVar(root)

    x_label = customtkinter.CTkLabel(root, text="X Variable:",fg_color="transparent")
    x_label.grid(row=0, column=0, padx=10, pady=10)

    x_variable = tk.OptionMenu(root, x_var, "Select X")
    x_variable.grid(row=0, column=1, padx=10, pady=10)

    y_label = customtkinter.CTkLabel(root, text="Y Variable:",fg_color="transparent")
    y_label.grid(row=1, column=0, padx=10, pady=10)

    y_variable = tk.OptionMenu(root, y_var, "Select Y")
    y_variable.grid(row=1, column=1, padx=10, pady=10)

    open_button = customtkinter.CTkButton(root, text="Open CSV File", command=open_file)
    open_button.grid(row=2, column=0, columnspan=2, pady=10)

    show_button = customtkinter.CTkButton(root, text="Show Graph", command=show_scatter)
    show_button.grid(row=3, column=0, columnspan=2, pady=10)

    open_button = customtkinter.CTkButton(root,text='Exit',command=root.destroy)
    open_button.grid(row=3, column=5, columnspan=2, pady=10)

def show_scatter():
    x_value = x_var.get()
    y_value = y_var.get()

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    x_data = [row[x_value] for row in data]
    y_data = [float(row[y_value]) for row in data]

    plt.scatter(x_data,y_data)
    plt.xlabel(x_value)
    plt.ylabel(y_value)
    plt.title(f'{y_value} vs {x_value}')
    plt.show()

#buttons
open_button = customtkinter.CTkButton(w1,text='Line plot',command=lineplot)
open_button.place(x=50,y=100)
open_button = customtkinter.CTkButton(w1,text='Bar Graph',command=bargraph)
open_button.place(x=200,y=100)
open_button = customtkinter.CTkButton(w1,text='Scatter plot',command=scplot)
open_button.place(x=350,y=100)

open_button = customtkinter.CTkButton(w1,text='Exit',command=w1.destroy)
open_button.place(x=200,y=200)


w1.mainloop()