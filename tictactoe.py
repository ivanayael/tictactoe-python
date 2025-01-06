# Crear el tablero vacío
def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

# Mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

# Prueba inicial
tablero = crear_tablero()
mostrar_tablero(tablero)


def movimiento_valido(tablero, fila, columna):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " "

def registrar_movimiento(tablero, fila, columna, jugador):
    if movimiento_valido(tablero, fila, columna):
        tablero[fila][columna] = jugador
        return True
    return False


def verificar_victoria(tablero, jugador):
    # Comprobar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    # Comprobar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False



def jugar():
    tablero = crear_tablero()
    jugador_actual = "X"
    
    for turno in range(9):  # Máximo de 9 turnos
        mostrar_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        
        # Solicitar movimiento
        try:
            fila = int(input("Ingresa la fila (0-2): "))
            columna = int(input("Ingresa la columna (0-2): "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue
        
        if registrar_movimiento(tablero, fila, columna, jugador_actual):
            if verificar_victoria(tablero, jugador_actual):
                mostrar_tablero(tablero)
                print(f"¡El jugador {jugador_actual} gana!")
                return
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Movimiento inválido, intenta nuevamente.")
    
    mostrar_tablero(tablero)
    print("¡Es un empate!")

if __name__ == "__main__":
    jugar()
