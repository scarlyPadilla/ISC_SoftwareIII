precio_venta = 850
precio_closto = 520 
costo_actual = 12000
usuario_anterior = 80
usuario_nuevo = 124

ganancia = precio_venta - precio_closto
margen = ganancia / precio_venta * 100
ahorro = costo_actual * 0.08
crecimiento = ((usuario_nuevo - usuario_anterior) / usuario_anterior * 100 )

print(f"La ganancia es de {ganancia}")
print(f"El margen de ganancia es {margen}")
print(f"El ahorro {ahorro}")
print(f"El crecimiento porcentual {crecimiento}")

