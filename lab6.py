import tkinter as tk
import random
import statistics
import math
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.title("Программа")
output = tk.Text(root, height=25, width=115)
output.pack()

def lab1_function():
    laba1 = 'Hello'
    output.delete(1.0, tk.END)
    output.insert(tk.END, laba1 + "\n")  

def lab2_function():
    one = 43
    two = 2
    output.delete(1.0, tk.END)
    output.insert(tk.END, "summ= " + str(one + two) + "\n")  
    output.insert(tk.END, "vish= " + str(one - two) + "\n")  
    output.insert(tk.END, "mult= " + str(one * two) + "\n") 
    if (one == 0) or (two == 0):
        output.insert(tk.END, "One or Two = 0\n")  
    else:
        output.insert(tk.END, "del= " + str(one/two) + "\n")  
        output.insert(tk.END, "step= " + str(one ** two) + "\n")  
        output.insert(tk.END, "comb= " + str(math.comb(one, two)) + "\n")  

def lab3_function():
    output.delete(1.0, tk.END)  
    mass = [random.randint(1, 99) for i in range(10)]
    output.insert(tk.END, "random numbers= " + str(mass) + "\n")  
    mass.sort()
    output.insert(tk.END, "sort= " + str(mass) + "\n")  
    minim = min(mass)
    maxim = max(mass)
    output.insert(tk.END, "min= " + str(minim) + "\n")  
    output.insert(tk.END, "max= " + str(maxim) + "\n")  
    output.insert(tk.END, "summ= " + str(sum(mass)) + "\n")  

def lab4_function():
    def create_file():
        for name in range(1, 4):  
            file_text = [random.randint(0, 99) for i in range(10)]
            translate = str(file_text)
            with open(f"{name}.txt", "w", encoding="utf-8") as file:
                file.write(translate)
            print(f'file {name}.txt created')

    create_file()

    file_open = askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    if file_open:
        with open(file_open, 'r', encoding='utf-8') as file:
            chtivo = file.read()
            print(chtivo)

            massiv = []
            for line in chtivo.splitlines():  
                line = line.strip().strip('[]').replace(',', ' ')
                massiv.extend(map(float, line.split()))

            sredina_numbers = statistics.mean(massiv)
            print("Average number = ", sredina_numbers)

            output.delete(1.0, tk.END)    
            output.insert(tk.END, str(massiv) + "\n")  
            output.insert(tk.END, str(sredina_numbers) + "\n")  
    else:
        print('Text file has not been selected\n\n')

def lab5_function():
    def hi():
        return "здравствуй, Путник"
    
    output.delete(1.0, tk.END)
    output.insert(tk.END, hi() + "\n")

    class Cat:
        def __init__(self, name):  
            self.name = name

        def speak(self):

            return f"{self.name} meow"

    class Dog(Cat):
        def bark(self):
            return f"{self.name} woof"
    
    my_cat = Cat('cat')
    my_dog = Dog('dog')
    output.insert(tk.END, my_cat.speak() + "\n")
    output.insert(tk.END, my_dog.speak() + "\n")


but1 = tk.Button(root, text="Лабораторная 1", command=lab1_function)
but1.pack(pady=15, padx=500)

but2 = tk.Button(root, text="Лабораторная 2", command=lab2_function)
but2.pack(pady=15, padx=500)

but3 = tk.Button(root, text="Лабораторная 3", command=lab3_function)
but3.pack(pady=15, padx=500)

but4 = tk.Button(root, text="Лабораторная 4", command=lab4_function)
but4.pack(pady=15, padx=500)

but5 = tk.Button(root, text="Лабораторная 5", command=lab5_function)
but5.pack(pady=15, padx=500)

root.mainloop()
