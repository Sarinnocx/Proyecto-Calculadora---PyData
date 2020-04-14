import tkinter as tk

root = tk.Tk()
# Suma
suma_1 = tk.StringVar()
suma_2 = tk.StringVar()
# Resta
restar_1 = tk.StringVar()
restar_2 = tk.StringVar()
# Multiplicaion
multi_1 = tk.StringVar()
multi_2 = tk.StringVar()
# Division
dividir_1 = tk.StringVar()
dividir_2 = tk.StringVar()

# Mensaje a mostrar
mensaje = tk.IntVar()

# Definir


def limipiar():
    suma_1.set("")
    suma_2.set("")
    restar_1.set("")
    restar_2.set("")
    multi_1.set("")
    multi_2.set("")
    dividir_1.set("")
    dividir_2.set("")


def suma():
    num1 = int(suma_1.get())
    num2 = int(suma_2.get())
    suma = num1 + num2
    mensaje.set(suma)


def resta():
    num1 = int(restar_1.get())
    num2 = int(restar_2.get())
    resta = num1 - num2
    mensaje.set(resta)

def multiplicacion():
    num1 = int(multi_1.get())
    num2 = int(multi_2.get())
    multi = num1 * num2
    mensaje.set(multi)


def division():
    num1 = int(dividir_1.get())
    num2 = int(dividir_2.get())
    div = num1 // num2
    mensaje.set(div)

root.geometry("800x500")
root.title("Calculadora")
root.configure(bg="#ec6e2b")
tk.Label(root, text="CALCULADORA", bg="#ec6e2b", fg="white", font=("", 32)).place(x=225, y=30)

# Sumar
tk.Label(root, text='SUMAR', bg="#ec6e2b", fg='white', font=('', 24)).place(x=30, y=90)
tk.Button(root, text='=', bd=0, command=suma).place(x=290, y=100, width=80)
num1 = tk.Entry(root, justify="center", textvariable=suma_1).place(x=170, y=100, width=35)
num2 = tk.Entry(root, justify="center", textvariable=suma_2).place(x=220, y=100, width=35)

# Resta
tk.Label(root, text='RESTAR', bg="#ec6e2b", fg='white', font=('', 24)).place(x=30, y=140)
tk.Button(root, text='=', bd=0, command=resta).place(x=290, y=145, width=80)
rest1 = tk.Entry(root, justify="center", textvariable=restar_1).place(x=170, y=148, width=35)
rest2 = tk.Entry(root, justify="center", textvariable=restar_2).place(x=220, y=148, width=35)

# Multiplicacion
tk.Label(root, text='MULTIPLICAR', bg="#ec6e2b", fg='white', font=('', 24)).place(x=30, y=190)
tk.Button(root, text='=', bd=0, command=multiplicacion).place(x=365, y=200, width=80)
m1 = tk.Entry(root, justify="center", textvariable=multi_1).place(x=255, y=200, width=35)
m2 = tk.Entry(root, justify="center", textvariable=multi_2).place(x=305, y=200, width=35)

# Division
tk.Label(root, text='DIVIDIR', bg="#ec6e2b", fg='white', font=('', 24)).place(x=30, y=240)
tk.Button(root, text='=', bd=0, command=division).place(x=290, y=250, width=80)
d1 = tk.Entry(root, justify="center", textvariable=dividir_1).place(x=170, y=250, width=35)
d2 = tk.Entry(root, justify="center", textvariable=dividir_2).place(x=220, y=250, width=35)

# General de la ventana
tk.Label(root, textvariable=mensaje, bg="#ec6e2b", fg='#ecfb00', font=('', 24)).place(x=400, y=410)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=400, y=450)
tk.Button(root, text="Borrar", bd=0, command=limipiar).place(x=30, y=290, width=100)
root.mainloop()
