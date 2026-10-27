from copy import deepcopy
from math import inf

from isolation import IsolationBoard


VALOR_VICTORIA = 1
VALOR_DERROTA = -1


class AgenteIsolation:
    """Agente inteligente para jugar Isolation mediante Minimax."""

    def __init__(
        self,
        jugador_agente: str,
        jugador_rival: str,
        profundidad: int = 3,
    ):
        """Configura el agente y la profundidad de búsqueda."""
        if profundidad <= 0:
            raise ValueError(
                "La profundidad debe ser mayor que 0"
            )

        self.jugador_agente = jugador_agente
        self.jugador_rival = jugador_rival
        self.profundidad = profundidad

        self.nodos_visitados = 0
        self.mejor_puntaje = 0.0
        self.evaluaciones_movimientos = []

    def obtener_otro_jugador(
        self,
        jugador: str,
    ) -> str:
        """Retorna el jugador contrario."""
        if jugador == self.jugador_agente:
            return self.jugador_rival

        if jugador == self.jugador_rival:
            return self.jugador_agente

        raise ValueError(
            f"Jugador inválido: {jugador}"
        )

    def utilidad_terminal(
        self,
        jugador_turno: str,
    ) -> int:
        """Evalúa un estado terminal únicamente con -1 o 1.

        En Isolation no existe empate. Si el jugador que debe mover
        no tiene movimientos legales, pierde.
        """
        if jugador_turno == self.jugador_agente:
            return VALOR_DERROTA

        if jugador_turno == self.jugador_rival:
            return VALOR_VICTORIA

        raise ValueError(
            f"Jugador inválido: {jugador_turno}"
        )

    def valor_centro(
        self,
        tablero: IsolationBoard,
    ) -> int:
        """Retorna c en la escala -1, 0, 1.

        c = 1  si solo el agente ocupa una casilla central.
        c = -1 si solo el rival ocupa una casilla central.
        c = 0  si ninguno ocupa el centro o ambos están en centros.

        Para tableros impares existe una casilla central. Para
        tableros pares existen cuatro casillas centrales.
        """
        n = len(tablero)

        if n % 2 == 1:
            centro = (n // 2 + 1, n // 2 + 1)
            centros = {centro}
        else:
            superior = n // 2
            inferior = superior + 1
            centros = {
                (superior, superior),
                (superior, inferior),
                (inferior, superior),
                (inferior, inferior),
            }

        posicion_agente = tablero.obtener_posicion(
            self.jugador_agente
        )
        posicion_rival = tablero.obtener_posicion(
            self.jugador_rival
        )

        agente_en_centro = posicion_agente in centros
        rival_en_centro = posicion_rival in centros

        if agente_en_centro and not rival_en_centro:
            return 1

        if rival_en_centro and not agente_en_centro:
            return -1

        return 0

    def estimacion(
        self,
        tablero: IsolationBoard,
    ) -> float:
        """Estima un estado no terminal en un intervalo menor que 1.

        Se combinan dos características:
        - movilidad relativa de agente y rival;
        - control del centro c, evaluado como -1, 0 o 1.

        La estimación queda entre -0.99 y 0.99, por lo que una
        victoria (+1) o derrota (-1) terminal siempre tiene prioridad.
        """
        movimientos_agente = len(
            tablero.movimientos_legales(
                self.jugador_agente
            )
        )
        movimientos_rival = len(
            tablero.movimientos_legales(
                self.jugador_rival
            )
        )

        total_movimientos = (
            movimientos_agente + movimientos_rival
        )

        if total_movimientos == 0:
            movilidad = 0.0
        else:
            movilidad = (
                movimientos_agente - movimientos_rival
            ) / total_movimientos

        c = self.valor_centro(tablero)

        return 0.90 * movilidad + 0.09 * c

    def detalle_estimacion(
        self,
        tablero: IsolationBoard,
    ) -> dict:
        """Retorna los componentes usados por la estimación."""
        movimientos_agente = len(
            tablero.movimientos_legales(
                self.jugador_agente
            )
        )
        movimientos_rival = len(
            tablero.movimientos_legales(
                self.jugador_rival
            )
        )
        c = self.valor_centro(tablero)
        valor = self.estimacion(tablero)

        return {
            "movimientos_agente": movimientos_agente,
            "movimientos_rival": movimientos_rival,
            "c": c,
            "estimacion": valor,
        }

    def evaluar(
        self,
        tablero: IsolationBoard,
    ) -> float:
        """Alias de estimacion para mantener compatibilidad."""
        return self.estimacion(tablero)

    def minimax(
        self,
        tablero: IsolationBoard,
        profundidad: int,
        jugador_turno: str,
    ) -> float:
        """Evalúa un estado utilizando Minimax limitado."""
        self.nodos_visitados += 1

        movimientos = tablero.movimientos_legales(
            jugador_turno
        )

        if not movimientos:
            return self.utilidad_terminal(
                jugador_turno
            )

        if profundidad == 0:
            return self.estimacion(tablero)

        siguiente_jugador = self.obtener_otro_jugador(
            jugador_turno
        )

        if jugador_turno == self.jugador_agente:
            mejor_valor = -inf

            for fila, columna in movimientos:
                tablero_hijo = deepcopy(tablero)
                tablero_hijo.jugar(
                    jugador_turno,
                    fila,
                    columna,
                )

                valor = self.minimax(
                    tablero_hijo,
                    profundidad - 1,
                    siguiente_jugador,
                )
                mejor_valor = max(
                    mejor_valor,
                    valor,
                )

            return mejor_valor

        mejor_valor = inf

        for fila, columna in movimientos:
            tablero_hijo = deepcopy(tablero)
            tablero_hijo.jugar(
                jugador_turno,
                fila,
                columna,
            )

            valor = self.minimax(
                tablero_hijo,
                profundidad - 1,
                siguiente_jugador,
            )
            mejor_valor = min(
                mejor_valor,
                valor,
            )

        return mejor_valor

    def mejor_movimiento(
        self,
        tablero: IsolationBoard,
    ) -> tuple[int, int] | None:
        """Selecciona la mejor jugada con Minimax y registra puntajes."""
        movimientos = tablero.movimientos_legales(
            self.jugador_agente
        )

        if not movimientos:
            return None

        self.nodos_visitados = 0
        self.evaluaciones_movimientos = []

        mejor_valor = -inf
        movimiento_elegido = movimientos[0]

        for fila, columna in movimientos:
            tablero_hijo = deepcopy(tablero)
            tablero_hijo.jugar(
                self.jugador_agente,
                fila,
                columna,
            )

            valor = self.minimax(
                tablero_hijo,
                self.profundidad - 1,
                self.jugador_rival,
            )

            detalle = self.detalle_estimacion(
                tablero_hijo
            )

            self.evaluaciones_movimientos.append(
                {
                    "movimiento": (fila, columna),
                    "valor_busqueda": valor,
                    "estimacion_inmediata": detalle["estimacion"],
                    "c": detalle["c"],
                }
            )

            if valor > mejor_valor:
                mejor_valor = valor
                movimiento_elegido = (
                    fila,
                    columna,
                )

        self.mejor_puntaje = mejor_valor
        return movimiento_elegido



