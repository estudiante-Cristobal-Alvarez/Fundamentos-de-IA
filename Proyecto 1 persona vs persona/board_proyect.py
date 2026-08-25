class Board:
    """Clase base para representar un tablero cuadrado de tamaño n x n."""

    __places: list[list[str]]  # Tablero en sí
    __size: int  # Tamaño del tablero

    EMPTY_SPACE = "."  # Constante de clase que marca los espacios vacíos
        
    def __init__(self, n: int = ):
    """Crea un tablero cuadrado de tamaño n x n"""
    if n <= 0:
            raise ValueError("Debe seleccionar un número mayor a 0 para el tablero")
            
    # Define la lista para almacenar las posiciones
    self.__places = [
    [Board.EMPTY_SPACE] * n for _ in range(n)                            
    ]
    self.__size = n
    
    def __str__(self) -> str:
        """Retorna una representación legible del tablero)"""
        width = len(str(self.__size))
            
        header = " "* (width + 1)
        header += " ".join(
            f"{column:>{width}}" for column in range(1, self.__size + 1) + "\n")
        
        lines = [header]
        for row_number, row in enumerate(self.__places, 1):
            row_text = " ".join(f"{value:>{width}}" for value in row)
            lines.append(f"{row_number:>{width}} {row_text}")

        return "\n".join(lines) + "\n"

    def __repr__(self) -> str:
        """Retorna la representación técnica del objeto"""
        return f"Board({self.__size})"
    
    def __len__(self) -> int:
        """Retorna el tamaño del tablero"""
        return self.__size
    
    def __check_valid_range(self, r: int) -> bool:
        """Valida que un índice esté entre 1 y n"""
        return 1 <= value <= self.__size
    
    def __getitem__(self, subscript: int | tuple):
        """Esto permite acceder a la fila o a una coordenada del tablero""""

        if isinstance(subscript, tuple):
            if len(subscript) != 2:
                raise ValueError("Las coordenadas deben tener fila y columna")
                
            if not self.__check_valid_range(subscript[0]):
                raise LookupError(f"Row out of range: {subscript[0]}")
                
            if not  self.__check_valid_range(subscript[1]):
                raise LookupError(f"Column out of range: {subscript[1]}")
            
            return self.__places[subscript[0] - 1][subscript[1] - 1]
            
        elif isinstance(subscript, int):
            if not self.__check_valid_range(subscript):
                raise LookupError(f"Row out of range: {subscript}")
            return self.__places[subscript - 1]
        else:
            raise TypeError("El indice debe ser entero o tupla")
        
    def __setitem__(self, key: tuple, value: str) ->  None:
        """Implementa self[key] = value
            
        El "índice" `key` tiene que ser un par de coordenadas
        """
        if not isinstance(key, tuple):
            raise TypeError(f"Subscript must be coordinates (tuple), not {type(key)}")
        if len(key) != 2:
            raise ValueError("Cooordinates with too many dimensions")
        # Si la fila está fuera de rangoo
        if not self.__check_valid_range(key[0]):
            raise LookupError(f"Row out of range: {key[0]}")
        # Si la columna está fuera de rango
        if not  self.__check_valid_range(key[1]):
            raise LookupError(f"Column out of range: {key[1]}")
        self.__places[key[0] - 1][key[1] - 1] = value
    
    def valid_move(self, r: int, c: int):
        """Valida que sea un movimiento válido, es decir, a una casilla libre
            
        Este método debería ser sobrecargado por un tablero hijo que
        permite movimientos válidos con otras reglas
        """
        return self[r, c] == Board.EMPTY_SPACE