roadmap = [
    "v1.0 - Registro y login de usuarios",
    "v1.1 - Dashboard de proyectos",
    "v2.0 - Exportar reportes PDF",
    "v2.1 - Notificaciones por correo"
]

print("===== ROADMAP DEL PRODUCTO =====")

for i, version in enumerate(roadmap, 1):
    print(f"Versión {i}: {version}")
 
print("===============================")
print(f"Total de versiones: {len(roadmap)}")