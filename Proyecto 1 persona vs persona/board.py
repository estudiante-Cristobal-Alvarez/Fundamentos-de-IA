class Board:
    """Clase base para representar un tablero cuadrado de tamaño n x n."""

    __casillas: list[list[str]]
    __tamano: int
    ESPACIO_VACIO = "."

    def __init__(self, n: int = 3):
        """Crea un tablero cuadrado de tamaño n x n."""
        if n <= 0:
            raise ValueError(
                "El tamaño del tablero debe ser mayor que 0"
            )

        self.__casillas = [
            [Board.ESPACIO_VACIO] * n for _ in range(n)
        ]
        self.__tamano = n

    def __str__(self) -> str:
        """Retorna una representación legible del tablero."""
        ancho = len(str(self.__tamano))

        encabezado = " " * (ancho + 1)
        encabezado += " ".join(
            f"{columna:>{ancho}}"
            for columna in range(1, self.__tamano + 1)
        )

        lineas = [encabezado]

        for numero_fila, fila in enumerate(self.__casillas, 1):
            texto_fila = " ".join(
                f"{valor:>{ancho}}" for valor in fila
            )
            lineas.append(
                f"{numero_fila:>{ancho}} {texto_fila}"
            )

        return "\n".join(lineas) + "\n"

    def __repr__(self) -> str:
        """Retorna una representación técnica del tablero."""
        return f"Board({self.__tamano})"

    def __len__(self) -> int:
        """Retorna el tamaño del tablero."""
        return self.__tamano

    def __rango_valido(self, valor: int) -> bool:
        """Valida que una fila o columna esté entre 1 y n."""
        return 1 <= valor <= self.__tamano

    def __getitem__(self, indice: int | tuple):
        """Permite acceder a una fila o coordenada del tablero."""
        if isinstance(indice, tuple):
            if len(indice) != 2:
                raise ValueError(
                    "Las coordenadas deben tener fila y columna"
                )

            fila, columna = indice

            if not self.__rango_valido(fila):
                raise LookupError(
                    f"Fila fuera de rango: {fila}"
                )

            if not self.__rango_valido(columna):
                raise LookupError(
                    f"Columna fuera de rango: {columna}"
                )

            return self.__casillas[fila - 1][columna - 1]

        if isinstance(indice, int):
            if not self.__rango_valido(indice):
                raise LookupError(
                    f"Fila fuera de rango: {indice}"
                )

            return self.__casillas[indice - 1]

        raise TypeError(
            "El índice debe ser un entero o una tupla"
        )

    def __setitem__(
        self,
        coordenadas: tuple,
        valor: str,
    ) -> None:
        """Permite modificar una coordenada del tablero."""
        if not isinstance(coordenadas, tuple):
            raise TypeError(
                "El índice debe ser una tupla (fila, columna)"
            )

        if len(coordenadas) != 2:
            raise ValueError(
                "Las coordenadas deben tener fila y columna"
            )

        fila, columna = coordenadas

        if not self.__rango_valido(fila):
            raise LookupError(
                f"Fila fuera de rango: {fila}"
            )

        if not self.__rango_valido(columna):
            raise LookupError(
                f"Columna fuera de rango: {columna}"
            )

        self.__casillas[fila - 1][columna - 1] = valor

    def casilla_vacia(self, fila: int, columna: int) -> bool:
        """Retorna True si la casilla indicada está vacía."""
        return self[fila, columna] == Board.ESPACIO_VACIO


if __name__ == "__main__":
    tablero = Board(5)
    print(tablero)
