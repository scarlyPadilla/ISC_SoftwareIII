usuarios_anio1 = 200
precio = 149

usuarios_anio2 = usuarios_anio1 * 1.5
usuarios_anio3 = usuarios_anio2 * 1.5

ingreso_anio1 = usuarios_anio1 * precio * 12
ingreso_anio2 = usuarios_anio2 * precio * 12
ingreso_anio3 = usuarios_anio3 * precio * 12

ingreso_total = ingreso_anio1 + ingreso_anio2 + ingreso_anio3

print("====== PROYECCIÓN DE INGRESOS ======")

print(f"Año 1 | {usuarios_anio1} usuarios | ${ingreso_anio1:.2f}")
print(f"Año 2 | {usuarios_anio2:.0f} usuarios | ${ingreso_anio2:.2f}")
print(f"Año 3 | {usuarios_anio3:.0f} usuarios | ${ingreso_anio3:.2f}")

print("------------------------------------")
print(f"Ingreso acumulado 3 años: ${ingreso_total:.2f}")
