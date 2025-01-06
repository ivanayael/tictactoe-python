import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tic-Tac-Toe")
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugador_actual = "X"
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(3):
            for columna in range(3):
                boton = tk.Button(self.ventana, text=" ", font=("Arial", 24), width=5, height=2,
                                  command=lambda f=fila, c=columna: self.realizar_movimiento(f, c))
                boton.grid(row=fila, column=columna)
                self.botones[fila][columna] = boton

    def realizar_movimiento(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = self.jugador_actual
            self.botones[fila][columna].config(text=self.jugador_actual)
            if self.verificar_victoria(self.jugador_actual):
                messagebox.showinfo("¡Victoria!", f"¡El jugador {self.jugador_actual} gana!")
                self.ventana.destroy()
            elif all(all(cell != " " for cell in row) for row in self.tablero):
                messagebox.showinfo("Empate", "¡Es un empate!")
                self.ventana.destroy()
            else:
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def verificar_victoria(self, jugador):
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)) or all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        if all(self.tablero[i][i] == jugador for i in range(3)) or all(self.tablero[i][2 - i] == jugador for i in range(3)):
            return True
        return False

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = TicTacToe()
    juego.iniciar()
