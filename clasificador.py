plan_usuario = "basico"

if plan_usuario == "gratuito":
    print("Acceso Limitado - 3 proyectos máximo")

elif plan_usuario == "basico":
    print("Acceso Estándar - 10 proyectos")

elif plan_usuario == "profesional":
    print("Acceso Completo - proyectos ilimitados")

elif plan_usuario == "empresarial":
    print("Acceso Total + Soporte prioritario")

else:
    print("Plan no válido")