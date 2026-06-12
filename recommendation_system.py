# Crear un sistema de recomendación simple en Python.
# El programa debe recomendar productos según los intereses de un usuario.
# Debe usar listas, diccionarios, funciones y mostrar resultados por pantalla.

productos = [
    {
        "nombre": "Curso de Python",
        "categoria": "programacion",
        "descripcion": "Curso básico para aprender programación con Python."
    },
    {
        "nombre": "Libro de Inteligencia Artificial",
        "categoria": "ia",
        "descripcion": "Libro introductorio sobre inteligencia artificial."
    },
    {
        "nombre": "Notebook para estudiantes",
        "categoria": "tecnologia",
        "descripcion": "Equipo recomendado para estudiar y programar."
    },
    {
        "nombre": "Curso de GitHub",
        "categoria": "programacion",
        "descripcion": "Curso para aprender control de versiones."
    },
    {
        "nombre": "GitHub Copilot",
        "categoria": "ia",
        "descripcion": "Herramienta de IA que ayuda a escribir código."
    }
]


def recomendar_productos(interes):
    recomendaciones = []

    for producto in productos:
        if producto["categoria"].lower() == interes.lower():
            recomendaciones.append(producto)

    return recomendaciones


def mostrar_recomendaciones(recomendaciones):
    if len(recomendaciones) == 0:
        print("No se encontraron recomendaciones para ese interés.")
    else:
        print("\nRecomendaciones encontradas:\n")

        for producto in recomendaciones:
            print("Nombre:", producto["nombre"])
            print("Categoría:", producto["categoria"])
            print("Descripción:", producto["descripcion"])
            print("-" * 40)


def main():
    print("Sistema de Recomendación con Python")
    print("Intereses disponibles: programacion, ia, tecnologia")

    interes_usuario = input("Ingresa tu interés: ")

    recomendaciones = recomendar_productos(interes_usuario)
    mostrar_recomendaciones(recomendaciones)


main()