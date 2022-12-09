# ---------- IMPORTACIONES ----------
from data.datos1 import sudoku_ej

# ---------- FUNCIONES ----------

def valor_valido(sudoku, fila, columna, valor):
    '''Funcion que comprueba si un valor es válido en una casilla de un sudoku.'''
    for i in range(9):
        if sudoku[fila][i] == valor: #si el valor está ya en la fila, no es válido
            return False
        if sudoku[i][columna] == valor: #si el valor está ya en la columna, no es válido
            return False
        if sudoku[(fila // 3)*3 + i//3][(columna//3)*3 + i%3] == valor: #si el valor está ya en el cuadrado, no es válido
            return False
    #si pasa todos los tests, es válido
    return True 

def resolver(sudoku):
    '''Funcion que resuelve un sudoku'''
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0: #si hay una casilla vacía
                for valor in range(1,10): #probamos con los valores del 1 al 9
                    if valor_valido(sudoku, fila, columna, valor): #si el valor es válido
                        sudoku[fila][columna] = valor #lo ponemos en el sudoku
                        if resolver(sudoku): #si el sudoku se resuelve, lo devuelve
                            return sudoku
                        else: #si no, lo borra y prueba con el siguiente
                            sudoku[fila][columna] = 0
                return False #si no hay ningún valor válido, devuelve False
    return sudoku #si no hay ningún 0, devuelve el sudoku


def imprimir_sudoku(sudoku):
    '''Funcion que imprime el sudoku'''
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()

def ejercicio_1():
    print('Sudoku a resolver:')
    imprimir_sudoku(sudoku_ej)
    print()
    print('Sudoku resuelto:')
    imprimir_sudoku(resolver(sudoku_ej))


# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == '__main__':
    ejercicio_1()
