from tkinter import *
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    fahrenheit = 32 + celsius*1.8
    return round(fahrenheit, 3)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return round(celsius, 3)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return round(celsius,3)

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return round(kelvin, 3)

def convert():
    try:
        celsius = celsius_input.get(1.0, END)
        fahrenheit = fahrenheit_input.get(1.0, END)
        kelvin = kelvin_input.get(1.0, END)

        if len(celsius) > 1:
            celsius = int(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)

        elif len(kelvin)>1:
            kelvin = int(kelvin)
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = celsius_to_fahrenheit(celsius)

        elif len(fahrenheit) > 1:
            fahrenheit = int(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = celsius_to_kelvin(celsius)


        celsius_input.delete(1.0, END)
        celsius_input.insert(END, celsius)
        fahrenheit_input.delete(1.0, END)
        fahrenheit_input.insert(END, fahrenheit)
        kelvin_input.delete(1.0, END)
        kelvin_input.insert(END, kelvin)


    except:
          print("ERROR")


def clear():
    celsius_input.delete(1.0, END)
    fahrenheit_input.delete(1.0, END)
    kelvin_input.delete(1.0, END)

root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.config(bg = 'black')
root.title("TEMPERATURE CONVERTER")

Label(root, text = "TEMPERATURE CONVERTER", font = 'arial 25 bold', bg = "black", fg = "yellow", height = 1).place(x = 12, y = 0)
Label(root, text = "Celsius", font = 'arial 20 bold', bg = "black", fg = "white").place(x = 50, y = 60)
Label(root, text = "Fahrenheit", font = 'arial 20 bold', bg = "black", fg = "white").place(x = 50, y = 137)
Label(root, text = "Kelvin", font = 'arial 20 bold', bg = "black", fg = "white").place(x = 50, y = 210)


celsius_input = Text(root, font = 'arial 20', height = 1, width = 14, wrap = WORD, padx = 5, pady = 5)
celsius_input.place(x=225, y = 60)

fahrenheit_input = Text(root, font = 'arial 20', height = 1, width = 14, wrap = WORD, padx = 5, pady = 5)
fahrenheit_input.place(x=225, y = 135)
    
kelvin_input = Text(root, font = 'arial 20', height = 1, width = 14, wrap = WORD, padx = 5, pady = 5)
kelvin_input.place(x=225, y = 210)

clearBtn = Button(root, text = 'Clear', font= 'arial 22 bold', padx = 5, pady = 5, command= clear)
clearBtn.place(x = 100, y= 300)

convertBtn = Button(root, text = 'Convert', font= 'arial 22 bold', padx = 5, pady = 5, command= convert)
convertBtn.place(x = 250, y= 300)                  

root.mainloop()
          

        





            
