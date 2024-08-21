import tkinter as tk

# Creamos la ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x300")

# Creamos la pantalla para ver los números y operaciones
screen = tk.Entry(root, font=("Arial", 12), bd=10, insertwidth=2, width=35, borderwidth=4)
screen.grid(row=0, column=0, columnspan=4)

primero = None  # Esta variable contendrá el primer número
operacion = None  # Esta variable contendrá la operación a realizar

# Función para manejar la suma
def sumar():
    global primero, operacion
    primero = float(screen.get())
    operacion = 'sumar'
    screen.delete(0, tk.END)

# Función para manejar la resta
def resta():
    global primero, operacion
    primero = float(screen.get())
    operacion = 'resta'
    screen.delete(0, tk.END)

# Función para manejar la multiplicación
def multiplicacion():
    global primero, operacion
    primero = float(screen.get())
    operacion = 'multiplicacion'
    screen.delete(0, tk.END)

# Función para manejar la división
def division():
    global primero, operacion
    primero = float(screen.get())
    operacion = 'division'
    screen.delete(0, tk.END)

# Función para mostrar el resultado
def igual():
    segundo = float(screen.get())
    resultado = 0
    if operacion == 'sumar':
        resultado = primero + segundo
    elif operacion == 'resta':
        resultado = primero - segundo
    elif operacion == 'multiplicacion':
        resultado = primero * segundo
    elif operacion == 'division':
        if segundo != 0:
            resultado = primero / segundo
        else:
            resultado = "Error"
    screen.delete(0, tk.END)
    screen.insert(0, str(resultado))

# Función para agregar números a la pantalla
def agregar_numero(numero):
    screen.insert(tk.END, str(numero))

# Crear botones numéricos
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
]

for (text, row, column) in buttons:
    tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: agregar_numero(t)).grid(row=row, column=column)

# Crear botones de operaciones
button_sum = tk.Button(root, text="+", padx=20, pady=20, command=sumar)
button_sum.grid(row=1, column=3)

button_rest = tk.Button(root, text="-", padx=20, pady=20, command=resta)
button_rest.grid(row=2, column=3)

button_mult = tk.Button(root, text="*", padx=20, pady=20, command=multiplicacion)
button_mult.grid(row=3, column=3)

button_div = tk.Button(root, text="/", padx=20, pady=20, command=division)
button_div.grid(row=4, column=3)

button_equal = tk.Button(root, text="=", padx=20, pady=20, command=igual)
button_equal.grid(row=4, column=2)

# Botón para borrar la pantalla
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=lambda: screen.delete(0, tk.END))
button_clear.grid(row=4, column=0)

# Iniciamos el bucle principal de la aplicación
root.mainloop()
