import argparse

from isolation import IsolationBoard


def leer_argumentos():
    """Obtiene los parámetros ingresados por consola."""
    analizador = argparse.ArgumentParser(
        description="Juego de mesa Isolation"
    )

    analizador.add_argument(
        "--size",
        type=int,
        required=True,
        help="Tamaño del tablero (n >= 4)",
    )

    return analizador.parse_args()


def leer_movimiento(jugador: str) -> tuple[int, int]:
    """Solicita al jugador un destino con formato fila,columna."""
    while True:
        try:
            valores = input(
                f"Jugador {jugador}, ingrese destino "
                "(fila,columna): "
            ).split(",")

            if len(valores) != 2:
                raise ValueError

            fila = int(valores[0].strip())
            columna = int(valores[1].strip())

            return fila, columna

        except ValueError:
            print("Formato inválido. Ejemplo: 2,4")


def obtener_otro_jugador(
    tablero: IsolationBoard,
    jugador_actual: str,
) -> str:
    """Retorna el jugador contrario."""
    if jugador_actual == tablero.jugador1:
        return tablero.jugador2

    return tablero.jugador1


def main() -> None:
    """Ejecuta una partida de Isolation para dos jugadores."""
    argumentos = leer_argumentos()

    try:
        tablero = IsolationBoard(argumentos.size)
    except ValueError as error:
        print(error)
        return

    jugador_actual = tablero.jugador1

    print("\n=== ISOLATION ===")
    print("A comienza en (1, 1) y B en (n, n).")
    print(
        "Movimiento: horizontal, vertical o diagonal, "
        "como una reina.\n"
    )
    print(tablero)

    while True:
        if tablero.validar_derrota(jugador_actual):
            ganador = obtener_otro_jugador(
                tablero,
                jugador_actual,
            )

            print(
                f"El jugador {jugador_actual} "
                "no tiene movimientos legales."
            )
            print(f"¡Gana el jugador {ganador}!")
            break

        fila, columna = leer_movimiento(jugador_actual)

        if tablero.jugar(
            jugador_actual,
            fila,
            columna,
        ):
            print()
            print(tablero)

            jugador_actual = obtener_otro_jugador(
                tablero,
                jugador_actual,
            )
        else:
            print(
                "Movimiento inválido. Intente nuevamente."
            )


if __name__ == "__main__":
    main()
