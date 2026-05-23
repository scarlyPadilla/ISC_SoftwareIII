# Parte A: Variables del producto

nombre = "EduTrack Pro"
precio_unitario = 149.00
unidades_disponibles = 30
categoria = "Software educativo"

# Calcular valor total del inventario
valor_inventario = precio_unitario * unidades_disponibles

# Mostrar reporte
print("=== REPORTE DE PRODUCTO ===\n")

print(f"Producto : {nombre}")
print(f"Categoría : {categoria}")
print(f"Precio : ${precio_unitario:.2f}")
print(f"Unidades : {unidades_disponibles}")
print(f"Valor total inventario : ${valor_inventario:.2f}")

# Parte B: Plan anual

precio_mensual = 149.00
descuento_anual = 0.20
meses = 12

# Cálculo con descuento
total_pagar = precio_mensual * meses * (1 - descuento_anual)

print("\n=== PLAN ANUAL ===\n")

print(f"Precio mensual : ${precio_mensual:.2f}")
print(f"Descuento anual : {descuento_anual*100:.0f}%")
print(f"Total a pagar : ${total_pagar:.2f}")