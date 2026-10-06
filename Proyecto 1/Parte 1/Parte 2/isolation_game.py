import argparse

from agente import AgenteIsolation
from isolation import IsolationBoard


def leer_argumentos():
    """Obtiene los parámetros ingresados por consola."""
    analizador = argparse.ArgumentParser(
        description=(
            "Isolation: jugador humano contra agente inteligente"
        )
    )

    analizador.add_argument(
        "--size",
        type=int,
        required=True,
        help="Tamaño del tablero (n >= 4)",
    )

    analizador.add_argument(
        "--depth",
        type=int,
        default=3,
        help="Profundidad máxima de búsqueda (por defecto: 3)",
    )

    return analizador.parse_args()


def leer_movimiento(jugador: str) -> tuple[int, int]:
    """Solicita primero la fila y luego la columna."""
    while True:
        try:
            print(f"Turno del jugador {jugador}")
            fila = int(
                input("Ingrese la fila: ")
            )
            columna = int(
                input("Ingrese la columna: ")
            )

            return fila, columna

        except ValueError:
            print(
                "Entrada inválida. "
                "Debe ingresar números enteros."
            )


def obtener_otro_jugador(
    tablero: IsolationBoard,
    jugador_actual: str,
) -> str:
    """Retorna el jugador contrario."""
    if jugador_actual == tablero.jugador1:
        return tablero.jugador2

    return tablero.jugador1


def imprimir_estimaciones(
    agente: AgenteIsolation,
) -> None:
    """Muestra el puntaje estimado de cada movimiento posible."""
    for evaluacion in agente.evaluaciones_movimientos:
        movimiento = evaluacion["movimiento"]
        puntaje = evaluacion["valor_busqueda"]

        print(
            f"{movimiento} ptje: {puntaje:.2f}"
        )

    print(
        "\nMejor estimación: "
        f"{agente.mejor_puntaje:.2f}\n"
    )


def main() -> None:
    """Ejecuta una partida de humano contra agente."""
    argumentos = leer_argumentos()

    try:
        tablero = IsolationBoard(
            argumentos.size
        )

        agente = AgenteIsolation(
            jugador_agente=tablero.jugador2,
            jugador_rival=tablero.jugador1,
            profundidad=argumentos.depth,
        )

    except ValueError as error:
        print(error)
        return

    jugador_humano = tablero.jugador1
    jugador_agente = tablero.jugador2
    jugador_actual = tablero.jugador1

    print("\n=== ISOLATION ===")
    print(
        f"Humano: {jugador_humano} | "
        f"Agente: {jugador_agente}"
    )
    print(
        "A comienza en (1, 1) y B en (n, n)."
    )
    print(
        "Movimiento: horizontal, vertical o diagonal, "
        "como una reina de ajedrez."
    )
    print(
        "Algoritmo del agente: Minimax"
    )
    print(
        f"Profundidad de búsqueda: {argumentos.depth}\n"
    )
    print(tablero)

    while True:
        if tablero.validar_derrota(
            jugador_actual
        ):
            ganador = obtener_otro_jugador(
                tablero,
                jugador_actual,
            )

            print(
                f"El jugador {jugador_actual} "
                "no tiene movimientos legales."
            )
            print(
                f"¡Gana el jugador {ganador}!"
            )
            break

        if jugador_actual == jugador_humano:
            fila, columna = leer_movimiento(
                jugador_actual
            )

            if not tablero.jugar(
                jugador_actual,
                fila,
                columna,
            ):
                print(
                    "Movimiento inválido. "
                    "Intente nuevamente."
                )
                continue

        else:
            print(
                f"El agente {jugador_agente} "
                "está analizando...\n"
            )

            movimiento = agente.mejor_movimiento(
                tablero,
            )

            if movimiento is not None:
                imprimir_estimaciones(
                    agente,
                )

            if movimiento is None:
                print(
                    f"El agente {jugador_agente} "
                    "no tiene movimientos legales."
                )
                print(
                    f"¡Gana el jugador {jugador_humano}!"
                )
                break

            fila, columna = movimiento

            tablero.jugar(
                jugador_agente,
                fila,
                columna,
            )

            print(
                f"El agente juega en "
                f"({fila}, {columna}).\n"
            )
            print(
                "Puntaje seleccionado: "
                f"{agente.mejor_puntaje:.2f}\n"
            )
            print(
                "Nodos visitados: "
                f"{agente.nodos_visitados}\n"
            )

        print()
        print(tablero)

        jugador_actual = obtener_otro_jugador(
            tablero,
            jugador_actual,
        )


if __name__ == "__main__":
    main()