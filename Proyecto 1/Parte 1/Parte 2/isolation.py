from board import Board


class IsolationBoard(Board):
    """Tablero para jugar Isolation con movimiento tipo reina."""

    CASILLA_BLOQUEADA = "×"

    def __init__(
        self,
        n: int = 4,
        jugador1: str = "A",
        jugador2: str = "B",
    ):
        """Construye un tablero de Isolation de tamaño n x n."""
        if n < 4:
            raise ValueError(
                "El tamaño del tablero debe ser mayor o igual a 4"
            )

        super().__init__(n)

        self.jugador1 = jugador1
        self.jugador2 = jugador2

        self.ultima_jugada1 = (1, 1)
        self.ultima_jugada2 = (n, n)

        self[1, 1] = self.jugador1
        self[n, n] = self.jugador2

    def obtener_posicion(
        self,
        jugador: str,
    ) -> tuple[int, int]:
        """Retorna la posición actual del jugador indicado."""
        if jugador == self.jugador1:
            return self.ultima_jugada1

        if jugador == self.jugador2:
            return self.ultima_jugada2

        raise ValueError(
            f"Jugador inválido: {jugador}"
        )

    def __actualizar_posicion(
        self,
        jugador: str,
        posicion: tuple[int, int],
    ) -> None:
        """Actualiza la posición guardada de un jugador."""
        if jugador == self.jugador1:
            self.ultima_jugada1 = posicion
        elif jugador == self.jugador2:
            self.ultima_jugada2 = posicion
        else:
            raise ValueError(
                f"Jugador inválido: {jugador}"
            )

    def __dentro_del_tablero(
        self,
        fila: int,
        columna: int,
    ) -> bool:
        """Retorna True si la coordenada pertenece al tablero."""
        return (
            1 <= fila <= len(self)
            and 1 <= columna <= len(self)
        )

    def __direccion_movimiento(
        self,
        fila_inicial: int,
        columna_inicial: int,
        fila_final: int,
        columna_final: int,
    ) -> tuple[int, int] | None:
        """Obtiene la dirección de un movimiento tipo reina."""
        diferencia_filas = fila_final - fila_inicial
        diferencia_columnas = columna_final - columna_inicial

        if diferencia_filas == 0 and diferencia_columnas == 0:
            return None

        if diferencia_filas == 0:
            paso_columna = (
                1 if diferencia_columnas > 0 else -1
            )
            return 0, paso_columna

        if diferencia_columnas == 0:
            paso_fila = 1 if diferencia_filas > 0 else -1
            return paso_fila, 0

        if abs(diferencia_filas) == abs(diferencia_columnas):
            paso_fila = 1 if diferencia_filas > 0 else -1
            paso_columna = (
                1 if diferencia_columnas > 0 else -1
            )
            return paso_fila, paso_columna

        return None

    def movimiento_valido(
        self,
        jugador: str,
        fila: int,
        columna: int,
    ) -> bool:
        """Valida una jugada de Isolation."""
        if jugador not in (self.jugador1, self.jugador2):
            raise ValueError(
                f"Jugador inválido: {jugador}"
            )

        if not self.__dentro_del_tablero(fila, columna):
            return False

        if not self.casilla_vacia(fila, columna):
            return False

        fila_inicial, columna_inicial = self.obtener_posicion(
            jugador
        )

        direccion = self.__direccion_movimiento(
            fila_inicial,
            columna_inicial,
            fila,
            columna,
        )

        if direccion is None:
            return False

        paso_fila, paso_columna = direccion
        fila_actual = fila_inicial + paso_fila
        columna_actual = columna_inicial + paso_columna

        while (fila_actual, columna_actual) != (fila, columna):
            if not self.casilla_vacia(
                fila_actual,
                columna_actual,
            ):
                return False

            fila_actual += paso_fila
            columna_actual += paso_columna

        return True

    def jugar(
        self,
        jugador: str,
        fila: int,
        columna: int,
    ) -> bool:
        """Realiza una jugada y bloquea la casilla abandonada."""
        if not self.movimiento_valido(
            jugador,
            fila,
            columna,
        ):
            return False

        fila_anterior, columna_anterior = self.obtener_posicion(
            jugador
        )

        self[fila_anterior, columna_anterior] = (
            IsolationBoard.CASILLA_BLOQUEADA
        )
        self[fila, columna] = jugador

        self.__actualizar_posicion(
            jugador,
            (fila, columna),
        )

        return True

    def juego1(self, fila: int, columna: int) -> bool:
        """Realiza una jugada del jugador 1."""
        return self.jugar(
            self.jugador1,
            fila,
            columna,
        )

    def juego2(self, fila: int, columna: int) -> bool:
        """Realiza una jugada del jugador 2."""
        return self.jugar(
            self.jugador2,
            fila,
            columna,
        )

    def movimientos_legales(
        self,
        jugador: str,
    ) -> list[tuple[int, int]]:
        """Genera todos los destinos legales del jugador."""
        fila, columna = self.obtener_posicion(jugador)

        direcciones = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        movimientos = []

        for diferencia_fila, diferencia_columna in direcciones:
            nueva_fila = fila + diferencia_fila
            nueva_columna = columna + diferencia_columna

            while self.__dentro_del_tablero(
                nueva_fila,
                nueva_columna,
            ):
                if not self.casilla_vacia(
                    nueva_fila,
                    nueva_columna,
                ):
                    break

                movimientos.append(
                    (nueva_fila, nueva_columna)
                )

                nueva_fila += diferencia_fila
                nueva_columna += diferencia_columna

        return movimientos

    def tiene_movimientos(self, jugador: str) -> bool:
        """Retorna True si el jugador tiene movimientos legales."""
        return bool(self.movimientos_legales(jugador))

    def validar_derrota(self, jugador: str) -> bool:
        """Retorna True si el jugador quedó sin movimientos."""
        return not self.tiene_movimientos(jugador)


if __name__ == "__main__":
    tablero = IsolationBoard(4)
    print(tablero)
