def calcular_promedio_notas():
    print("--- CALCULADORA DE NOTAS SENCILLA ---")

    notas = []

    while True:
        entrada = input(
            "Ingresa una nota (o escribe 'fin' para calcular): "
        ).strip()

        if entrada.lower() == "fin":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 100:
                notas.append(nota)
            else:
                print("Por favor, ingresa una nota válida.")
        except ValueError:
            print("Entrada no válida. Ingresa un número o la palabra 'fin'.")

    if not notas:
        print("\nNo se ingresó ninguna nota.")
        return

    promedio = sum(notas) / len(notas)

    print("\n--------------------------------")
    print(f"Notas ingresadas: {notas}")
    print(f"Total de notas: {len(notas)}")
    print(f"Promedio final: {promedio:.2f}")

    nota_minima_aprobacion = 6.0

    if promedio >= nota_minima_aprobacion:
        print("Estado: ¡APROBADO! 🎉")
    else:
        print("Estado: REPROBADO ❌")
    print("--------------------------------")


if __name__ == "__main__":
    calcular_promedio_notas()
