import tkinter as tk
from datetime import date

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Estado de Cuenta")
ventana.geometry("800x600")

tk.Label(ventana, text="ESTADO DE CUENTA", font=("Arial", 16, "bold")).pack(pady=10)

# Clases definidas
class Cliente:
    # Definición del método o función constructora
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, domicilio):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.domicilio = domicilio  

class Cuenta:
    def __init__(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = 1000.0  # Saldo inicial
        self.movimientos = []  # Lista para almacenar los movimientos de la cuenta

    def abonar(self, cantidad):
        saldo_anterior = self.saldo
        self.saldo += cantidad
        # Agregar movimiento de abono
        movimiento = Movimiento(date.today(), "Abono", saldo_anterior, cantidad, 0, self.saldo)
        self.movimientos.append(movimiento)

    def cargar(self, cantidad):
        saldo_anterior = self.saldo
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            # Agregar movimiento de carga
            movimiento = Movimiento(date.today(), "Cargo", saldo_anterior, 0, cantidad, self.saldo)
            self.movimientos.append(movimiento)
            return True
        else:
            return False

class Movimiento:
    def __init__(self, fecha_movimiento, descripcion, saldo_anterior, abono, cargo, saldo):
        self.fecha_movimiento = fecha_movimiento
        self.descripcion = descripcion
        self.saldo_anterior = saldo_anterior
        self.abono = abono
        self.cargo = cargo
        self.saldo = saldo

class EstadoCuenta:
    def __init__(self, cliente, cuenta, fecha_ingreso, movimiento):
        self.cliente = cliente
        self.cuenta = cuenta
        self.fecha_ingreso = fecha_ingreso
        self.movimiento = movimiento

# Función para mostrar estado de cuenta
def mostrar_estado_cuenta():
    # Obtener los datos ingresados por el usuario
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    domicilio = entry_domicilio.get()
   
    # Validar entradas numéricas
    try:
        abono = float(entry_abono.get()) if entry_abono.get() else 0.0
    except ValueError:
        abono = 0.0
    try:
        cargo = float(entry_cargo.get()) if entry_cargo.get() else 0.0
    except ValueError:
        cargo = 0.0

    # Crear la instancia del cliente con los datos obtenidos
    cliente = Cliente(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, domicilio)
    cuenta = Cuenta(entry_numero_cuenta.get())  # Crear cuenta con el número ingresado
   
    # Realizar un abono o cargo según corresponda
    if abono > 0:
        cuenta.abonar(abono)
    if cargo > 0:
        if not cuenta.cargar(cargo):
            label_estado.config(text="Saldo insuficiente para realizar el cargo.")
            return

    # Mostrar los datos en una etiqueta
    estado = f"Cliente: {cliente.nombre} {cliente.apellido_paterno} {cliente.apellido_materno}\n"
    estado += f"Fecha de Nacimiento: {cliente.fecha_nacimiento}\n"
    estado += f"Domicilio: {cliente.domicilio}\n"
    estado += f"Número de Cuenta: {cuenta.numero_cuenta}\n"
    estado += f"Saldo Inicial: $1000.00\n"
    estado += f"Abono: ${abono:.2f}\n"
    estado += f"Cargo: ${cargo:.2f}\n"
    estado += f"Saldo Actual: ${cuenta.saldo:.2f}\n"
   
    # Mostrar los movimientos
    estado += "\nMovimientos:\n"
    for movimiento in cuenta.movimientos:
        estado += f"Fecha: {movimiento.fecha_movimiento}, Tipo: {movimiento.descripcion}, " \
                  f"Saldo Anterior: ${movimiento.saldo_anterior:.2f}, Abono: ${movimiento.abono:.2f}, " \
                  f"Cargo: ${movimiento.cargo:.2f}, Saldo Actual: ${movimiento.saldo:.2f}\n"

    label_estado.config(text=estado)

# Etiquetas para los datos del cliente
tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Apellido Paterno:").pack(pady=5)
entry_apellido_paterno = tk.Entry(ventana)
entry_apellido_paterno.pack(pady=5)

tk.Label(ventana, text="Apellido Materno:").pack(pady=5)
entry_apellido_materno = tk.Entry(ventana)
entry_apellido_materno.pack(pady=5)

tk.Label(ventana, text="Fecha de Nacimiento (YYYY-MM-DD):").pack(pady=5)
entry_fecha_nacimiento = tk.Entry(ventana)
entry_fecha_nacimiento.pack(pady=5)

tk.Label(ventana, text="Domicilio:").pack(pady=5)
entry_domicilio = tk.Entry(ventana)
entry_domicilio.pack(pady=5)

tk.Label(ventana, text="Número de Cuenta:").pack(pady=5)
entry_numero_cuenta = tk.Entry(ventana)
entry_numero_cuenta.pack(pady=5)

tk.Label(ventana, text="Abono:").pack(pady=5)
entry_abono = tk.Entry(ventana)
entry_abono.pack(pady=5)

tk.Label(ventana, text="Cargo:").pack(pady=5)
entry_cargo = tk.Entry(ventana)
entry_cargo.pack(pady=5)

# Botón para mostrar estado de cuenta
btn_mostrar_estado = tk.Button(ventana, text="Mostrar Estado de Cuenta", command=mostrar_estado_cuenta)
btn_mostrar_estado.pack(pady=20)

# para mostrar el estado de cuenta
label_estado = tk.Label(ventana, text="", font=("Arial", 12))
label_estado.pack(pady=20)

ventana.mainloop()
