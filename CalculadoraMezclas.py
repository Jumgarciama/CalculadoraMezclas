import tkinter as tk
from tkinter import ttk

# Fórmulas base (gramos)

FORMULAS = {

    "MEZ ESE REVOLCON CEREZA-LIMON": {
        "Amarillo tarta": 66,
        "Malico": 1890
    },

    "MEZ ESE REVOLCON FRESA-MANZANA": {
        "Azul bae": 22,
        "Amarillo": 67,
        "Malico": 1890
    },

}


def calcular():

    # Limpiar tabla
    for item in tabla.get_children():
        tabla.delete(item)

    formula = combo_formula.get()

    try:
        kilos_deseados = float(entry_kilos.get())
    except:
        return

    receta = FORMULAS[formula]

    total_receta_gramos = sum(receta.values())
    total_receta_kg = total_receta_gramos / 1000

    factor = kilos_deseados / total_receta_kg

    total_calculado = 0

    for ingrediente, gramos in receta.items():

        cantidad_kg = (gramos / 1000) * factor

        tabla.insert(
            "",
            tk.END,
            values=(
                ingrediente,
                f"{cantidad_kg:.3f}"
            )
        )

        total_calculado += cantidad_kg

    lbl_total.config(text=f"Total: {total_calculado:.3f} kg")


# Ventana principal

root = tk.Tk()
root.title("Calculadora de Mezclas")
root.geometry("700x500")

titulo = tk.Label(
    root,
    text="CALCULADORA DE MEZCLAS",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Fórmula:").grid(row=0, column=0, padx=5)

combo_formula = ttk.Combobox(
    frame,
    values=list(FORMULAS.keys()),
    width=30
)

combo_formula.grid(row=0, column=1)
combo_formula.current(0)

tk.Label(frame, text="Cantidad a fabricar (kg):").grid(
    row=1,
    column=0,
    padx=5,
    pady=10
)

entry_kilos = tk.Entry(frame)
entry_kilos.grid(row=1, column=1)

btn_calcular = tk.Button(
    frame,
    text="Calcular",
    command=calcular
)

btn_calcular.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=10
)

# Tabla

tabla = ttk.Treeview(
    root,
    columns=("Ingrediente", "Cantidad"),
    show="headings"
)

tabla.heading("Ingrediente", text="Ingrediente")
tabla.heading("Cantidad", text="Cantidad (kg)")

tabla.column("Ingrediente", width=400)
tabla.column("Cantidad", width=150)

tabla.pack(fill="both", expand=True, padx=20, pady=10)

lbl_total = tk.Label(
    root,
    text="Total: 0.000 kg",
    font=("Arial", 12, "bold")
)

lbl_total.pack(pady=10)

root.mainloop()