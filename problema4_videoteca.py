# Curso: Fundamentos de Programación (213022) - Fase 5 Evaluación Final POA
# Estudiante: Juan Pablo Restrepo Marulanda
# Programa: Ingeniería Electrónica - CEAD Medellín
# Problema 4: Catálogo de Videoteca Digital

def contar_titulos_destacados(catalogo, calificacion_minima, anio_limite):
    """
    Cuenta cuántos títulos de la matriz cumplen simultáneamente con:
    - Calificación mayor o igual al umbral definido.
    - Año de lanzamiento mayor o igual al año límite establecido.
    """
    contador = 0
    for pelicula in catalogo:
        titulo = pelicula[0]
        anio = pelicula[1]
        calificacion = pelicula[2]
        genero = pelicula[3]

        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1
    return contador


def main():
    # Matriz de 7 títulos: [Título, Año de lanzamiento, Calificación (1 a 10), Género]
    videoteca = [
        ["Dune: Parte Dos", 2024, 8.6, "Ciencia Ficción"],
        ["Oppenheimer", 2023, 8.4, "Drama Histórico"],
        ["Interestelar", 2014, 8.7, "Ciencia Ficción"],
        ["Spider-Man: A través del Spider-Verso", 2023, 8.7, "Animación"],
        ["El Padrino", 1972, 9.2, "Crimen"],
        ["Top Gun: Maverick", 2022, 8.2, "Acción"],
        ["Uncharted: Fuera del mapa", 2022, 6.3, "Aventura"]
    ]

    print("=== CATÁLOGO DE VIDEOTECA DIGITAL ===")
    for fila in videoteca:
        print(f"- {fila[0]} ({fila[1]}) | Calificación: {fila[2]} | Género: {fila[3]}")

    print("\n--- Criterios de Búsqueda ---")
    try:
        umbral_calificacion = float(input("Ingrese la calificación mínima (1 a 10): "))
        anio_corte = int(input("Ingrese el año de lanzamiento límite: "))

        if not (1 <= umbral_calificacion <= 10):
            print("Error: La calificación debe estar entre 1 y 10.")
            return

        total = contar_titulos_destacados(videoteca, umbral_calificacion, anio_corte)
        print(f"\nResultado: {total} título(s) cumplen con calificación >= {umbral_calificacion} y año >= {anio_corte}.")

    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos para la calificación y el año.")


if __name__ == "__main__":
    main()
