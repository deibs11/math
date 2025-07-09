import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import math
from euler import euler_mejorado
from runge import runge_kutta
from newton import newton_raphson

def parse_function(expr, variables):
    def f(*args):
        local_vars = dict(zip(variables, args))
        try:
            return eval(expr, {**local_vars, "math": math, "__builtins__": {}})
        except Exception as e:
            raise ValueError(f"Error en la función: {e}")
    return f

def calcular():
    metodo = metodo_var.get()
    try:
        for i in tabla.get_children():
            tabla.delete(i)
        expr = entry_funcion.get()
        if metodo in ["Euler Mejorado", "Runge-Kutta"]:
            f = parse_function(expr, ["x", "y"])
            x0 = float(entry_x0.get())
            y0 = float(entry_y0.get())
            xf = float(entry_xf.get())
            h = float(entry_h.get())
            n = int(abs((xf - x0) / h))
            if metodo == "Euler Mejorado":
                datos = euler_mejorado(f, x0, y0, h, n)
                df = pd.DataFrame(datos, columns=["Iteración", "x", "y"])
                tabla["columns"] = ("Iteración", "x", "y")
                for col in ("Iteración", "x", "y"):
                    tabla.heading(col, text=col)
                for _, row in df.iterrows():
                    tabla.insert("", "end", values=(
                        row["Iteración"],
                        f"{row['x']:.7f}",
                        f"{row['y']:.7f}"
                    ))
                if check_grafica.get():
                    plt.style.use('seaborn-v0_8-darkgrid')
                    plt.plot(df["x"], df["y"], marker="o", color="#007acc")
                    plt.title("Solución con Método de Euler Mejorado", fontsize=14, fontweight='bold')
                    plt.xlabel("x", fontsize=12)
                    plt.ylabel("y", fontsize=12)
                    plt.grid(True, linestyle='--', alpha=0.7)
                    plt.tight_layout()
                    plt.show()
            elif metodo == "Runge-Kutta":
                datos = runge_kutta(f, x0, y0, h, n)
                df = pd.DataFrame(datos, columns=["Iteración", "x", "y"])
                tabla["columns"] = ("Iteración", "x", "y")
                for col in ("Iteración", "x", "y"):
                    tabla.heading(col, text=col)
                for _, row in df.iterrows():
                    tabla.insert("", "end", values=(
                        row["Iteración"],
                        f"{row['x']:.7f}",
                        f"{row['y']:.7f}"
                    ))
                if check_grafica.get():
                    plt.style.use('seaborn-v0_8-darkgrid')
                    plt.plot(df["x"], df["y"], marker="o", color="#e67e22")
                    plt.title("Solución con Runge-Kutta", fontsize=14, fontweight='bold')
                    plt.xlabel("x", fontsize=12)
                    plt.ylabel("y", fontsize=12)
                    plt.grid(True, linestyle='--', alpha=0.7)
                    plt.tight_layout()
                    plt.show()
        elif metodo == "Newton-Raphson":
            f = parse_function(expr, ["x"])
            df_expr = entry_funcion_derivada.get()
            dfun = parse_function(df_expr, ["x"])
            x0 = float(entry_x0.get())
            tol = float(entry_tol.get())
            max_iter = int(entry_max_iter.get())
            datos = newton_raphson(f, dfun, x0, tol, max_iter)
            df = pd.DataFrame(datos, columns=["Iteración", "x", "f(x)"])
            tabla["columns"] = ("Iteración", "x", "f(x)")
            for col in ("Iteración", "x", "f(x)"):
                tabla.heading(col, text=col)
            for _, row in df.iterrows():
                tabla.insert("", "end", values=(
                    row["Iteración"],
                    f"{row['x']:.7f}",
                    f"{row['f(x)']:.7f}"
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI ---
ventana = tk.Tk()
ventana.title("Métodos Numéricos - GUI")
ventana.configure(bg="#f0f4f8")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#e6f2ff", fieldbackground="#e6f2ff", foreground="#003366", rowheight=25, font=('Arial', 10))
style.configure("Treeview.Heading", font=('Arial', 11, 'bold'), background="#007acc", foreground="white")
style.map("Treeview", background=[('selected', '#b3d9ff')])

label_font = ("Arial", 11)
entry_font = ("Arial", 11)
button_font = ("Arial", 11, "bold")

# Selección de método
tk.Label(ventana, text="Método:", bg="#f0f4f8", font=label_font).grid(row=0, column=0, sticky="e", pady=4)
metodo_var = tk.StringVar(value="Euler Mejorado")
metodos = ["Euler Mejorado", "Runge-Kutta", "Newton-Raphson"]
combo_metodo = ttk.Combobox(ventana, textvariable=metodo_var, values=metodos, state="readonly", font=entry_font, width=18)
combo_metodo.grid(row=0, column=1, pady=4, padx=4)

# Función
tk.Label(ventana, text="f(x, y) o f(x):", bg="#f0f4f8", font=label_font).grid(row=1, column=0, sticky="e", pady=4)
entry_funcion = tk.Entry(ventana, font=entry_font, width=20)
entry_funcion.insert(0, "x + y")
entry_funcion.grid(row=1, column=1, pady=4, padx=4)

# Derivada para Newton-Raphson
tk.Label(ventana, text="f'(x):", bg="#f0f4f8", font=label_font).grid(row=2, column=0, sticky="e", pady=4)
entry_funcion_derivada = tk.Entry(ventana, font=entry_font, width=20)
entry_funcion_derivada.insert(0, "1 + x")
entry_funcion_derivada.grid(row=2, column=1, pady=4, padx=4)

# x0
tk.Label(ventana, text="x₀:", bg="#f0f4f8", font=label_font).grid(row=3, column=0, sticky="e", pady=4)
entry_x0 = tk.Entry(ventana, font=entry_font)
entry_x0.grid(row=3, column=1, pady=4, padx=4)

# y0
tk.Label(ventana, text="y₀:", bg="#f0f4f8", font=label_font).grid(row=4, column=0, sticky="e", pady=4)
entry_y0 = tk.Entry(ventana, font=entry_font)
entry_y0.grid(row=4, column=1, pady=4, padx=4)

# x final
tk.Label(ventana, text="x final:", bg="#f0f4f8", font=label_font).grid(row=5, column=0, sticky="e", pady=4)
entry_xf = tk.Entry(ventana, font=entry_font)
entry_xf.grid(row=5, column=1, pady=4, padx=4)

# Paso h
tk.Label(ventana, text="Paso h:", bg="#f0f4f8", font=label_font).grid(row=6, column=0, sticky="e", pady=4)
entry_h = tk.Entry(ventana, font=entry_font)
entry_h.grid(row=6, column=1, pady=4, padx=4)

# Tolerancia y máximo de iteraciones para Newton-Raphson
tk.Label(ventana, text="Tolerancia:", bg="#f0f4f8", font=label_font).grid(row=7, column=0, sticky="e", pady=4)
entry_tol = tk.Entry(ventana, font=entry_font)
entry_tol.insert(0, "1e-7")
entry_tol.grid(row=7, column=1, pady=4, padx=4)

tk.Label(ventana, text="Máx. iteraciones:", bg="#f0f4f8", font=label_font).grid(row=8, column=0, sticky="e", pady=4)
entry_max_iter = tk.Entry(ventana, font=entry_font)
entry_max_iter.insert(0, "100")
entry_max_iter.grid(row=8, column=1, pady=4, padx=4)

check_grafica = tk.BooleanVar()
tk.Checkbutton(ventana, text="Mostrar gráfica", variable=check_grafica, bg="#f0f4f8", font=label_font).grid(row=9, columnspan=2, pady=4)

tk.Button(ventana, text="Calcular", command=calcular, bg="#007acc", fg="white", font=button_font, relief="raised", bd=2).grid(row=10, columnspan=2, pady=10, ipadx=10)

cols = ("Iteración", "x", "y/f(x)")
tabla = ttk.Treeview(ventana, columns=cols, show="headings", height=10)
for col in cols:
    tabla.heading(col, text=col)
tabla.grid(row=11, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

def actualizar_campos(*args):
    metodo = metodo_var.get()
    if metodo == "Newton-Raphson":
        entry_funcion_derivada.config(state="normal")
        entry_y0.config(state="disabled")
        entry_xf.config(state="disabled")
        entry_h.config(state="disabled")
        entry_tol.config(state="normal")
        entry_max_iter.config(state="normal")
    else:
        entry_funcion_derivada.config(state="disabled")
        entry_y0.config(state="normal")
        entry_xf.config(state="normal")
        entry_h.config(state="normal")
        entry_tol.config(state="disabled")
        entry_max_iter.config(state="disabled")

metodo_var.trace_add("write", actualizar_campos)
actualizar_campos()

ventana.mainloop()