import math

class Board:
    """Clase base para representar un tablero cuadrado de tamaño n x n."""

    __places: list[list[str]]
    __size: int

    EMPTY_SPACE = "."

    def __init__(self, n: int):
        """Crea un tablero cuadrado de tamaño n x n"""
        if n <= 0:
            raise ValueError(
                "Debe seleccionar un número positivo para el tablero"
            )
        if n < 4:
            raise ValueError(
                "Debe seleccionar un número mayor a 4 para el tablero"
            )

        self.__places = [
            [Board.EMPTY_SPACE] * n for _ in range(n)
        ]
        self.__size = n

    def __str__(self) -> str:
        """Retorna una representación legible del tablero"""

        offset = math.ceil(math.log10(self.__size))
        board = " " * offset + " "
        board += " ".join(
            chr(ord('A') + i)
            for i in range(self.__size)
        ) + "\n"

        for i, line in enumerate(self.__places, 1):
            board += f"{i} " + " ".join(line) + '\n'

        return board
    def __repr__(self) -> str:
        """Función para cuando se llama repr(self)"""
        return f"Board({self.__size})"

    def __len__(self) -> int:
        """Función para cuando se llama len(self)"""
        return self.__size

    def __check_valid_range(self, r: int) -> bool:
        """Valida que el valor esté dentro del rango del tablero"""

        if 1 > r or r > self.__size:
            return False

        return True

    def __getitem__(self, subscript: int | tuple):
        """Implementa self[subscript]"""

        if isinstance(subscript, tuple):

            if len(subscript) != 2:
                raise ValueError(
                    "Cooordinates with too many dimensions"
                )

            if not self.__check_valid_range(subscript[0]):
                raise LookupError(
                    f"Row out of range: {subscript[0]}"
                )

            if not self.__check_valid_range(subscript[1]):
                raise LookupError(
                    f"Column out of range: {subscript[1]}"
                )

            return self.__places[
                subscript[0] - 1
            ][
                subscript[1] - 1
            ]

        elif isinstance(subscript, int):

            if not self.__check_valid_range(subscript):
                raise LookupError(
                    f"Row out of range: {subscript}"
                )

            return self.__places[subscript - 1]

        else:
            raise TypeError(
                "Subscript must be integer or coordinates"
            )

    def __setitem__(self, key: tuple, value: str) -> None:
        """Implementa self[key] = value"""

        if not isinstance(key, tuple):
            raise TypeError(
                f"Subscript must be coordinates (tuple), not {type(key)}"
            )

        if len(key) != 2:
            raise ValueError(
                "Cooordinates with too many dimensions"
            )

        if not self.__check_valid_range(key[0]):
            raise LookupError(
                f"Row out of range: {key[0]}"
            )

        if not self.__check_valid_range(key[1]):
            raise LookupError(
                f"Column out of range: {key[1]}"
            )

        self.__places[key[0] - 1][key[1] - 1] = value

    def valid_move(self, r: int, c: int):
        """Valida que sea un movimiento válido"""

        return self[r, c] == Board.EMPTY_SPACE


class TicTacToeBoard(Board):

    def __init__(self, jugador1="A", jugador2="B"):
        super().__init__(5)

        self.jugador1 = jugador1
        self.jugador2 = jugador2
        n = len(self)
        self.ultima_jugada1 = (1, 1)
        self.ultima_jugada2 = (n, n)
        self[1, 1] = self.jugador1
        self[n, n] = self.jugador2

    def juego1(self, fila, columna):
        if self.ultima_jugada1 is not None or (
            self[self.ultima_jugada1] == "A"
            or self[self.ultima_jugada1] == "B"
        ):
            self[self.ultima_jugada1] = "X"

        if not self.valid_move(fila, columna):
            raise ValueError("Casilla ocupada")

        self[fila, columna] = self.jugador1
        self.ultima_jugada1 = (fila, columna)

    def juego2(self, fila, columna):
        if self.ultima_jugada2 is not None or (
            self[self.ultima_jugada2] == "A"
            or self[self.ultima_jugada2] == "B"
        ):
            self[self.ultima_jugada2] = "X"

        if not self.valid_move(fila, columna):
            raise ValueError("Casilla ocupada")

        self[fila, columna] = self.jugador2
        self.ultima_jugada2 = (fila, columna)

    def tiene_movimientos(self, fila, columna):

        direcciones = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for df, dc in direcciones:

            f = fila + df
            c = columna + dc

            while 1 <= f <= len(self) and 1 <= c <= len(self):
                if self.valid_move(f, c):
                    return True

                f += df
                c += dc

        return False

    def validate_winner(self, jugador):

        posicion = (
            self.ultima_jugada1
            if jugador == 1
            else self.ultima_jugada2
        )

        if posicion is None:
            return False

        fila, columna = posicion

        return not self.tiene_movimientos(fila, columna)


def main():

    ganador = ""

    board = TicTacToeBoard("A", "B")
    print(board)

    turno = 1

    while ganador == "":

        player = "A" if turno % 2 == 1 else "B"

        jugador_actual = (
            1 if player == "A" else 2
        )
        print(board.validate_winner(1))

        print(board.validate_winner(2))
        print("Jugador:", jugador_actual)

        print("Resultado:", board.validate_winner(jugador_actual))
        if board.validate_winner(jugador_actual):

            ganador = (
                "B" if player == "A" else "A"
            )

            break

        fila, columna = map(
            int,
            input(
                f"Ingrese jugada de jugador {player} (fila,columna): "
            ).split(",")
        )

        if turno % 2 == 1:
            board.juego1(fila, columna)
        else:
            board.juego2(fila, columna)

        print(board)

        turno += 1

    print(f"¡Gana el jugador {ganador}!")


if __name__ == "__main__":
    main()
