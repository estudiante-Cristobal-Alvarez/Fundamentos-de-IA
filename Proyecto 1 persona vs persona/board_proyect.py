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
                "Debe seleccionar un número mayor a 0 para el tablero"
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
        super().__init__(3)

        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def juego1(self, fila, columna):

        if not self.valid_move(fila, columna):
            raise ValueError("Casilla ocupada")

        self[fila, columna] = self.jugador1

    def juego2(self, fila, columna):

        if not self.valid_move(fila, columna):
            raise ValueError("Casilla ocupada")

        self[fila, columna] = self.jugador2

    def validate_winner(self, jugador):

        ficha = (
            self.jugador1
            if jugador == 1
            else self.jugador2
        )

        for fila in range(1, 4):
            if all(
                self[fila, col] == ficha
                for col in range(1, 4)
            ):
                return True

        for col in range(1, 4):
            if all(
                self[fila, col] == ficha
                for fila in range(1, 4)
            ):
                return True

        if all(
            self[i, i] == ficha
            for i in range(1, 4)
        ):
            return True

        if all(
            self[i, 4 - i] == ficha
            for i in range(1, 4)
        ):
            return True

        return False


def main():

    ganador = ""

    board = TicTacToeBoard("A", "B")

    turno = 1

    while ganador == "" and turno <= 9:

        player = "A" if turno % 2 == 1 else "B"

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

        jugador_actual = (
            1 if player == "A" else 2
        )

        if board.validate_winner(jugador_actual):
            ganador = player

        turno += 1

    if ganador:
        print(f"¡Gana el jugador {ganador}!")
    else:
        print("Empate")


if __name__ == "__main__":
    main()